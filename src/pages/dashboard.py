import reflex as rx

from src.states.auth import AuthState

AZUL_OSCURO = "#14283C"
VERDE = "#4CB43C"
TEAL = "#146478"
BLANCO = "#FFFFFF"
GRIS_CLARO = "#F5F7FA"


def sidebar():
    return rx.vstack(
        rx.image(src="/logo_app_web.jpg", height="60px", width="auto", border_radius="8px"),
        rx.text("AgroNova", font_size="1.25rem", font_weight="700", color=BLANCO),
        rx.divider(border_color="rgba(255,255,255,0.2)", width="100%"),
        rx.vstack(
            rx.text(f"Bienvenido, {AuthState.usuario_nombre}", font_size="0.85rem", color="rgba(255,255,255,0.8)"),
            rx.text(f"Rol: {AuthState.usuario_rol}", font_size="0.8rem", color="rgba(255,255,255,0.6)"),
            width="100%",
        ),
        rx.spacer(),
        rx.button(
            "Cerrar Sesión",
            on_click=AuthState.cerrar_sesion,
            bg="rgba(255,255,255,0.1)",
            color=BLANCO,
            border="1px solid rgba(255,255,255,0.2)",
            border_radius="8px",
            padding="0.5rem 1rem",
            width="100%",
            _hover={"bg": "rgba(255,255,255,0.2)"},
        ),
        width="250px",
        height="100vh",
        bg=AZUL_OSCURO,
        padding="1.5rem",
        align_items="flex-start",
    )


def contenido():
    return rx.vstack(
        rx.heading("Panel Principal", font_size="1.5rem", color=AZUL_OSCURO),
        rx.text("Selecciona una opción del menú para comenzar.", color=TEAL),
        rx.grid(
            rx.box(
                rx.text("Parcelas", font_weight="600", color=AZUL_OSCURO),
                rx.text("Gestiona tus parcelas registradas", font_size="0.85rem", color=TEAL),
                bg=BLANCO,
                padding="1.5rem",
                border_radius="10px",
                box_shadow="0 1px 3px rgba(0,0,0,0.1)",
                width="100%",
            ),
            rx.box(
                rx.text("Cultivos", font_weight="600", color=AZUL_OSCURO),
                rx.text("Controla tus cultivos activos", font_size="0.85rem", color=TEAL),
                bg=BLANCO,
                padding="1.5rem",
                border_radius="10px",
                box_shadow="0 1px 3px rgba(0,0,0,0.1)",
                width="100%",
            ),
            rx.box(
                rx.text("Actividades", font_weight="600", color=AZUL_OSCURO),
                rx.text("Registra riegos, fertilización y más", font_size="0.85rem", color=TEAL),
                bg=BLANCO,
                padding="1.5rem",
                border_radius="10px",
                box_shadow="0 1px 3px rgba(0,0,0,0.1)",
                width="100%",
            ),
            rx.box(
                rx.text("Reportes", font_weight="600", color=AZUL_OSCURO),
                rx.text("Consulta indicadores y rendimiento", font_size="0.85rem", color=TEAL),
                bg=BLANCO,
                padding="1.5rem",
                border_radius="10px",
                box_shadow="0 1px 3px rgba(0,0,0,0.1)",
                width="100%",
            ),
            columns="2",
            spacing="4",
            width="100%",
        ),
        width="100%",
        padding="2rem",
        align_items="flex-start",
    )


@rx.page(route="/dashboard", title="Dashboard - AgroNova")
def dashboard_page() -> rx.Component:
    return rx.hstack(
        sidebar(),
        contenido(),
        width="100%",
        min_height="100vh",
        bg=GRIS_CLARO,
    )
