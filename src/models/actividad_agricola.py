import sqlmodel
import datetime

class ActividadAgricola(sqlmodel.SQLModel, table=True):
    __tablename__ = "actividades_agricolas"
    id_actividad: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_cultivo: int = sqlmodel.Field(foreign_key="cultivos.id_cultivo")
    tipo_actividad: str
    fecha_actividad: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
    descripcion: str | None = None
    responsable: str | None = None
