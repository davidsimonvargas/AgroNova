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
    ultimo_acceso: str = ""
    mensaje_bienvenida: str = ""
    offline: bool = False
    mostrar_contraseña: bool = False

    def set_correo(self, value: str):
        self.correo = value

    def set_contraseña(self, value: str):
        self.contraseña = value

    def toggle_mostrar_contraseña(self):
        self.mostrar_contraseña = not self.mostrar_contraseña

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

    def check_offline(self):
        self.offline = True
        self.error = "Sin conexión a internet. Verifica tu conexión e intenta de nuevo."

    def login(self):
        self.error = ""
        self.campos_faltantes = []
        self.mensaje_bienvenida = ""

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
                    self.ultimo_acceso = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                    self.mensaje_bienvenida = f"¡Bienvenido, {result.nombres}! Has iniciado sesión el {self.ultimo_acceso}."
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
        self.ultimo_acceso = ""
        self.mensaje_bienvenida = ""
        return rx.redirect("/")
