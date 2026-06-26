import sqlmodel

class ProductoInventario(sqlmodel.SQLModel, table=True):
    __tablename__ = "productos_inventario"
    id_producto: int | None = sqlmodel.Field(default=None, primary_key=True)
    nombre: str
    categoria: str | None = None
    unidad_medida: str | None = None
    stock_actual: float = 0
    stock_minimo: float = 0
