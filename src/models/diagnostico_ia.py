import sqlmodel
import datetime

class DiagnosticoIA(sqlmodel.SQLModel, table=True):
    __tablename__ = "diagnosticos_ia"
    id_diagnostico: int | None = sqlmodel.Field(default=None, primary_key=True)
    id_cultivo: int = sqlmodel.Field(foreign_key="cultivos.id_cultivo")
    id_fotografia: int = sqlmodel.Field(foreign_key="fotografias.id_fotografia")
    enfermedad_detectada: str | None = None
    confianza: float | None = None
    recomendacion: str | None = None
    fecha_analisis: datetime.datetime = sqlmodel.Field(default_factory=datetime.datetime.now)
