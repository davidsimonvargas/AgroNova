import reflex as rx

from src.states.auth import AuthState
from src.states.parcela import ParcelaState

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


def formulario_parcela():
    return rx.box(
        rx.vstack(
            rx.heading(
                rx.cond(ParcelaState.editando_id, "Editar Parcela", "Nueva Parcela"),
                font_size="1.25rem",
                color=AZUL_OSCURO,
            ),
            campo("Nombre de la Parcela", ParcelaState.nombre, ParcelaState.set_nombre, "Ej: Lote Norte"),
            campo("Ubicación", ParcelaState.ubicacion, ParcelaState.set_ubicacion, "Ej: Sector 3, km 15"),
            campo("Área (hectáreas)", ParcelaState.area_hectareas, ParcelaState.set_area, "Ej: 5.5", "number"),
            campo("Tipo de Suelo", ParcelaState.tipo_suelo, ParcelaState.set_tipo_suelo, "Ej: Franco arcilloso"),
            rx.box(height="0.5rem"),
            rx.hstack(
                rx.button(
                    "Cancelar",
                    on_click=ParcelaState.limpiar_formulario,
                    bg="transparent",
                    color=TEAL,
                    border="1px solid #E2E8F0",
                    border_radius="8px",
                    padding="0.75rem",
                    width="50%",
                    cursor="pointer",
                    _hover={"bg": GRIS_CLARO},
                ),
                rx.button(
                    rx.cond(ParcelaState.editando_id, "Actualizar", "Guardar"),
                    on_click=ParcelaState.guardar,
                    bg=VERDE,
                    color=BLANCO,
                    border="none",
                    border_radius="8px",
                    padding="0.75rem",
                    width="50%",
                    font_weight="600",
                    cursor="pointer",
                    _hover={"bg": "#3D9B30"},
                ),
                width="100%",
                spacing="4",
            ),
            width="100%",
        ),
        bg=BLANCO,
        padding="1.5rem",
        border_radius="12px",
        box_shadow="0 4px 6px -1px rgba(0,0,0,0.1)",
        width="100%",
    )


def tarjeta_parcela(parcela):
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(parcela.nombre, font_weight="600", font_size="1.05rem", color=AZUL_OSCURO),
                rx.hstack(
                    rx.text(f"Área: {parcela.area_hectareas} ha", font_size="0.85rem", color=TEAL),
                    rx.cond(
                        parcela.tipo_suelo,
                        rx.text(f"Suelo: {parcela.tipo_suelo}", font_size="0.85rem", color=TEAL),
                    ),
                    spacing="4",
                ),
                rx.cond(
                    parcela.ubicacion,
                    rx.text(f"Ubicación: {parcela.ubicacion}", font_size="0.85rem", color=TEAL),
                ),
                align_items="flex-start",
                width="100%",
            ),
            rx.hstack(
                rx.button(
                    "Editar",
                    on_click=lambda: ParcelaState.editar(parcela.id_parcela),
                    bg="transparent",
                    color=TEAL,
                    border="1px solid #E2E8F0",
                    border_radius="6px",
                    padding="0.4rem 0.8rem",
                    font_size="0.8rem",
                    cursor="pointer",
                    _hover={"bg": GRIS_CLARO},
                ),
                rx.button(
                    "Eliminar",
                    on_click=lambda: ParcelaState.confirmar_eliminar(parcela.id_parcela),
                    bg="transparent",
                    color="red.500",
                    border="1px solid #FED7D7",
                    border_radius="6px",
                    padding="0.4rem 0.8rem",
                    font_size="0.8rem",
                    cursor="pointer",
                    _hover={"bg": "#FED7D7"},
                ),
                spacing="2",
            ),
            width="100%",
            justify="between",
            align_items="center",
        ),
        bg=BLANCO,
        padding="1rem 1.5rem",
        border_radius="10px",
        box_shadow="0 1px 3px rgba(0,0,0,0.1)",
        width="100%",
    )


