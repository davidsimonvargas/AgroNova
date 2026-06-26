import sqlmodel
import datetime

class Recomendacion(sqlmodel.SQLModel, table=True):
    __tablename__ = "recomendaciones"
    id_recomendacion: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_incidencia: int = sqlmodel.Field(foreign_key="incidencias.id_incidencia")
    id_tecnico: int = sqlmodel.Field(foreign_key="usuarios.id_usuario")
    recomendacion: str
    fecha_recomendacion: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
