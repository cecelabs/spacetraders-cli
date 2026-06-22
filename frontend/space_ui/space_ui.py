import reflex as rx
from space_ui.components.card import system_card
from src.traders.domain.entities.system import System
from rxconfig import config


class CourseState(rx.State):
    clics_demo: int = 0
    
    def incrementar(self):
        self.clics_demo += 1
        
    def reiniciar(self):
        self.clics_demo = 0


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        
        rx.vstack(
            rx.vstack(
                rx.heading("Reflex: Ejemplos ", size="9", weight="bold"),
                rx.text(
                    "Demostración interactiva de layouts, estados y componentes aprendidos.",
                    size="4",
                    color_scheme="gray",
                ),
                align_items="center",
                spacing="2",
                width="100%",
                padding_top="6",
            ),
            
            rx.hstack(
                rx.link(
                    rx.button(
                        "Explorar Lista de Sistemas →",
                        size="3",
                        color_scheme="violet",
                        variant="solid",
                        cursor="pointer",
                        _hover={"transform": "translateY(-2px)", "transition": "0.2s"},
                    ),
                    href="/cards",
                ),
                justify="center",
                width="100%",
                padding="4",
            ),
            
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Layouts y Contenedores", value="layouts"),
                    rx.tabs.trigger("Componentes y Reactividad", value="interactive"),
                    rx.tabs.trigger("Screaming Architecture", value="architecture"),
                    width="100%",
                    justify="center",
                ),
                
                rx.tabs.content(
                    rx.card(
                        rx.vstack(
                            rx.heading("Estructuración con Box, HStack y VStack", size="4"),
                            rx.text("Reflex permite apilar elementos vertical u horizontalmente sin escribir CSS manual."),
                            rx.hstack(
                                rx.box(rx.text("Caja A"), padding="4", bg="var(--violet-3)", border_radius="md", width="100px", text_align="center"),
                                rx.box(rx.text("Caja B"), padding="4", bg="var(--blue-3)", border_radius="md", width="100px", text_align="center"),
                                rx.box(rx.text("Caja C"), padding="4", bg="var(--green-3)", border_radius="md", width="100px", text_align="center"),
                                spacing="4",
                                justify="center",
                                width="100%",
                            ),
                            spacing="3",
                        ),
                        padding="5",
                    ),
                    value="layouts",
                ),
                
                rx.tabs.content(
                    rx.card(
                        rx.vstack(
                            rx.heading("Interactividad y Estado Reactivo", size="4"),
                            rx.text(
                                "Al hacer clic en los botones, el backend en Python modifica el valor del State y la UI se actualiza inmediatamente.",
                                size="2",
                            ),
                            rx.hstack(
                                rx.button("Incrementar Clics", on_click=CourseState.incrementar, color_scheme="blue"),
                                rx.button("Reiniciar", on_click=CourseState.reiniciar, color_scheme="gray", variant="outline"),
                                spacing="3",
                            ),
                            rx.badge(
                                f"Total clics: {CourseState.clics_demo}",
                                size="3",
                                color_scheme="green",
                                variant="soft",
                            ),
                            spacing="3",
                            align_items="center",
                        ),
                        padding="5",
                    ),
                    value="interactive",
                ),
                
                rx.tabs.content(
                    rx.card(
                        rx.vstack(
                            rx.heading("Organización por Características", size="4"),
                            rx.text(
                                "El proyecto está estructurado para que el nombre de las carpetas grite su propósito de negocio (ej: features/systems_explorer).",
                                size="2",
                            ),
                            rx.code_block(
                                """
frontend/
└── space_ui/
    ├── components/
    │   └── card.py          # Componentes transversales
    ├── features/            # Dominios de negocio
    │   └── systems_explorer/
    │       ├── components/
    │       ├── state.py
    │       └── page.py
    └── space_ui.py          # Punto de entrada y rutas
                                """.strip(),
                                language="bash",
                            ),
                            spacing="3",
                        ),
                        padding="5",
                    ),
                    value="architecture",
                ),
                
                default_value="layouts",
                width="100%",
            ),
            
            spacing="6",
            align_items="stretch",
            min_height="80vh",
            padding_bottom="10",
        ),
    )


def cards_view() -> rx.Component:
    sistemas = [
        System(symbol="X1-DF44", sector_symbol="X1", type="NEUTRON_STAR", x=10, y=-20, constellation="Andromeda"),
        System(symbol="SOL-01", sector_symbol="SOL", type="YELLOW_DWARF", x=0, y=0, constellation="Orion"),
        System(symbol="KEPLER-186", sector_symbol="K1", type="RED_DWARF", x=150, y=340, constellation="Cygnus"),
        System(symbol="SIRIUS-A", sector_symbol="SIR", type="WHITE_DWARF", x=-45, y=89, constellation="Canis Major"),
        System(symbol="VEGA-09", sector_symbol="VEG", type="BLUE_GIANT", x=92, y=-115, constellation="Lyra"),
        System(symbol="PROXIMA-C", sector_symbol="PRX", type="RED_DWARF", x=4, y=4, constellation="Centaurus"),
    ]
    
    return rx.container(
        rx.color_mode.button(position="top-right"),
        
        rx.vstack(
            rx.hstack(
                rx.link(
                    rx.button("← Volver a Ejemplos", variant="outline", size="2", cursor="pointer"),
                    href="/",
                ),
                width="100%",
                padding_top="6",
            ),
            
            rx.vstack(
                rx.heading("Lista de Sistemas Espaciales", size="8", weight="bold"),
                rx.text(
                    "Vista de 6 sistemas por ahora",
                    size="3",
                    color_scheme="gray",
                ),
                align_items="start",
                spacing="1",
                width="100%",
            ),
            
            rx.grid(
                *[system_card(sys) for sys in sistemas],
                columns=rx.breakpoints(initial="1", sm="2", md="3"),
                spacing="5",
                width="100%",
                padding_y="4",
            ),
            
            spacing="5",
            align_items="stretch",
            min_height="80vh",
            padding_bottom="10",
        ),
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(cards_view, route="/cards")

