import reflex as rx

from src.models import (
    Usuario, Parcela, Cultivo, ActividadAgricola,
    Observacion, Fotografia, Inspeccion, Incidencia,
    Recomendacion, ProductoInventario, MovimientoInventario,
    Gasto, Ingreso, Alerta, DiagnosticoIA,
    PrediccionCosecha, Sincronizacion,
)
from src.pages.login import login_page
from src.pages.dashboard import dashboard_page

app = rx.App()
