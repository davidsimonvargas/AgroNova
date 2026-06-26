import sqlmodel
import datetime

class Parcela(sqlmodel.SQLModel, table=True):
    __tablename__ = "parcelas"
    id_parcela: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_usuario: int = sqlmodel.Field(foreign_key="usuarios.id_usuario")
    nombre: str
    ubicacion: str | None = None
    area_hectareas: float
    tipo_suelo: str | None = None
    fecha_registro: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
