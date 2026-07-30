import reflex as rx
from sqlmodel import select

from src.models import Cultivo, Parcela, ActividadAgricola, Gasto, Ingreso
from src.states.auth import AuthState


class ReportesState(rx.State):
    cargando: bool = False
    vista_activa: str = "produccion"

    total_cosechado: str = "0"
    cultivos_produccion: str = "0"

    prod_por_cultivo: list[dict] = []
    prod_por_parcela: list[dict] = []

    total_gastos: str = "S/ 0.00"
    total_ingresos: str = "S/ 0.00"
    rentabilidad: str = "S/ 0.00"
    rentabilidad_positiva: bool = True
    gastos_por_parcela: list[dict] = []
    ingresos_por_parcela: list[dict] = []

    rendimiento_parcelas: list[dict] = []

    total_parcelas: str = "0"
    total_area: str = "0"
    total_cultivos: str = "0"
    cultivos_activos: str = "0"
    total_actividades: str = "0"

    async def _get_parcelas_ids(self):
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            ids = session.exec(
                select(Parcela.id_parcela).where(Parcela.id_usuario == auth.usuario_id)
            ).all()
            return ids, auth

    def set_vista(self, vista: str):
        self.vista_activa = vista
        if vista == "produccion":
            return ReportesState.cargar_reporte_produccion()
        elif vista == "costos":
            return ReportesState.cargar_reporte_costos()
        elif vista == "rendimiento":
            return ReportesState.cargar_rendimiento()
        elif vista == "estadisticas":
            return ReportesState.cargar_estadisticas()

    async def cargar_reporte_produccion(self):
        self.cargando = True
        yield
        parcelas_ids, auth = await self._get_parcelas_ids()
        if not parcelas_ids:
            self.total_cosechado = "0"
            self.cultivos_produccion = "0"
            self.prod_por_cultivo = []
            self.prod_por_parcela = []
            self.cargando = False
            return

        with rx.session() as session:
            cultivos = session.exec(
                select(Cultivo).where(Cultivo.id_parcela.in_(parcelas_ids))
            ).all()
            cultivos_ids = [c.id_cultivo for c in cultivos]

            cosechas = []
            if cultivos_ids:
                cosechas = session.exec(
                    select(ActividadAgricola).where(
                        ActividadAgricola.id_cultivo.in_(cultivos_ids),
                        ActividadAgricola.tipo_actividad == "Cosecha",
                    )
                ).all()

            cultivo_map = {c.id_cultivo: c for c in cultivos}
            parcelas = session.exec(
                select(Parcela).where(Parcela.id_parcela.in_(parcelas_ids))
            ).all()
            parcela_map = {p.id_parcela: p for p in parcelas}

            prod_por_cultivo = {}
            for c in cosechas:
                cultivo = cultivo_map.get(c.id_cultivo)
                nombre = cultivo.nombre_cultivo if cultivo else f"ID {c.id_cultivo}"
                cantidad = 0
                if c.descripcion:
                    try:
                        cantidad = float(c.descripcion.split()[0])
                    except (ValueError, IndexError):
                        cantidad = 1
                else:
                    cantidad = 1
                prod_por_cultivo[nombre] = prod_por_cultivo.get(nombre, 0) + cantidad

            total = sum(prod_por_cultivo.values())
            self.total_cosechado = f"{total:.1f} unidades"
            self.cultivos_produccion = str(len(prod_por_cultivo))
            self.prod_por_cultivo = [
                {
                    "nombre": k,
                    "cantidad": f"{v:.1f}",
                    "porcentaje": f"{round(v / total * 100, 1)}%" if total else "0%",
                    "barra": f"{round(v / total * 100, 1)}" if total else "0",
                }
                for k, v in sorted(prod_por_cultivo.items(), key=lambda x: -x[1])
            ]

            prod_por_parcela = {}
            for c in cosechas:
                cultivo = cultivo_map.get(c.id_cultivo)
                if cultivo:
                    parcela = parcela_map.get(cultivo.id_parcela)
                    nombre_parcela = parcela.nombre if parcela else f"ID {cultivo.id_parcela}"
                    cantidad = 0
                    if c.descripcion:
                        try:
                            cantidad = float(c.descripcion.split()[0])
                        except (ValueError, IndexError):
                            cantidad = 1
                    else:
                        cantidad = 1
                    prod_por_parcela[nombre_parcela] = prod_por_parcela.get(nombre_parcela, 0) + cantidad

            self.prod_por_parcela = [
                {"nombre": k, "cantidad": f"{v:.1f} unidades"}
                for k, v in sorted(prod_por_parcela.items(), key=lambda x: -x[1])
            ]
        self.cargando = False

    async def cargar_reporte_costos(self):
        self.cargando = True
        yield
        parcelas_ids, _ = await self._get_parcelas_ids()
        if not parcelas_ids:
            self.total_gastos = "S/ 0.00"
            self.total_ingresos = "S/ 0.00"
            self.rentabilidad = "S/ 0.00"
            self.rentabilidad_positiva = True
            self.gastos_por_parcela = []
            self.ingresos_por_parcela = []
            self.cargando = False
            return

        with rx.session() as session:
            gastos = session.exec(
                select(Gasto).where(Gasto.id_parcela.in_(parcelas_ids))
            ).all()
            ingresos = session.exec(
                select(Ingreso).where(Ingreso.id_parcela.in_(parcelas_ids))
            ).all()

            parcelas = session.exec(
                select(Parcela).where(Parcela.id_parcela.in_(parcelas_ids))
            ).all()
            parcela_map = {p.id_parcela: p.nombre for p in parcelas}

            total_gastos = sum(g.monto for g in gastos)
            total_ingresos = sum(i.monto for i in ingresos)
            renta = total_ingresos - total_gastos

            self.total_gastos = f"S/ {total_gastos:.2f}"
            self.total_ingresos = f"S/ {total_ingresos:.2f}"
            self.rentabilidad = f"S/ {renta:.2f}"
            self.rentabilidad_positiva = renta >= 0

            gastos_por_parcela = {}
            for g in gastos:
                nombre = parcela_map.get(g.id_parcela, f"ID {g.id_parcela}")
                gastos_por_parcela[nombre] = gastos_por_parcela.get(nombre, 0) + g.monto
            self.gastos_por_parcela = [
                {"nombre": k, "monto": f"S/ {v:.2f}"}
                for k, v in sorted(gastos_por_parcela.items(), key=lambda x: -x[1])
            ]

            ingresos_por_parcela = {}
            for i in ingresos:
                nombre = parcela_map.get(i.id_parcela, f"ID {i.id_parcela}")
                ingresos_por_parcela[nombre] = ingresos_por_parcela.get(nombre, 0) + i.monto
            self.ingresos_por_parcela = [
                {"nombre": k, "monto": f"S/ {v:.2f}"}
                for k, v in sorted(ingresos_por_parcela.items(), key=lambda x: -x[1])
            ]
        self.cargando = False

    async def cargar_rendimiento(self):
        self.cargando = True
        yield
        parcelas_ids, _ = await self._get_parcelas_ids()
        if not parcelas_ids:
            self.rendimiento_parcelas = []
            self.cargando = False
            return

        with rx.session() as session:
            parcelas = session.exec(
                select(Parcela).where(Parcela.id_parcela.in_(parcelas_ids))
            ).all()

            rendimiento = []
            for p in parcelas:
                cultivos = session.exec(
                    select(Cultivo).where(Cultivo.id_parcela == p.id_parcela)
                ).all()
                total_cosechas = 0
                for c in cultivos:
                    cosechas = session.exec(
                        select(ActividadAgricola).where(
                            ActividadAgricola.id_cultivo == c.id_cultivo,
                            ActividadAgricola.tipo_actividad == "Cosecha",
                        )
                    ).all()
                    for cosecha in cosechas:
                        if cosecha.descripcion:
                            try:
                                total_cosechas += float(cosecha.descripcion.split()[0])
                            except (ValueError, IndexError):
                                total_cosechas += 1
                        else:
                            total_cosechas += 1

                rendimiento_ha = round(total_cosechas / p.area_hectareas, 2) if p.area_hectareas > 0 else 0
                rendimiento.append({
                    "nombre": p.nombre,
                    "area": f"{p.area_hectareas:.1f} ha",
                    "total_cosechado": f"{total_cosechas:.1f} unid",
                    "rendimiento_ha": f"{rendimiento_ha:.1f} unid/ha",
                    "cultivos_activos": str(sum(1 for c in cultivos if c.estado not in ("finalizado", "cosechado"))),
                })

            self.rendimiento_parcelas = sorted(
                rendimiento,
                key=lambda x: -float(x["rendimiento_ha"].split()[0]) if x["rendimiento_ha"].split()[0].replace(".", "").isdigit() else 0
            )
        self.cargando = False

    async def cargar_estadisticas(self):
        self.cargando = True
        yield
        parcelas_ids, _ = await self._get_parcelas_ids()

        total_parcelas = len(parcelas_ids)
        total_area = 0
        total_cultivos = 0
        cultivos_activos_val = 0
        total_actividades = 0

        if parcelas_ids:
            with rx.session() as session:
                parcelas = session.exec(
                    select(Parcela).where(Parcela.id_parcela.in_(parcelas_ids))
                ).all()
                total_area = sum(p.area_hectareas for p in parcelas)

                cultivos = session.exec(
                    select(Cultivo).where(Cultivo.id_parcela.in_(parcelas_ids))
                ).all()
                total_cultivos = len(cultivos)
                cultivos_activos_val = sum(1 for c in cultivos if c.estado not in ("finalizado", "cosechado"))

                cultivos_ids = [c.id_cultivo for c in cultivos]
                if cultivos_ids:
                    total_actividades = len(session.exec(
                        select(ActividadAgricola).where(ActividadAgricola.id_cultivo.in_(cultivos_ids))
                    ).all())

        self.total_parcelas = str(total_parcelas)
        self.total_area = str(round(total_area, 2))
        self.total_cultivos = str(total_cultivos)
        self.cultivos_activos = str(cultivos_activos_val)
        self.total_actividades = str(total_actividades)
        self.cargando = False
