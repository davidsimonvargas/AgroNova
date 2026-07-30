import reflex as rx

from src.states.cultivo import CultivoState

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


def select_parcela():
    return rx.vstack(
        rx.text("Parcela", font_size="0.875rem", font_weight="500", color=AZUL_OSCURO, width="100%"),
        rx.select(
            CultivoState.parcelas,
            value=CultivoState.id_parcela,
            on_change=CultivoState.set_parcela,
            placeholder="Selecciona una parcela",
            width="100%",
            padding="0.75rem 1rem",
            border="1px solid #E2E8F0",
            border_radius="8px",
        ),
        width="100%",
    )


def select_estado():
    return rx.vstack(
        rx.text("Estado", font_size="0.875rem", font_weight="500", color=AZUL_OSCURO, width="100%"),
        rx.select(
            ["activo", "crecimiento", "floracion", "cosechado", "finalizado"],
            value=CultivoState.estado,
            on_change=CultivoState.set_estado,
            placeholder="Selecciona estado",
            width="100%",
            padding="0.75rem 1rem",
            border="1px solid #E2E8F0",
            border_radius="8px",
        ),
        width="100%",
    )


def formulario_cultivo():
    return rx.box(
        rx.vstack(
            rx.heading(
                rx.cond(CultivoState.editando_id, "Editar Cultivo", "Nuevo Cultivo"),
                font_size="1.25rem", color=AZUL_OSCURO,
            ),
            select_parcela(),
            campo("Nombre del Cultivo", CultivoState.nombre_cultivo, CultivoState.set_nombre, "Ej: Tomate"),
            campo("Variedad", CultivoState.variedad, CultivoState.set_variedad, "Ej: Cherry"),
            campo("Fecha de Siembra", CultivoState.fecha_siembra, CultivoState.set_fecha, "YYYY-MM-DD", "date"),
            campo("Área Sembrada (ha)", CultivoState.area_sembrada, CultivoState.set_area, "Ej: 2.5", "number"),
            select_estado(),
            rx.hstack(
                rx.button("Cancelar", on_click=CultivoState.limpiar_formulario,
                    bg="transparent", color=TEAL, border="1px solid #E2E8F0",
                    border_radius="8px", padding="0.75rem", width="50%", cursor="pointer",
                    _hover={"bg": GRIS_CLARO}),
                rx.button(rx.cond(CultivoState.editando_id, "Actualizar", "Guardar"),
                    on_click=CultivoState.guardar, bg=VERDE, color=BLANCO,
                    border="none", border_radius="8px", padding="0.75rem", width="50%",
                    font_weight="600", cursor="pointer", _hover={"bg": "#3D9B30"}),
                width="100%", spacing="4",
            ),
            width="100%",
        ),
        bg=BLANCO, padding="1.5rem", border_radius="12px",
        box_shadow="0 4px 6px -1px rgba(0,0,0,0.1)", width="100%",
    )


def badge_estado(estado: str):
    colores = {"activo": VERDE, "crecimiento": "#3182CE", "floracion": "#D69E2E",
               "cosechado": TEAL, "finalizado": "#A0AEC0"}
    color = colores.get(estado, "#A0AEC0")
    return rx.box(
        rx.text(estado, font_size="0.75rem", font_weight="600"),
        bg=color + "20",
        color=color,
        padding="0.2rem 0.6rem",
        border_radius="12px",
        display="inline-block",
    )


