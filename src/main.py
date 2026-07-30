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
from src.pages.perfil import perfil_page
from src.pages.parcelas import parcelas_page
from src.pages.cultivos import cultivos_page
from src.pages.actividades import actividades_page
from src.pages.reportes import reportes_page

app = rx.App()
