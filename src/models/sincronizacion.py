import sqlmodel
import datetime

class Sincronizacion(sqlmodel.SQLModel, table=True):
    __tablename__ = "sincronizaciones"
    id_sync: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_usuario: int = sqlmodel.Field(foreign_key="usuarios.id_usuario")
    fecha_sync: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
    registros_enviados: int = 0
    estado: str
