import reflex as rx

from src.states.auth import AuthState

VERDE = "#4CB43C"
AZUL_OSCURO = "#14283C"
TEAL = "#146478"
GRIS_CLARO = "#F5F7FA"
BLANCO = "#FFFFFF"


def input_correo() -> rx.Component:
    return rx.input(
        placeholder="correo@ejemplo.com",
        type="email",
        value=AuthState.correo,
        on_change=AuthState.set_correo,
        width="100%",
        padding="0.75rem 1rem",
        border="1px solid #E2E8F0",
        border_radius="8px",
        font_size="0.95rem",
        outline="none",
        _focus={"border_color": VERDE, "box_shadow": "0 0 0 3px rgba(76, 180, 60, 0.15)"},
    )


def input_contraseña() -> rx.Component:
    return rx.input(
        placeholder="Ingresa tu contraseña",
        type="password",
        value=AuthState.contraseña,
        on_change=AuthState.set_contraseña,
        width="100%",
        padding="0.75rem 1rem",
        border="1px solid #E2E8F0",
        border_radius="8px",
        font_size="0.95rem",
        outline="none",
        _focus={"border_color": VERDE, "box_shadow": "0 0 0 3px rgba(76, 180, 60, 0.15)"},
    )


@rx.page(route="/", title="Iniciar Sesión - AgroNova")
def login_page() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.spacer(height="2rem"),
                rx.image(
                    src="/logo_app_web.jpg",
                    height="100px",
                    width="auto",
                    border_radius="12px",
                ),
                rx.text(
                    "AgroNova",
                    font_size="1.75rem",
                    font_weight="700",
                    color=AZUL_OSCURO,
                ),
                rx.text(
                    "Sistema de Gestión Agrícola",
                    font_size="0.9rem",
                    color=TEAL,
                    margin_bottom="1.5rem",
                ),
                rx.box(
                    rx.vstack(
                        rx.cond(
                            AuthState.error != "",
                            rx.box(
                                rx.text(AuthState.error, color="red.500", font_size="0.875rem"),
                                padding="0.75rem",
                                bg="#FED7D7",
                                border_radius="8px",
                                margin_bottom="1rem",
                                width="100%",
                            ),
                        ),
                        rx.text("Correo electrónico", font_size="0.875rem", font_weight="500", color=AZUL_OSCURO, width="100%"),
                        input_correo(),
                        rx.cond(
                            AuthState.campos_faltantes.contains("correo"),
                            rx.text("El correo es obligatorio", color="red.500", font_size="0.75rem", width="100%"),
                        ),
                        rx.box(height="0.75rem"),
                        rx.text("Contraseña", font_size="0.875rem", font_weight="500", color=AZUL_OSCURO, width="100%"),
                        input_contraseña(),
                        rx.cond(
                            AuthState.campos_faltantes.contains("contraseña"),
                            rx.text("La contraseña es obligatoria", color="red.500", font_size="0.75rem", width="100%"),
                        ),
                        rx.box(height="1.25rem"),
                        rx.button(
                            "Iniciar Sesión",
                            on_click=AuthState.login,
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
                        rx.box(height="0.5rem"),
                        rx.text(
                            "¿No tienes cuenta? Contacta a tu administrador",
                            font_size="0.8rem",
                            color=TEAL,
                            text_align="center",
                        ),
                        width="100%",
                        align_items="flex-start",
                    ),
                    bg=BLANCO,
                    padding="2rem",
                    border_radius="12px",
                    box_shadow="0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1)",
                    width="100%",
                    max_width="400px",
                ),
                rx.spacer(height="2rem"),
                width="100%",
                align_items="center",
            ),
            width="100%",
            min_height="100vh",
            bg=GRIS_CLARO,
        ),
        width="100%",
    )
