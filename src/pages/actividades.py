import reflex as rx

from src.states.actividad import ActividadState

AZUL_OSCURO = "#14283C"
VERDE = "#4CB43C"
TEAL = "#146478"
BLANCO = "#FFFFFF"
GRIS_CLARO = "#F5F7FA"

TIPOS_ACTIVIDAD = [
    "Riego", "Fertilizacion", "Pesticida", "Poda", "Cosecha",
]

TIPO_ICONOS = {
    "Riego": "💧", "Fertilizacion": "🧪", "Pesticida": "🧴",
    "Poda": "✂️", "Cosecha": "🌾",
}


def select_cultivo():
    return rx.vstack(
        rx.text("Cultivo", font_size="0.875rem", font_weight="500", color=AZUL_OSCURO, width="100%"),
        rx.select(
            ActividadState.cultivos,
            value=ActividadState.id_cultivo,
            on_change=ActividadState.set_cultivo,
            placeholder="Selecciona un cultivo",
            width="100%",
            padding="0.75rem 1rem",
            border="1px solid #E2E8F0",
            border_radius="8px",
        ),
        width="100%",
    )


def select_tipo():
    return rx.vstack(
        rx.text("Tipo de Actividad", font_size="0.875rem", font_weight="500", color=AZUL_OSCURO, width="100%"),
        rx.select(
            TIPOS_ACTIVIDAD,
            value=ActividadState.tipo_actividad,
            on_change=ActividadState.set_tipo,
            placeholder="Selecciona tipo de actividad",
            width="100%",
            padding="0.75rem 1rem",
            border="1px solid #E2E8F0",
            border_radius="8px",
        ),
        width="100%",
    )


def formulario_actividad():
    return rx.box(
        rx.vstack(
            rx.heading(
                rx.cond(ActividadState.editando_id, "Editar Actividad", ActividadState.tipo_label),
                font_size="1.25rem", color=AZUL_OSCURO,
            ),
            select_cultivo(),
            select_tipo(),
            rx.vstack(
                rx.text("Fecha", font_size="0.875rem", font_weight="500", color=AZUL_OSCURO, width="100%"),
                rx.input(
                    value=ActividadState.fecha_actividad,
                    on_change=ActividadState.set_fecha,
                    type="datetime-local",
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
                width="100%",
            ),
            rx.vstack(
                rx.text("Descripción / Detalles", font_size="0.875rem", font_weight="500", color=AZUL_OSCURO, width="100%"),
                rx.text_area(
                    value=ActividadState.descripcion,
                    on_change=ActividadState.set_descripcion,
                    placeholder=ActividadState.descripcion_placeholder,
                    width="100%",
                    padding="0.75rem 1rem",
                    border="1px solid #E2E8F0",
                    border_radius="8px",
                    font_size="0.95rem",
                    outline="none",
                    min_height="100px",
                    _focus={"border_color": VERDE},
                ),
                width="100%",
            ),
            rx.vstack(
                rx.text("Responsable", font_size="0.875rem", font_weight="500", color=AZUL_OSCURO, width="100%"),
                rx.input(
                    value=ActividadState.responsable,
                    on_change=ActividadState.set_responsable,
                    placeholder="Nombre del responsable",
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
                width="100%",
            ),
            rx.hstack(
                rx.button("Cancelar", on_click=ActividadState.limpiar_formulario,
                    bg="transparent", color=TEAL, border="1px solid #E2E8F0",
                    border_radius="8px", padding="0.75rem", width="50%", cursor="pointer",
                    _hover={"bg": GRIS_CLARO}),
                rx.button(rx.cond(ActividadState.editando_id, "Actualizar", "Guardar"),
                    on_click=ActividadState.guardar, bg=VERDE, color=BLANCO,
                    border="none", border_radius="8px", padding="0.75rem", width="50%",
                    font_weight="600", cursor="pointer", _hover={"bg": "#3D9B30"}),
                width="100%", spacing="4",
            ),
            width="100%",
        ),
        bg=BLANCO, padding="1.5rem", border_radius="12px",
        box_shadow="0 4px 6px -1px rgba(0,0,0,0.1)", width="100%",
    )


def badge_tipo(tipo: str):
    icono = TIPO_ICONOS.get(tipo, "📋")
    colores = {"Riego": "#3182CE", "Fertilizacion": "#D69E2E", "Pesticida": "#E53E3E",
               "Poda": "#805AD5", "Cosecha": VERDE}
    color = colores.get(tipo, "#A0AEC0")
    return rx.box(
        rx.text(f"{icono} {tipo}", font_size="0.8rem", font_weight="600"),
        bg=color + "15",
        color=color,
        padding="0.25rem 0.75rem",
        border_radius="12px",
        display="inline-block",
    )


def tarjeta_actividad(act):
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    badge_tipo(act.tipo_actividad),
                    rx.text(act.fecha_actividad, font_size="0.8rem", color="#A0AEC0"),
                    spacing="3",
                ),
                rx.cond(act.descripcion,
                    rx.text(act.descripcion, font_size="0.9rem", color=AZUL_OSCURO)),
                rx.cond(act.responsable,
                    rx.text(f"Responsable: {act.responsable}", font_size="0.8rem", color=TEAL)),
                align_items="flex-start", width="100%",
            ),
            rx.hstack(
                rx.button("Editar", on_click=lambda: ActividadState.editar(act.id_actividad),
                    bg="transparent", color=TEAL, border="1px solid #E2E8F0",
                    border_radius="6px", padding="0.4rem 0.8rem", font_size="0.8rem",
                    cursor="pointer", _hover={"bg": GRIS_CLARO}),
                rx.button("Eliminar", on_click=lambda: ActividadState.confirmar_eliminar(act.id_actividad),
                    bg="transparent", color="red.500", border="1px solid #FED7D7",
                    border_radius="6px", padding="0.4rem 0.8rem", font_size="0.8rem",
                    cursor="pointer", _hover={"bg": "#FED7D7"}),
                spacing="2",
            ),
            width="100%", justify="between", align_items="flex-start",
        ),
        bg=BLANCO, padding="1rem 1.5rem", border_radius="10px",
        box_shadow="0 1px 3px rgba(0,0,0,0.1)", width="100%",
    )