def tarjeta_cultivo(cultivo):
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(cultivo.nombre_cultivo, font_weight="600", font_size="1.05rem", color=AZUL_OSCURO),
                rx.hstack(
                    badge_estado(cultivo.estado),
                    rx.cond(cultivo.variedad, rx.text(f"Var: {cultivo.variedad}", font_size="0.85rem", color=TEAL)),
                    spacing="3",
                ),
                rx.text(f"Área: {cultivo.area_sembrada} ha | Siembra: {cultivo.fecha_siembra}", font_size="0.85rem", color=TEAL),
                align_items="flex-start", width="100%",
            ),
            rx.hstack(
                rx.button("Editar", on_click=lambda: CultivoState.editar(cultivo.id_cultivo),
                    bg="transparent", color=TEAL, border="1px solid #E2E8F0",
                    border_radius="6px", padding="0.4rem 0.8rem", font_size="0.8rem",
                    cursor="pointer", _hover={"bg": GRIS_CLARO}),
                rx.button("Eliminar", on_click=lambda: CultivoState.confirmar_eliminar(cultivo.id_cultivo),
                    bg="transparent", color="red.500", border="1px solid #FED7D7",
                    border_radius="6px", padding="0.4rem 0.8rem", font_size="0.8rem",
                    cursor="pointer", _hover={"bg": "#FED7D7"}),
                spacing="2",
            ),
            width="100%", justify="between", align_items="center",
        ),
        bg=BLANCO, padding="1rem 1.5rem", border_radius="10px",
        box_shadow="0 1px 3px rgba(0,0,0,0.1)", width="100%",
    )


def modal_eliminar():
    return rx.cond(
        CultivoState.eliminar_id,
        rx.box(
            rx.center(
                rx.vstack(
                    rx.text("¿Eliminar cultivo?", font_weight="600", font_size="1.1rem", color=AZUL_OSCURO),
                    rx.text("Se eliminará el registro del cultivo. Las actividades asociadas se conservarán.", font_size="0.9rem", color=TEAL),
                    rx.hstack(
                        rx.button("Cancelar", on_click=CultivoState.cancelar_eliminar,
                            bg="transparent", color=TEAL, border="1px solid #E2E8F0",
                            border_radius="8px", padding="0.75rem", width="50%", cursor="pointer"),
                        rx.button("Eliminar", on_click=CultivoState.eliminar,
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


@rx.page(route="/cultivos", title="Mis Cultivos - AgroNova")
def cultivos_page() -> rx.Component:
    return rx.box(
        rx.link("← Volver al Dashboard", href="/dashboard", color=TEAL, font_size="0.9rem", padding="1rem", _hover={"color": VERDE}),
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.heading("Mis Cultivos", font_size="1.5rem", color=AZUL_OSCURO),
                    rx.button("+ Nuevo Cultivo", on_click=CultivoState.limpiar_formulario,
                        bg=VERDE, color=BLANCO, border="none", border_radius="8px",
                        padding="0.6rem 1.2rem", font_weight="600", cursor="pointer",
                        _hover={"bg": "#3D9B30"}),
                    width="100%", justify="between",
                ),
                rx.cond(CultivoState.exito != "",
                    rx.box(rx.text(CultivoState.exito, color=VERDE, font_size="0.875rem"),
                        padding="0.75rem", bg="#E6F7E4", border_radius="8px", width="100%")),
                rx.cond(CultivoState.error != "",
                    rx.box(rx.text(CultivoState.error, color="red.500", font_size="0.875rem"),
                        padding="0.75rem", bg="#FED7D7", border_radius="8px", width="100%")),
                rx.hstack(
                    rx.input(value=CultivoState.buscar, on_change=CultivoState.set_buscar,
                        placeholder="Buscar por nombre...", variant="soft", color="black",
                        width="100%", padding="5px 14px", border="1px solid #E2E8F0",
                        border_radius="8px", font_size="0.95rem", outline="none",
                        _focus={"border_color": VERDE}),
                    rx.button("Buscar", on_click=CultivoState.cargar_cultivos,
                        bg=TEAL, color=BLANCO, border="none", border_radius="8px",
                        padding="0.75rem 1.5rem", cursor="pointer", _hover={"bg": "#0F5264"}),
                    width="100%", spacing="2",
                ),
                rx.vstack(
                    rx.foreach(CultivoState.cultivos, tarjeta_cultivo),
                    width="100%", spacing="4",
                ),
                rx.cond(CultivoState.cultivos.length() == 0,
                    rx.text("No tienes cultivos registrados. ¡Crea uno nuevo!", color=TEAL, padding="2rem")),
                formulario_cultivo(),
                modal_eliminar(),
                width="100%", max_width="800px", align_items="flex-start",
            ),
            width="100%", padding="1rem 2rem 2rem 2rem",
        ),
        width="100%", min_height="100vh", bg=GRIS_CLARO,
        on_mount=[CultivoState.cargar_parcelas, CultivoState.cargar_cultivos],
    )
