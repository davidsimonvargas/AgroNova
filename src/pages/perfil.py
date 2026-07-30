import reflex as rx

from src.states.auth import AuthState
from src.states.perfil import PerfilState

AZUL_OSCURO = "#14283C"
VERDE = "#4CB43C"
TEAL = "#146478"
BLANCO = "#FFFFFF"
GRIS_CLARO = "#F5F7FA"


def campo(label: str, value, on_change, placeholder: str = "", tipo: str = "text"):
    return rx.vstack(
        rx.text(label, font_size="0.875rem", font_weight="500", color=AZUL_OSCURO, width="100%"),
        rx.input(
            value=value,
            on_change=on_change,
            placeholder=placeholder,
            type=tipo,
            variant="soft",
            color="black",
            width="100%",
            padding="5px 14px",
            border="1px solid #E2E8F0",
            border_radius="8px",
            font_size="0.95rem",
            outline="none",
            _focus={"border_color": VERDE, "box_shadow": "0 0 0 3px rgba(76, 180, 60, 0.15)"},
        ),
        width="100%",
    )


@rx.page(route="/perfil", title="Mi Perfil - AgroNova")
def perfil_page() -> rx.Component:
    return rx.box(
        rx.link("← Volver al Dashboard", href="/dashboard", color=TEAL, font_size="0.9rem", padding="1rem", _hover={"color": VERDE}),
        rx.center(
            rx.vstack(
                rx.heading("Mi Perfil", font_size="1.5rem", color=AZUL_OSCURO),
                rx.cond(
                    PerfilState.exito != "",
                    rx.box(
                        rx.text(PerfilState.exito, color=VERDE, font_size="0.875rem"),
                        padding="0.75rem",
                        bg="#E6F7E4",
                        border_radius="8px",
                        width="100%",
                    ),
                ),
                rx.cond(
                    PerfilState.error != "",
                    rx.box(
                        rx.text(PerfilState.error, color="red.500", font_size="0.875rem"),
                        padding="0.75rem",
                        bg="#FED7D7",
                        border_radius="8px",
                        width="100%",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        campo("Nombres", PerfilState.nombres, PerfilState.set_nombres, "Tus nombres"),
                        campo("Apellidos", PerfilState.apellidos, PerfilState.set_apellidos, "Tus apellidos"),
                        campo("Correo Electrónico", PerfilState.correo, PerfilState.set_correo, "tu@correo.com", "email"),
                        campo("Teléfono", PerfilState.telefono, PerfilState.set_telefono, "Tu teléfono", "tel"),
                        rx.box(height="1rem"),
                        rx.button(
                            "Guardar Cambios",
                            on_click=PerfilState.guardar,
                            width="100%",
                            padding="0.75rem",
                            bg=VERDE,
                            color=BLANCO,
                            border="none",
                            border_radius="8px",
                            font_size="1rem",
                            font_weight="600",
                            cursor="pointer",
                            _hover={"bg": "#3D9B30"},
                        ),
                        width="100%",
                    ),
                    bg=BLANCO,
                    padding="2rem",
                    border_radius="12px",
                    box_shadow="0 4px 6px -1px rgba(0,0,0,0.1)",
                    width="100%",
                    max_width="500px",
                ),
                width="100%",
                max_width="600px",
                align_items="flex-start",
            ),
            width="100%",
            padding="1rem 2rem 2rem 2rem",
        ),
        width="100%",
        min_height="100vh",
        bg=GRIS_CLARO,
        on_mount=PerfilState.cargar_datos,
    )