def modal_eliminar():
    return rx.cond(
        ParcelaState.eliminar_id,
        rx.box(
            rx.center(
                rx.vstack(
                    rx.text("¿Eliminar parcela?", font_weight="600", font_size="1.1rem", color=AZUL_OSCURO),
                    rx.text("Esta acción no se puede deshacer. Los cultivos asociados se conservarán.", font_size="0.9rem", color=TEAL),
                    rx.hstack(
                        rx.button(
                            "Cancelar",
                            on_click=ParcelaState.cancelar_eliminar,
                            bg="transparent",
                            color=TEAL,
                            border="1px solid #E2E8F0",
                            border_radius="8px",
                            padding="0.75rem",
                            width="50%",
                            cursor="pointer",
                        ),
                        rx.button(
                            "Eliminar",
                            on_click=ParcelaState.eliminar,
                            bg="red.500",
                            color=BLANCO,
                            border="none",
                            border_radius="8px",
                            padding="0.75rem",
                            width="50%",
                            font_weight="600",
                            cursor="pointer",
                            _hover={"bg": "#E53E3E"},
                        ),
                        width="100%",
                        spacing="4",
                    ),
                    bg=BLANCO,
                    padding="2rem",
                    border_radius="12px",
                    box_shadow="0 10px 25px rgba(0,0,0,0.15)",
                    max_width="400px",
                    width="100%",
                ),
                width="100%",
                height="100%",
            ),
            position="fixed",
            top="0",
            left="0",
            width="100%",
            height="100%",
            bg="rgba(0,0,0,0.5)",
            z_index="1000",
        ),
    )


@rx.page(route="/parcelas", title="Mis Parcelas - AgroNova")
def parcelas_page() -> rx.Component:
    return rx.box(
        rx.link("← Volver al Dashboard", href="/dashboard", color=TEAL, font_size="0.9rem", padding="1rem", _hover={"color": VERDE}),
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.heading("Mis Parcelas", font_size="1.5rem", color=AZUL_OSCURO),
                    rx.button(
                        "+ Nueva Parcela",
                        on_click=ParcelaState.limpiar_formulario,
                        bg=VERDE,
                        color=BLANCO,
                        border="none",
                        border_radius="8px",
                        padding="0.6rem 1.2rem",
                        font_weight="600",
                        cursor="pointer",
                        _hover={"bg": "#3D9B30"},
                    ),
                    width="100%",
                    justify="between",
                ),
                rx.cond(
                    ParcelaState.exito != "",
                    rx.box(
                        rx.text(ParcelaState.exito, color=VERDE, font_size="0.875rem"),
                        padding="0.75rem",
                        bg="#E6F7E4",
                        border_radius="8px",
                        width="100%",
                    ),
                ),
                rx.cond(
                    ParcelaState.error != "",
                    rx.box(
                        rx.text(ParcelaState.error, color="red.500", font_size="0.875rem"),
                        padding="0.75rem",
                        bg="#FED7D7",
                        border_radius="8px",
                        width="100%",
                    ),
                ),
                rx.hstack(
                    rx.input(
                        value=ParcelaState.buscar,
                        on_change=ParcelaState.set_buscar,
                        placeholder="Buscar por nombre...",
                        variant="soft",
                        color="black",
                        width="100%",
                        padding="5px 14px",
                        border="1px solid #E2E8F0",
                        border_radius="8px",
                        font_size="0.95rem",
                        outline="none",
                        _focus={"border_color": VERDE},
                    ),
                    rx.button(
                        "Buscar",
                        on_click=ParcelaState.cargar_parcelas,
                        bg=TEAL,
                        color=BLANCO,
                        border="none",
                        border_radius="8px",
                        padding="0.75rem 1.5rem",
                        cursor="pointer",
                        _hover={"bg": "#0F5264"},
                    ),
                    width="100%",
                    spacing="2",
                ),
                rx.vstack(
                    rx.foreach(
                        ParcelaState.parcelas,
                        tarjeta_parcela,
                    ),
                    width="100%",
                    spacing="4",
                ),
            rx.cond(
                ParcelaState.parcelas.length() == 0,
                rx.text("No tienes parcelas registradas. ¡Crea una nueva!", color=TEAL, padding="2rem"),
            ),
                formulario_parcela(),
                modal_eliminar(),
                width="100%",
                max_width="800px",
                align_items="flex-start",
            ),
            width="100%",
            padding="1rem 2rem 2rem 2rem",
        ),
        width="100%",
        min_height="100vh",
        bg=GRIS_CLARO,
        on_mount=ParcelaState.cargar_parcelas,
    )
