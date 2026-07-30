import reflex as rx
from sqlmodel import select

from src.models import Usuario
from src.states.auth import AuthState


class PerfilState(rx.State):
    nombres: str = ""
    apellidos: str = ""
    correo: str = ""
    telefono: str = ""
    error: str = ""
    exito: str = ""

    async def cargar_datos(self):
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            usuario = session.exec(
                select(Usuario).where(Usuario.id_usuario == auth.usuario_id)
            ).first()
            if usuario:
                self.nombres = usuario.nombres
                self.apellidos = usuario.apellidos
                self.correo = usuario.correo
                self.telefono = usuario.telefono or ""

    def set_nombres(self, value: str):
        self.nombres = value

    def set_apellidos(self, value: str):
        self.apellidos = value

    def set_correo(self, value: str):
        self.correo = value

    def set_telefono(self, value: str):
        self.telefono = value

    async def guardar(self):
        self.error = ""
        self.exito = ""
        if not self.nombres.strip() or not self.apellidos.strip() or not self.correo.strip():
            self.error = "Los campos Nombre, Apellido y Correo son obligatorios."
            return
        auth = await self.get_state(AuthState)
        with rx.session() as session:
            usuario = session.exec(
                select(Usuario).where(Usuario.id_usuario == auth.usuario_id)
            ).first()
            if usuario:
                usuario.nombres = self.nombres.strip()
                usuario.apellidos = self.apellidos.strip()
                usuario.correo = self.correo.strip()
                usuario.telefono = self.telefono.strip() or None
                session.add(usuario)
                session.commit()
                auth.usuario_nombre = f"{self.nombres.strip()} {self.apellidos.strip()}"
                self.exito = "Perfil actualizado correctamente."
