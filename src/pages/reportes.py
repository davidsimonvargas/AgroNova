import reflex as rx

from src.states.reportes import ReportesState

AZUL_OSCURO = "#14283C"
VERDE = "#4CB43C"
TEAL = "#146478"
BLANCO = "#FFFFFF"
GRIS_CLARO = "#F5F7FA"


def btn_tab(vista: str, label: str):
    activa = ReportesState.vista_activa == vista
    return rx.button(
        label,
        on_click=lambda: ReportesState.set_vista(vista),
        bg=rx.cond(activa, VERDE, "transparent"),
        color=rx.cond(activa, BLANCO, TEAL),
        border="1px solid #E2E8F0",
        border_radius="8px",
        padding="0.6rem 1.2rem",
        font_weight="600",
        font_size="0.9rem",
        cursor="pointer",
        _hover={"bg": rx.cond(activa, "#3D9B30", VERDE), "color": BLANCO},
    )


def tabs():
    return rx.hstack(
        btn_tab("produccion", "Producción"),
        btn_tab("costos", "Costos"),
        btn_tab("rendimiento", "Rendimiento"),
        btn_tab("estadisticas", "Estadísticas"),
        spacing="3",
        width="100%",
        flex_wrap="wrap",
    )


def kpi(titulo: str, valor, color=TEAL):
    return rx.box(
        rx.vstack(
            rx.text(titulo, font_size="0.8rem", color=TEAL, font_weight="500"),
            rx.text(valor, font_size="1.5rem", font_weight="700", color=color),
            align_items="flex-start",
            width="100%",
        ),
        bg=BLANCO,
        padding="1.2rem",
        border_radius="10px",
        box_shadow="0 1px 3px rgba(0,0,0,0.1)",
        width="100%",
    )


def seccion_produccion():
    return rx.vstack(
        rx.heading("Reporte de Producción", font_size="1.3rem", color=AZUL_OSCURO),
        rx.hstack(
            kpi("Total Cosechado", ReportesState.total_cosechado, VERDE),
            kpi("Cultivos en Producción", ReportesState.cultivos_produccion, TEAL),
            spacing="4",
            width="100%",
        ),
        rx.text("Producción por Cultivo", font_weight="600", color=AZUL_OSCURO, font_size="1rem"),
        rx.vstack(
            rx.foreach(
                ReportesState.prod_por_cultivo,
                lambda item: rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.text(item["nombre"], font_weight="500", color=AZUL_OSCURO, font_size="0.9rem"),
                            rx.hstack(
                                rx.text(item["cantidad"], font_size="0.8rem", color=TEAL),
                                rx.text(" unidades (", font_size="0.8rem", color=TEAL),
                                rx.text(item["porcentaje"], font_size="0.8rem", color=TEAL),
                                rx.text(")", font_size="0.8rem", color=TEAL),
                                spacing="0",
                            ),
                            spacing="1",
                            width="100%",
                        ),
                        rx.box(
                            rx.box(
                                height="8px", width=item["barra"],
                                bg=VERDE, border_radius="4px",
                            ),
                            width="100%", bg="#E2E8F0", border_radius="4px",
                        ),
                        width="100%", spacing="3",
                    ),
                    padding="0.8rem 0",
                    width="100%",
                ),
            ),
            width="100%", spacing="1",
        ),
        rx.text("Producción por Parcela", font_weight="600", color=AZUL_OSCURO, font_size="1rem"),
        rx.vstack(
            rx.foreach(
                ReportesState.prod_por_parcela,
                lambda item: rx.box(
                    rx.hstack(
                        rx.text(item["nombre"], font_weight="500", color=AZUL_OSCURO, width="50%"),
                        rx.text(item["cantidad"], color=TEAL, width="50%"),
                        width="100%",
                    ),
                    padding="0.6rem 0",
                    border_bottom="1px solid #E2E8F0",
                    width="100%",
                ),
            ),
            width="100%",
        ),
        rx.cond(
            ReportesState.prod_por_cultivo.length() == 0,
            rx.text("No hay datos de producción registrados. Registra cosechas en Actividades.", color=TEAL, padding="1rem"),
        ),
        width="100%", spacing="4",
    )


