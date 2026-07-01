import reflex as rx
import hashlib
import datetime
from sqlmodel import select

from src.models import Usuario


class AuthState(rx.State):
    correo: str = ""
    contraseña: str = ""
    error: str = ""
    usuario_id: int | None = None
    usuario_nombre: str = ""
    usuario_rol: str = ""
    campos_faltantes: list[str] = []

    def set_correo(self, value: str):
        self.correo = value

    def set_contraseña(self, value: str):
        self.contraseña = value

    @rx.var(cache=True)
    def autenticado(self) -> bool:
        return self.usuario_id is not None

    def validar_campos(self) -> bool:
        faltantes = []
        if not self.correo.strip():
            faltantes.append("correo")
        if not self.contraseña.strip():
            faltantes.append("contraseña")
        self.campos_faltantes = faltantes
        return len(faltantes) == 0

    def login(self):
        self.error = ""
        self.campos_faltantes = []

        if not self.validar_campos():
            return

        try:
            with rx.session() as session:
                contraseña_hash = hashlib.sha256(
                    self.contraseña.encode()
                ).hexdigest()
                result = session.exec(
                    select(Usuario).where(
                        Usuario.correo == self.correo.strip(),
                        Usuario.contraseña_hash == contraseña_hash,
                        Usuario.estado == True,
                    )
                ).first()

                if result:
                    self.usuario_id = result.id_usuario
                    self.usuario_nombre = f"{result.nombres} {result.apellidos}"
                    self.usuario_rol = result.rol
                    self.correo = ""
                    self.contraseña = ""
                    return rx.redirect("/dashboard")
                else:
                    self.error = "Credenciales inválidas. Verifica tu correo y contraseña."
        except Exception:
            self.error = "Error de conexión. Verifica tu conexión a internet."

    def cerrar_sesion(self):
        self.usuario_id = None
        self.usuario_nombre = ""
        self.usuario_rol = ""
        self.correo = ""
        self.contraseña = ""
        self.error = ""
        return rx.redirect("/")
