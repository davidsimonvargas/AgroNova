import sqlmodel
import datetime

class Observacion(sqlmodel.SQLModel, table=True):
    __tablename__ = "observaciones"
    id_observacion: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_cultivo: int = sqlmodel.Field(foreign_key="cultivos.id_cultivo")
    id_usuario: int = sqlmodel.Field(foreign_key="usuarios.id_usuario")
    observacion: str
    fecha_observacion: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
