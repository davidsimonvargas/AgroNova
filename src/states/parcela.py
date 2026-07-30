import reflex as rx
from sqlmodel import select

from src.models import Parcela
from src.states.auth import AuthState


class ParcelaState(rx.State):
    parcelas: list[Parcela] = []
    nombre: str = ""
    ubicacion: str = ""
    area_hectareas: str = ""
    tipo_suelo: str = ""
    error: str = ""
    exito: str = ""
    editando_id: int | None = None
    eliminar_id: int | None = None
    buscar: str = ""

    async def cargar_parcelas(self):
        auth = await self.get_state(AuthState)
        uid = auth.usuario_id
        with rx.session() as session:
            query = select(Parcela).where(Parcela.id_usuario == uid)
            if self.buscar.strip():
                query = query.where(Parcela.nombre.ilike(f"%{self.buscar.strip()}%"))
            self.parcelas = session.exec(query).all()

    def set_nombre(self, value: str):
        self.nombre = value

    def set_ubicacion(self, value: str):
        self.ubicacion = value

    def set_area(self, value: str):
        self.area_hectareas = value

    def set_tipo_suelo(self, value: str):
        self.tipo_suelo = value

    def set_buscar(self, value: str):
        self.buscar = value

    def limpiar_formulario(self):
        self.nombre = ""
        self.ubicacion = ""
        self.area_hectareas = ""
        self.tipo_suelo = ""
        self.error = ""
        self.exito = ""
        self.editando_id = None

    async def guardar(self):
        self.error = ""
        self.exito = ""
        if not self.nombre.strip():
            self.error = "El nombre de la parcela es obligatorio."
            return
        if not self.area_hectareas.strip():
            self.error = "El área en hectáreas es obligatoria."
            return
        try:
            area = float(self.area_hectareas)
            if area <= 0:
                self.error = "El área debe ser un número positivo."
                return
        except ValueError:
            self.error = "El área debe ser un número válido."
            return

        auth = await self.get_state(AuthState)
        uid = auth.usuario_id
        with rx.session() as session:
            if self.editando_id:
                parcela = session.exec(
                    select(Parcela).where(
                        Parcela.id_parcela == self.editando_id,
                        Parcela.id_usuario == uid,
                    )
                ).first()
                if parcela:
                    parcela.nombre = self.nombre.strip()
                    parcela.ubicacion = self.ubicacion.strip() or None
                    parcela.area_hectareas = area
                    parcela.tipo_suelo = self.tipo_suelo.strip() or None
                    session.add(parcela)
                    session.commit()
                    self.exito = "Parcela actualizada correctamente."
            else:
                parcela = Parcela(
                    id_usuario=uid,
                    nombre=self.nombre.strip(),
                    ubicacion=self.ubicacion.strip() or None,
                    area_hectareas=area,
                    tipo_suelo=self.tipo_suelo.strip() or None,
                )
                session.add(parcela)
                session.commit()
                self.exito = "Parcela registrada correctamente."
            self.limpiar_formulario()
            await self.cargar_parcelas()

    async def editar(self, id_parcela: int):
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            parcela = session.exec(
                select(Parcela).where(
                    Parcela.id_parcela == id_parcela,
                    Parcela.id_usuario == auth.usuario_id,
                )
            ).first()
            if parcela:
                self.nombre = parcela.nombre
                self.ubicacion = parcela.ubicacion or ""
                self.area_hectareas = str(parcela.area_hectareas)
                self.tipo_suelo = parcela.tipo_suelo or ""
                self.editando_id = parcela.id_parcela

    def confirmar_eliminar(self, id_parcela: int):
        self.eliminar_id = id_parcela

    def cancelar_eliminar(self):
        self.eliminar_id = None

    async def eliminar(self):
        if not self.eliminar_id:
            return
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            parcela = session.exec(
                select(Parcela).where(
                    Parcela.id_parcela == self.eliminar_id,
                    Parcela.id_usuario == auth.usuario_id,
                )
            ).first()
            if parcela:
                session.delete(parcela)
                session.commit()
        self.eliminar_id = None
        self.exito = "Parcela eliminada correctamente."
        await self.cargar_parcelas()