def modal_eliminar():
    return rx.cond(
        ActividadState.eliminar_id,
        rx.box(
            rx.center(
                rx.vstack(
                    rx.text("¿Eliminar actividad?", font_weight="600", font_size="1.1rem", color=AZUL_OSCURO),
                    rx.text("Esta acción no se puede deshacer.", font_size="0.9rem", color=TEAL),
                    rx.hstack(
                        rx.button("Cancelar", on_click=ActividadState.cancelar_eliminar,
                            bg="transparent", color=TEAL, border="1px solid #E2E8F0",
                            border_radius="8px", padding="0.75rem", width="50%", cursor="pointer"),
                        rx.button("Eliminar", on_click=ActividadState.eliminar,
                            bg="red.500", color=BLANCO, border="none",
                            border_radius="8px", padding="0.75rem", width="50%",
                            font_weight="600", cursor="pointer", _hover={"bg": "#E53E3E"}),
                        width="100%", spacing="4",
                    ),
                    bg=BLANCO, padding="2rem", border_radius="12px",
                    box_shadow="0 10px 25px rgba(0,0,0,0.15)", max_width="400px", width="100%",
                ),
                width="100%", height="100%",
            ),
            position="fixed", top="0", left="0", width="100%", height="100%",
            bg="rgba(0,0,0,0.5)", z_index="1000",
        ),
    )


@rx.page(route="/actividades", title="Actividades Agrícolas - AgroNova")
def actividades_page() -> rx.Component:
    return rx.box(
        rx.link("← Volver al Dashboard", href="/dashboard", color=TEAL, font_size="0.9rem", padding="1rem", _hover={"color": VERDE}),
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.heading("Actividades Agrícolas", font_size="1.5rem", color=AZUL_OSCURO),
                    rx.button("+ Nueva Actividad", on_click=ActividadState.limpiar_formulario,
                        bg=VERDE, color=BLANCO, border="none", border_radius="8px",
                        padding="0.6rem 1.2rem", font_weight="600", cursor="pointer",
                        _hover={"bg": "#3D9B30"}),
                    width="100%", justify="between",
                ),
                rx.cond(ActividadState.exito != "",
                    rx.box(rx.text(ActividadState.exito, color=VERDE, font_size="0.875rem"),
                        padding="0.75rem", bg="#E6F7E4", border_radius="8px", width="100%")),
                rx.cond(ActividadState.error != "",
                    rx.box(rx.text(ActividadState.error, color="red.500", font_size="0.875rem"),
                        padding="0.75rem", bg="#FED7D7", border_radius="8px", width="100%")),
                rx.hstack(
                    rx.select(
                        TIPOS_ACTIVIDAD,
                        value=ActividadState.filtro_tipo,
                        on_change=ActividadState.set_filtro_tipo,
                        placeholder="Filtrar por tipo",
                        width="100%",
                        padding="0.75rem 1rem",
                        border="1px solid #E2E8F0",
                        border_radius="8px",
                    ),
                    rx.button("Filtrar", on_click=ActividadState.cargar_actividades,
                        bg=TEAL, color=BLANCO, border="none", border_radius="8px",
                        padding="0.75rem 1.5rem", cursor="pointer", _hover={"bg": "#0F5264"}),
                    width="100%", spacing="2",
                ),
                rx.vstack(
                    rx.foreach(ActividadState.actividades, tarjeta_actividad),
                    width="100%", spacing="4",
                ),
                rx.cond(ActividadState.actividades.length() == 0,
                    rx.text("No hay actividades registradas. ¡Crea una nueva!", color=TEAL, padding="2rem")),
                formulario_actividad(),
                modal_eliminar(),
                width="100%", max_width="800px", align_items="flex-start",
            ),
            width="100%", padding="1rem 2rem 2rem 2rem",
        ),
        width="100%", min_height="100vh", bg=GRIS_CLARO,
        on_mount=[ActividadState.cargar_cultivos, ActividadState.cargar_actividades],
    )
