import sqlmodel
import datetime

class PrediccionCosecha(sqlmodel.SQLModel, table=True):
    __tablename__ = "predicciones_cosecha"
    id_prediccion: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_cultivo: int = sqlmodel.Field(foreign_key="cultivos.id_cultivo")
    rendimiento_estimado: float
    margen_error: float | None = None
    fecha_prediccion: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
