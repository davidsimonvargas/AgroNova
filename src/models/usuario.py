import sqlmodel
import datetime

class Usuario(sqlmodel.SQLModel, table=True):
    __tablename__ = "usuarios"
    id_usuario: int | None = sqlmodel.Field(default=None, primary_key=True)
    nombres: str
    apellidos: str
    correo: str
    contraseña_hash: str
    telefono: str | None = None
    rol: str
    fecha_registro: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
    estado: bool = True
