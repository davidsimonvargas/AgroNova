import reflex as rx
import datetime
from sqlmodel import select

from src.models import ActividadAgricola, Cultivo, Parcela
from src.states.auth import AuthState


class ActividadState(rx.State):
    actividades: list[ActividadAgricola] = []
    cultivos: list[str] = []
    id_cultivo: str = ""
    tipo_actividad: str = ""
    fecha_actividad: str = datetime.date.today().isoformat()
    descripcion: str = ""
    responsable: str = ""
    error: str = ""
    exito: str = ""
    editando_id: int | None = None
    eliminar_id: int | None = None
    filtro_tipo: str = ""

    async def cargar_actividades(self):
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            parcelas_ids = session.exec(
                select(Parcela.id_parcela).where(Parcela.id_usuario == auth.usuario_id)
            ).all()
            if not parcelas_ids:
                self.actividades = []
                return
            cultivos_ids = session.exec(
                select(Cultivo.id_cultivo).where(Cultivo.id_parcela.in_(parcelas_ids))
            ).all()
            if not cultivos_ids:
                self.actividades = []
                return
            query = select(ActividadAgricola).where(ActividadAgricola.id_cultivo.in_(cultivos_ids))
            if self.filtro_tipo:
                query = query.where(ActividadAgricola.tipo_actividad == self.filtro_tipo)
            query = query.order_by(ActividadAgricola.fecha_actividad.desc())
            self.actividades = session.exec(query).all()

    async def cargar_cultivos(self):
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            parcelas_ids = session.exec(
                select(Parcela.id_parcela).where(Parcela.id_usuario == auth.usuario_id)
            ).all()
            if not parcelas_ids:
                self.cultivos = []
                return
            cultivos = session.exec(
                select(Cultivo).where(Cultivo.id_parcela.in_(parcelas_ids))
            ).all()
            self.cultivos = [f"{c.id_cultivo} - {c.nombre_cultivo}" for c in cultivos]

    def set_cultivo(self, value: str):
        self.id_cultivo = value

    def set_tipo(self, value: str):
        self.tipo_actividad = value
        self.descripcion = ""

    def set_fecha(self, value: str):
        self.fecha_actividad = value

    def set_descripcion(self, value: str):
        self.descripcion = value

    def set_responsable(self, value: str):
        self.responsable = value

    def set_filtro_tipo(self, value: str):
        self.filtro_tipo = value

    def limpiar_formulario(self):
        self.id_cultivo = ""
        self.tipo_actividad = ""
        self.fecha_actividad = datetime.date.today().isoformat()
        self.descripcion = ""
        self.responsable = ""
        self.error = ""
        self.exito = ""
        self.editando_id = None

    async def guardar(self):
        self.error = ""
        self.exito = ""
        if not self.id_cultivo:
            self.error = "Selecciona un cultivo."
            return
        id_cultivo = int(self.id_cultivo.split(" - ")[0])
        if not self.tipo_actividad:
            self.error = "Selecciona el tipo de actividad."
            return

        with rx.session() as session:
            if self.editando_id:
                act = session.exec(
                    select(ActividadAgricola).where(ActividadAgricola.id_actividad == self.editando_id)
                ).first()
                if act:
                    act.id_cultivo = id_cultivo
                    act.tipo_actividad = self.tipo_actividad
                    act.descripcion = self.descripcion.strip() or None
                    act.responsable = self.responsable.strip() or None
                    if self.fecha_actividad:
                        try:
                            act.fecha_actividad = datetime.datetime.fromisoformat(self.fecha_actividad)
                        except ValueError:
                            pass
                    session.add(act)
                    session.commit()
                    self.exito = "Actividad actualizada correctamente."
            else:
                act = ActividadAgricola(
                    id_cultivo=id_cultivo,
                    tipo_actividad=self.tipo_actividad,
                    descripcion=self.descripcion.strip() or None,
                    responsable=self.responsable.strip() or None,
                )
                if self.fecha_actividad:
                    try:
                        act.fecha_actividad = datetime.datetime.fromisoformat(self.fecha_actividad)
                    except ValueError:
                        pass
                session.add(act)
                session.commit()
                self.exito = f"Actividad de {self.tipo_actividad} registrada correctamente."
            self.limpiar_formulario()
            await self.cargar_actividades()

    def editar(self, id_actividad: int):
        with rx.session() as session:
            act = session.exec(
                select(ActividadAgricola).where(ActividadAgricola.id_actividad == id_actividad)
            ).first()
            if act:
                for c in self.cultivos:
                    if c.startswith(f"{act.id_cultivo} - "):
                        self.id_cultivo = c
                        break
                if not self.id_cultivo:
                    self.id_cultivo = str(act.id_cultivo)
                self.tipo_actividad = act.tipo_actividad
                self.fecha_actividad = act.fecha_actividad.isoformat()
                self.descripcion = act.descripcion or ""
                self.responsable = act.responsable or ""
                self.editando_id = act.id_actividad

    def confirmar_eliminar(self, id_actividad: int):
        self.eliminar_id = id_actividad

    def cancelar_eliminar(self):
        self.eliminar_id = None

    async def eliminar(self):
        if not self.eliminar_id:
            return
        with rx.session() as session:
            act = session.exec(
                select(ActividadAgricola).where(ActividadAgricola.id_actividad == self.eliminar_id)
            ).first()
            if act:
                session.delete(act)
                session.commit()
        self.eliminar_id = None
        self.exito = "Actividad eliminada correctamente."
        await self.cargar_actividades()

    @rx.var(cache=True)
    def tipo_label(self) -> str:
        labels = {
            "Riego": "Registrar Riego",
            "Fertilizacion": "Registrar Fertilización",
            "Pesticida": "Registrar Aplicación de Pesticidas",
            "Poda": "Registrar Poda",
            "Cosecha": "Registrar Cosecha",
        }
        return labels.get(self.tipo_actividad, "Registrar Actividad")

    @rx.var(cache=True)
    def descripcion_placeholder(self) -> str:
        placeholders = {
            "Riego": "Cantidad de agua (L), método de riego, observaciones...",
            "Fertilizacion": "Fertilizante utilizado, dosis, observaciones...",
            "Pesticida": "Producto, dosis, motivo de aplicación, observaciones...",
            "Poda": "Tipo de poda, observaciones...",
            "Cosecha": "Cantidad cosechada, unidad de medida, calidad obtenida...",
        }
        return placeholders.get(self.tipo_actividad, "Descripción de la actividad")
