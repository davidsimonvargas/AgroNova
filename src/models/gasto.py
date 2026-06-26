import sqlmodel
import datetime

class Gasto(sqlmodel.SQLModel, table=True):
    __tablename__ = "gastos"
    id_gasto: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_parcela: int = sqlmodel.Field(foreign_key="parcelas.id_parcela")
    concepto: str
    monto: float
    fecha_gasto: datetime.date
