import sqlmodel
import datetime

class Incidencia(sqlmodel.SQLModel, table=True):
    __tablename__ = "incidencias"
    id_incidencia: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_cultivo: int = sqlmodel.Field(foreign_key="cultivos.id_cultivo")
    id_tecnico: int = sqlmodel.Field(foreign_key="usuarios.id_usuario")
    descripcion: str
    severidad: str
    fecha_registro: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
    estado: str
