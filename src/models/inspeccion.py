import sqlmodel
import datetime

class Inspeccion(sqlmodel.SQLModel, table=True):
    __tablename__ = "inspecciones"
    id_inspeccion: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_cultivo: int = sqlmodel.Field(foreign_key="cultivos.id_cultivo")
    id_tecnico: int = sqlmodel.Field(foreign_key="usuarios.id_usuario")
    fecha_inspeccion: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
    resultado: str | None = None