def seccion_costos():
    return rx.vstack(
        rx.heading("Reporte de Costos", font_size="1.3rem", color=AZUL_OSCURO),
        rx.hstack(
            kpi("Total Gastos", ReportesState.total_gastos, "red.500"),
            kpi("Total Ingresos", ReportesState.total_ingresos, VERDE),
            kpi("Rentabilidad", ReportesState.rentabilidad,
                rx.cond(ReportesState.rentabilidad_positiva, VERDE, "red.500")),
            spacing="4",
            width="100%",
        ),
        rx.hstack(
            rx.vstack(
                rx.text("Gastos por Parcela", font_weight="600", color=AZUL_OSCURO),
                rx.vstack(
                    rx.foreach(
                        ReportesState.gastos_por_parcela,
                        lambda item: rx.box(
                            rx.hstack(
                                rx.text(item["nombre"], font_weight="500", width="60%"),
                                rx.text(item["monto"], color="red.500", width="40%"),
                                width="100%",
                            ),
                            padding="0.5rem 0", border_bottom="1px solid #E2E8F0", width="100%",
                        ),
                    ),
                    width="100%",
                ),
                width="100%",
            ),
            rx.vstack(
                rx.text("Ingresos por Parcela", font_weight="600", color=AZUL_OSCURO),
                rx.vstack(
                    rx.foreach(
                        ReportesState.ingresos_por_parcela,
                        lambda item: rx.box(
                            rx.hstack(
                                rx.text(item["nombre"], font_weight="500", width="60%"),
                                rx.text(item["monto"], color=VERDE, width="40%"),
                                width="100%",
                            ),
                            padding="0.5rem 0", border_bottom="1px solid #E2E8F0", width="100%",
                        ),
                    ),
                    width="100%",
                ),
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        width="100%", spacing="4",
    )


def seccion_rendimiento():
    return rx.vstack(
        rx.heading("Rendimiento por Parcela", font_size="1.3rem", color=AZUL_OSCURO),
        rx.vstack(
            rx.foreach(
                ReportesState.rendimiento_parcelas,
                lambda item: rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text(item["nombre"], font_weight="600", color=AZUL_OSCURO),
                            rx.text(item["rendimiento_ha"], color=VERDE, font_weight="700"),
                            width="100%", justify="between",
                        ),
                        rx.hstack(
                            rx.text("Área: ", item["area"], font_size="0.85rem", color=TEAL),
                            rx.text("Cosechado: ", item["total_cosechado"], font_size="0.85rem", color=TEAL),
                            rx.text("Cultivos activos: ", item["cultivos_activos"], font_size="0.85rem", color=TEAL),
                            spacing="4",
                        ),
                        width="100%",
                    ),
                    bg=BLANCO,
                    padding="1rem 1.5rem",
                    border_radius="10px",
                    box_shadow="0 1px 3px rgba(0,0,0,0.1)",
                    width="100%",
                ),
            ),
            width="100%", spacing="3",
        ),
        rx.cond(
            ReportesState.rendimiento_parcelas.length() == 0,
            rx.text("No hay datos de rendimiento disponibles.", color=TEAL, padding="1rem"),
        ),
        width="100%", spacing="4",
    )


def seccion_estadisticas():
    return rx.vstack(
        rx.heading("Estadísticas Agrícolas", font_size="1.3rem", color=AZUL_OSCURO),
        rx.grid(
            kpi("Total Parcelas", ReportesState.total_parcelas, AZUL_OSCURO),
            kpi("Área Total (ha)", ReportesState.total_area, TEAL),
            kpi("Total Cultivos", ReportesState.total_cultivos, VERDE),
            kpi("Cultivos Activos", ReportesState.cultivos_activos, "#3182CE"),
            kpi("Actividades Registradas", ReportesState.total_actividades, "#D69E2E"),
            columns="3",
            spacing="4",
            width="100%",
        ),
        width="100%", spacing="4",
    )


@rx.page(route="/reportes", title="Reportes - AgroNova")
def reportes_page() -> rx.Component:
    return rx.box(
        rx.link("← Volver al Dashboard", href="/dashboard", color=TEAL, font_size="0.9rem", padding="1rem", _hover={"color": VERDE}),
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.heading("Reportes", font_size="1.5rem", color=AZUL_OSCURO),
                    width="100%", justify="between",
                ),
                tabs(),
                rx.cond(
                    ReportesState.cargando,
                    rx.center(rx.text("Cargando...", color=TEAL), padding="2rem", width="100%"),
                    rx.box(
                        rx.cond(ReportesState.vista_activa == "produccion", seccion_produccion()),
                        rx.cond(ReportesState.vista_activa == "costos", seccion_costos()),
                        rx.cond(ReportesState.vista_activa == "rendimiento", seccion_rendimiento()),
                        rx.cond(ReportesState.vista_activa == "estadisticas", seccion_estadisticas()),
                        width="100%",
                    ),
                ),
                width="100%", max_width="900px", align_items="flex-start",
            ),
            width="100%", padding="1rem 2rem 2rem 2rem",
        ),
        width="100%", min_height="100vh", bg=GRIS_CLARO,
        on_mount=ReportesState.cargar_reporte_produccion,
    )
