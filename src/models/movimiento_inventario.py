import sqlmodel
import datetime

class MovimientoInventario(sqlmodel.SQLModel, table=True):
    __tablename__ = "movimientos_inventario"
    id_movimiento: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_producto: int = sqlmodel.Field(foreign_key="productos_inventario.id_producto")
    tipo_movimiento: str
    cantidad: float
    fecha_movimiento: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
