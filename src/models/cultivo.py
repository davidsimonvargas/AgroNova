import sqlmodel
import datetime

class Cultivo(sqlmodel.SQLModel, table=True):
    __tablename__ = "cultivos"
    id_cultivo: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_parcela: int = sqlmodel.Field(foreign_key="parcelas.id_parcela")
    nombre_cultivo: str
    variedad: str | None = None
    fecha_siembra: datetime.date
    area_sembrada: float
    estado: str
