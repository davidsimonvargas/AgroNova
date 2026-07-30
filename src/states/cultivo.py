import reflex as rx
import datetime
from sqlmodel import select

from src.models import Cultivo, Parcela
from src.states.auth import AuthState


class CultivoState(rx.State):
    cultivos: list[Cultivo] = []
    parcelas: list[str] = []
    id_parcela: str = ""
    nombre_cultivo: str = ""
    variedad: str = ""
    fecha_siembra: str = ""
    area_sembrada: str = ""
    estado: str = "activo"
    error: str = ""
    exito: str = ""
    editando_id: int | None = None
    eliminar_id: int | None = None
    buscar: str = ""

    async def cargar_cultivos(self):
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            parcelas_ids = session.exec(
                select(Parcela.id_parcela).where(Parcela.id_usuario == auth.usuario_id)
            ).all()
            if not parcelas_ids:
                self.cultivos = []
                return
            query = select(Cultivo).where(Cultivo.id_parcela.in_(parcelas_ids))
            if self.buscar.strip():
                query = query.where(Cultivo.nombre_cultivo.ilike(f"%{self.buscar.strip()}%"))
            self.cultivos = session.exec(query).all()

    async def cargar_parcelas(self):
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            parcelas = session.exec(
                select(Parcela).where(Parcela.id_usuario == auth.usuario_id)
            ).all()
            self.parcelas = [f"{p.id_parcela} - {p.nombre}" for p in parcelas]

    def set_parcela(self, value: str):
        self.id_parcela = value

    def set_nombre(self, value: str):
        self.nombre_cultivo = value

    def set_variedad(self, value: str):
        self.variedad = value

    def set_fecha(self, value: str):
        self.fecha_siembra = value

    def set_area(self, value: str):
        self.area_sembrada = value

    def set_estado(self, value: str):
        self.estado = value

    def set_buscar(self, value: str):
        self.buscar = value

    def limpiar_formulario(self):
        self.id_parcela = ""
        self.nombre_cultivo = ""
        self.variedad = ""
        self.fecha_siembra = ""
        self.area_sembrada = ""
        self.estado = "activo"
        self.error = ""
        self.exito = ""
        self.editando_id = None

    async def guardar(self):
        self.error = ""
        self.exito = ""
        if not self.id_parcela:
            self.error = "Selecciona una parcela."
            return
        id_parcela = int(self.id_parcela.split(" - ")[0])
        if not self.nombre_cultivo.strip():
            self.error = "El nombre del cultivo es obligatorio."
            return
        if not self.fecha_siembra.strip():
            self.error = "La fecha de siembra es obligatoria."
            return
        try:
            area = float(self.area_sembrada) if self.area_sembrada else 0
        except ValueError:
            self.error = "El área debe ser un número válido."
            return
        try:
            fecha = datetime.date.fromisoformat(self.fecha_siembra.strip())
        except ValueError:
            self.error = "Fecha inválida. Usa formato YYYY-MM-DD."
            return

        with rx.session() as session:
            if self.editando_id:
                cultivo = session.exec(
                    select(Cultivo).where(Cultivo.id_cultivo == self.editando_id)
                ).first()
                if cultivo:
                    cultivo.id_parcela = id_parcela
                    cultivo.nombre_cultivo = self.nombre_cultivo.strip()
                    cultivo.variedad = self.variedad.strip() or None
                    cultivo.fecha_siembra = fecha
                    cultivo.area_sembrada = area
                    cultivo.estado = self.estado
                    session.add(cultivo)
                    session.commit()
                    self.exito = "Cultivo actualizado correctamente."
            else:
                cultivo = Cultivo(
                    id_parcela=id_parcela,
                    nombre_cultivo=self.nombre_cultivo.strip(),
                    variedad=self.variedad.strip() or None,
                    fecha_siembra=fecha,
                    area_sembrada=area,
                    estado=self.estado,
                )
                session.add(cultivo)
                session.commit()
                self.exito = "Cultivo registrado correctamente."
            self.limpiar_formulario()
            await self.cargar_cultivos()

    async def editar(self, id_cultivo: int):
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            cultivo = session.exec(
                select(Cultivo).where(Cultivo.id_cultivo == id_cultivo)
            ).first()
            if cultivo:
                for p in self.parcelas:
                    if p.startswith(f"{cultivo.id_parcela} - "):
                        self.id_parcela = p
                        break
                if not self.id_parcela:
                    self.id_parcela = str(cultivo.id_parcela)
                self.nombre_cultivo = cultivo.nombre_cultivo
                self.variedad = cultivo.variedad or ""
                self.fecha_siembra = cultivo.fecha_siembra.isoformat()
                self.area_sembrada = str(cultivo.area_sembrada)
                self.estado = cultivo.estado
                self.editando_id = cultivo.id_cultivo

    def confirmar_eliminar(self, id_cultivo: int):
        self.eliminar_id = id_cultivo

    def cancelar_eliminar(self):
        self.eliminar_id = None

    async def eliminar(self):
        if not self.eliminar_id:
            return
        with rx.session() as session:
            cultivo = session.exec(
                select(Cultivo).where(Cultivo.id_cultivo == self.eliminar_id)
            ).first()
            if cultivo:
                session.delete(cultivo)
                session.commit()
        self.eliminar_id = None
        self.exito = "Cultivo eliminado correctamente."
        await self.cargar_cultivos()
