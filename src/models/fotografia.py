import sqlmodel
import datetime

class Fotografia(sqlmodel.SQLModel, table=True):
    __tablename__ = "fotografias"
    id_fotografia: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_cultivo: int = sqlmodel.Field(foreign_key="cultivos.id_cultivo")
    url_imagen: str
    fecha_subida: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
