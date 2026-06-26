import sqlmodel
import datetime

class Ingreso(sqlmodel.SQLModel, table=True):
    __tablename__ = "ingresos"
    id_ingreso: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_parcela: int = sqlmodel.Field(foreign_key="parcelas.id_parcela")
    concepto: str
    monto: float
    fecha_ingreso: datetime.date
