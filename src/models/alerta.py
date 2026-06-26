import sqlmodel
import datetime

class Alerta(sqlmodel.SQLModel, table=True):
    __tablename__ = "alertas"
    id_alerta: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_usuario: int = sqlmodel.Field(foreign_key="usuarios.id_usuario")
    tipo_alerta: str
    mensaje: str
    prioridad: str
    atendida: bool = False
    fecha_alerta: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
