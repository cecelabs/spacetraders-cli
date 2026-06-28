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
                rx.link(
                    rx.button(
                        "Ir al Astillero (Shipyard) →",
                        size="3",
                        color_scheme="cyan",
                        variant="solid",
                        cursor="pointer",
                        _hover={"transform": "translateY(-2px)", "transition": "0.2s"},
                    ),
                    href="/shipyard",
                    margin_left="4px",
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


# --- NUEVO CÓDIGO DEL ASTILLERO (SHIPYARD) ---

ships_data = [
    {
        "symbol": "SHIP_PROBE",
        "type": "Reconnaissance",
        "class": "☆ Standard",
        "badge_color": "gray",
        "description": "Fast scout ship for charting new territories. Low cargo, high speed.",
        "speed": 60,
        "cargo": 15,
        "fuel": 300,
        "modules": 2,
        "locations": ["X1-ANDROMEDA-7", "KRONOS-IV"],
        "price": 25000,
    },
    {
        "symbol": "SHIP_MINING_DRONE",
        "type": "Excavation",
        "class": "☆ Standard",
        "badge_color": "gray",
        "description": "Specialized extraction vessel with heavy mining array.",
        "speed": 15,
        "cargo": 60,
        "fuel": 600,
        "modules": 3,
        "locations": ["X1-BB8"],
        "price": 38000,
    },
    {
        "symbol": "SHIP_LIGHT_HAULER",
        "type": "Transport",
        "class": "☆ Standard",
        "badge_color": "gray",
        "description": "Mid-range hauler balanced for medium-distance trade routes.",
        "speed": 22,
        "cargo": 160,
        "fuel": 700,
        "modules": 3,
        "locations": ["X1-ANDROMEDA-7", "OMICRON-VII"],
        "price": 54000,
    },
    {
        "symbol": "SHIP_HEAVY_FREIGHTER",
        "type": "Heavy Transport",
        "class": "★ Advanced",
        "badge_color": "blue",
        "description": "Heavy-duty freighter designed for large-scale cargo hauling.",
        "speed": 10,
        "cargo": 500,
        "fuel": 1200,
        "modules": 5,
        "locations": ["KRONOS-IV"],
        "price": 150000,
    },
    {
        "symbol": "SHIP_EXPLORER",
        "type": "Exploration",
        "class": "★ Advanced",
        "badge_color": "blue",
        "description": "Long-range explorer equipped with advanced sensors.",
        "speed": 45,
        "cargo": 50,
        "fuel": 800,
        "modules": 4,
        "locations": ["X1-ANDROMEDA-7"],
        "price": 95000,
    },
    {
        "symbol": "SHIP_COMMAND_FRIGATE",
        "type": "Command",
        "class": "◆ Elite",
        "badge_color": "purple",
        "description": "State-of-the-art command vessel with premium capabilities.",
        "speed": 30,
        "cargo": 200,
        "fuel": 1000,
        "modules": 6,
        "locations": ["OMICRON-VII"],
        "price": 250000,
    },
]


def sidebar_item(icon_tag: str, label: str, href: str, active: bool = False) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon_tag, size=18, color="#00d2ff" if active else "#64748b"),
            rx.text(
                label,
                color="#f8fafc" if active else "#94a3b8",
                font_size="0.9em",
                font_weight="semibold" if active else "normal",
            ),
            rx.spacer() if active else rx.box(),
            rx.icon("chevron-right", size=14, color="#00d2ff") if active else rx.box(),
            width="100%",
            padding="0.75em 1em",
            background_color="#0c1724" if active else "transparent",
            border_radius="md",
            border="1px solid #1e293b" if active else "1px solid transparent",
            align_items="center",
            spacing="3",
            _hover={"background_color": "#0d1b2a", "transition": "0.2s"},
        ),
        href=href,
        underline="none",
        width="100%",
    )


def sidebar(active_page: str = "shipyard") -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.icon("navigation", color="#00d2ff", size=24),
                padding="6px",
                background_color="#0d243a",
                border_radius="md",
            ),
            rx.vstack(
                rx.text("STELLAR NAV", color="#00d2ff", font_weight="bold", font_size="1.1em", letter_spacing="0.05em"),
                rx.text("Command v4.2", color="#64748b", font_size="0.75em", margin_top="-4px"),
                spacing="0",
                align_items="start",
            ),
            align_items="center",
            spacing="3",
            margin_bottom="1.5em",
        ),
        
        rx.vstack(
            rx.text("NAVIGATION", color="#475569", font_size="0.7em", font_weight="bold", letter_spacing="0.1em", margin_bottom="0.5em"),
            sidebar_item("layout-dashboard", "Dashboard", href="/", active=(active_page == "dashboard")),
            sidebar_item("rocket", "Fleet Command", href="/fleet", active=(active_page == "fleet")),
            sidebar_item("warehouse", "Shipyard", href="/shipyard", active=(active_page == "shipyard")),
            sidebar_item("file-text", "Contract Ledger", href="/contracts", active=(active_page == "contracts")),
            align_items="stretch",
            spacing="1",
            width="100%",
        ),
        
        rx.spacer(),
        
        rx.vstack(
            rx.hstack(
                rx.box(
                    background_color="#10b981",
                    width="8px",
                    height="8px",
                    border_radius="50%",
                    box_shadow="0 0 8px #10b981",
                ),
                rx.text("CONNECTED", color="#94a3b8", font_size="0.75em", font_weight="bold", letter_spacing="0.05em"),
                align_items="center",
                spacing="2",
                margin_bottom="0.5em",
            ),
            rx.vstack(
                rx.text("Credits Available", color="#64748b", font_size="0.75em"),
                rx.text("1,240,500 CR", color="#10b981", font_weight="bold", font_size="1.15em"),
                background_color="#0c1724",
                border="1px solid #1e293b",
                border_radius="lg",
                padding="1em",
                width="100%",
                align_items="start",
                spacing="1",
            ),
            align_items="start",
            width="100%",
        ),
        
        width="260px",
        background_color="#080c15",
        border_right="1px solid #1e293b",
        padding="1.5em",
        height="100vh",
        position="sticky",
        top="0",
        spacing="6",
        align_items="stretch",
    )

def grid_element(icon_text:str, texto:str )-> rx.Component:

    return rx.hstack(
                    rx.icon(icon_text, color="#00d2ff", size=14),
                    rx.text(texto, color="#f8fafc", font_size="0.8em"),
                    align_items="center",
                    spacing="2",
                )

def ship_card(ship: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon("rocket", color="#00d2ff", size=18),
                    padding="8px",
                    background_color="#0d243a",
                    border_radius="md",
                ),
                rx.vstack(
                    rx.text(ship["symbol"], color="#f8fafc", font_weight="bold", font_size="0.95em"),
                    rx.text(ship["type"], color="#64748b", font_size="0.75em", margin_top="-4px"),
                    spacing="0",
                    align_items="start",
                ),
                rx.spacer(),
                rx.badge(
                    ship["class"],
                    variant="outline",
                    color_scheme=ship["badge_color"],
                    font_size="0.7em",
                    border_radius="md",
                ),
                align_items="center",
                width="100%",
            ),
            
            rx.text(
                ship["description"],
                color="#94a3b8",
                font_size="0.8em",
                line_height="1.4",
                min_height="40px",
            ),
            
            rx.grid(
                grid_element(icon_text="zap", texto=f"Speed {ship['speed']}"),
                grid_element(icon_text="package",texto=f"Cargo {ship['cargo']}"),
                grid_element(icon_text="circle", texto=f"Fuel {ship['fuel']}"),
                grid_element(icon_text="cpu", texto=f"Modules {ship['modules']}"),
                columns="2",
                spacing="3",
                width="100%",
                border_top="1px solid #1e293b",
                border_bottom="1px solid #1e293b",
                padding_y="3",
            ),
            
            rx.vstack(
                rx.text("Available at:", color="#64748b", font_size="0.75em", font_weight="medium"),
                rx.hstack(
                    *[
                        rx.badge(
                            loc,
                            variant="outline",
                            color_scheme="cyan",
                            font_size="0.75em",
                            padding="2px 6px",
                            border_radius="md",
                        )
                        for loc in ship["locations"]
                    ],
                    spacing="2",
                ),
                align_items="start",
                spacing="1",
                width="100%",
            ),
            
            rx.hstack(
                rx.text(f"{ship['price']:,} CR", color="#10b981", font_weight="bold", font_size="1.05em"),
                rx.spacer(),
                rx.button(
                    rx.hstack(
                        rx.text("Purchase", font_size="0.8em", font_weight="bold"),
                        rx.icon("chevron-right", size=14),
                        align_items="center",
                        spacing="1",
                    ),
                    variant="outline",
                    color_scheme="blue",
                    size="2",
                    cursor="pointer",
                    _hover={"background_color": "#0d243a"},
                ),
                align_items="center",
                width="100%",
                padding_top="2",
            ),
            
            spacing="4",
            align_items="start",
        ),
        background_color="#0c1524",
        border="1px solid #1e293b",
        padding="1.25em",
        border_radius="lg",
        width="100%",
    )


def shipyard_view() -> rx.Component:
    return rx.flex(
        sidebar(),
        
        rx.box(
            rx.hstack(
                rx.hstack(
                    rx.icon("warehouse", color="#00d2ff", size=20),
                    rx.text("Shipyard", color="#94a3b8", font_size="0.95em", font_weight="medium"),
                    align_items="center",
                    spacing="2",
                ),
                rx.spacer(),
                rx.hstack(
                    rx.text("SECTOR:", color="#64748b", font_size="0.8em"),
                    rx.text("X1-ANDROMEDA", color="#00d2ff", font_size="0.8em", font_weight="bold"),
                    rx.box(
                        background_color="#3b82f6",
                        width="6px",
                        height="6px",
                        border_radius="50%",
                    ),
                    rx.text("3066.187", color="#94a3b8", font_size="0.8em"),
                    align_items="center",
                    spacing="2",
                ),
                width="100%",
                border_bottom="1px solid #1e293b",
                padding_bottom="1em",
                margin_bottom="1.5em",
            ),
            
            rx.vstack(
                rx.text("MODULE: SHIPYARD & MARKET", color="#00d2ff", font_size="0.75em", letter_spacing="0.1em", font_weight="bold"),
                rx.heading("Astillero & Mercado", size="7", color="#f8fafc", font_weight="bold", margin_top="0.25em"),
                rx.text("Browse available vessels and trading waypoints across the galaxy.", color="#64748b", font_size="0.95em"),
                align_items="start",
                spacing="1",
                margin_bottom="2em",
            ),
            
            rx.hstack(
                rx.button(
                    "SHIP CATALOG",
                    background_color="#0c1724",
                    border="1px solid #00d2ff",
                    color="#00d2ff",
                    border_radius="full",
                    font_size="0.8em",
                    font_weight="bold",
                    padding="0.5em 1.25em",
                    cursor="pointer",
                ),
                rx.button(
                    "WAYPOINTS",
                    background_color="transparent",
                    border="1px solid transparent",
                    color="#64748b",
                    font_size="0.8em",
                    font_weight="bold",
                    padding="0.5em 1.25em",
                    cursor="pointer",
                    _hover={"color": "#94a3b8"},
                ),
                spacing="3",
                margin_bottom="2em",
            ),
            
            rx.grid(
                *[ship_card(ship) for ship in ships_data],
                columns=rx.breakpoints(initial="1", sm="2", md="3"),
                spacing="5",
                width="100%",
            ),
            
            flex="1",
            padding="2em 3em",
            background_color="#030712",
            overflow_y="auto",
            height="100vh",
        ),
        
        width="100%",
        min_height="100vh",
        background_color="#030712",
        direction="row",
    )



def dashboard_view() -> rx.Component:
    return rx.flex(
        sidebar("dashboard"),
        
        rx.box(
            rx.hstack(
                rx.hstack(
                    rx.icon("layout-dashboard"),
                    rx.text("Dashboard"),
                ),
                rx.spacer(),
                rx.hstack(
                    rx.text("SECTOR:"),
                    rx.text("X1-ANDROMEDA"),
                    rx.text("3066.187"),
                ),
                width="100%",
            ),
            
            rx.vstack(
                rx.text("STELLAR DATE: 3066.187"),
                rx.heading("Command Overview"),
                rx.text("Empire status — Faction: Cosmic Syndicate · HQ: X1-ANDROMEDA-7"),
                align_items="start",
            ),
            
            rx.grid(
                rx.box(
                    rx.text("TOTAL CREDITS"),
                    rx.text("1,240,500 CR"),
                    rx.text("+14.2"),
                ),
                rx.box(
                    rx.text("ACTIVE SHIPS"),
                    rx.text("5 vessels"),
                ),
                rx.box(
                    rx.text("PENDING CONTRACTS"),
                    rx.text("3 missions"),
                    rx.text("-1"),
                ),
                rx.box(
                    rx.text("SYSTEMS CHARTED"),
                    rx.text("12 sectors"),
                    rx.text("+2"),
                ),
                columns="4",
                spacing="4",
                width="100%",
            ),
            
            rx.grid(
                rx.box(
                    rx.text("CREDIT FLOW – 24H"),
                    rx.text("+14.2%"),
                    rx.box(
                        rx.text("[Chart Placeholder: Credit Flow 24h Line Chart]"),
                        height="200px",
                    ),
                ),
                rx.box(
                    rx.text("AGENT PROFILE"),
                    rx.box(rx.text("CS")),  # Avatar box
                    rx.text("COMMANDER_7"),
                    rx.text("Cosmic Syndicate · Rank 4"),
                    rx.vstack(
                        rx.text("Ship Tokens: 5 / 10"),
                        rx.text("Starting Credits: 100,000 CR"),
                        rx.text("HQ Waypoint: X1-ANDROMEDA-7"),
                        align_items="start",
                    ),
                    rx.hstack(
                        rx.text("ONLINE · All systems nominal"),
                    ),
                ),
                columns="2",
                spacing="4",
                width="100%",
            ),
            
            flex="1",
            padding="2em 3em",
            overflow_y="auto",
            height="100vh",
        ),
        
        width="100%",
        min_height="100vh",
        direction="row",
    )


def fleet_view() -> rx.Component:
    return rx.flex(
        sidebar("fleet"),
        
        rx.box(
            rx.hstack(
                rx.hstack(
                    rx.icon("rocket"),
                    rx.text("Fleet Command"),
                ),
                rx.spacer(),
                rx.hstack(
                    rx.text("SECTOR:"),
                    rx.text("X1-ANDROMEDA"),
                    rx.text("3066.187"),
                ),
                width="100%",
            ),
            
            rx.vstack(
                rx.text("MODULE: FLEET COMMAND"),
                rx.heading("Fleet Management"),
                rx.text("5 vessels registered · 2 in transit"),
                align_items="start",
            ),
            
            rx.hstack(
                rx.button("ALL (5)"),
                rx.button("DOCKED"),
                rx.button("ORBITING"),
                rx.button("IN TRANSIT"),
            ),
            
            rx.vstack(
                rx.box(
                    rx.hstack(
                        rx.icon("rocket"),
                        rx.vstack(
                            rx.text("HORIZON-X1"),
                            rx.text("COMMAND • X1-ANDROMEDA-7"),
                        ),
                        rx.spacer(),
                        rx.text("Docked"),
                    ),
                    rx.vstack(
                        rx.text("Fuel"),
                        rx.progress(value=100),
                        rx.text("1200/1200"),
                        align_items="start",
                    ),
                    rx.vstack(
                        rx.text("Cargo"),
                        rx.progress(value=56),
                        rx.text("45/80"),
                        align_items="start",
                    ),
                    rx.hstack(
                        rx.button("Dock/Orbit"),
                        rx.button("Refuel"),
                        rx.button("Extract"),
                    ),
                ),
                
                rx.box(
                    rx.hstack(
                        rx.icon("rocket"),
                        rx.vstack(
                            rx.text("VEGA-II"),
                            rx.text("HAULER • KRONOS-IV"),
                        ),
                        rx.spacer(),
                        rx.text("In Transit"),
                    ),
                    rx.text("→ OMICRON-VII"),
                    rx.vstack(
                        rx.text("Fuel"),
                        rx.progress(value=67),
                        rx.text("540/800"),
                        align_items="start",
                    ),
                    rx.vstack(
                        rx.text("Cargo"),
                        rx.progress(value=83),
                        rx.text("200/240"),
                        align_items="start",
                    ),
                    rx.hstack(
                        rx.button("Dock/Orbit"),
                        rx.button("Refuel"),
                        rx.button("Extract"),
                    ),
                ),
                width="100%",
                spacing="4",
            ),
            
            flex="1",
            padding="2em 3em",
            overflow_y="auto",
            height="100vh",
        ),
        
        width="100%",
        min_height="100vh",
        direction="row",
    )


def contracts_view() -> rx.Component:
    return rx.flex(
        sidebar("contracts"),
        
        rx.box(
            rx.hstack(
                rx.hstack(
                    rx.icon("file-text"),
                    rx.text("Contract Ledger"),
                ),
                rx.spacer(),
                rx.hstack(
                    rx.text("SECTOR:"),
                    rx.text("X1-ANDROMEDA"),
                    rx.text("3066.187"),
                ),
                width="100%",
            ),
            
            rx.vstack(
                rx.text("MODULE: CONTRACT LEDGER"),
                rx.heading("Mission Contracts"),
                rx.text("1 active · 2 available · 1 completed"),
                align_items="start",
            ),
            
            rx.grid(
                rx.box(
                    rx.text("342,000 CR"),
                    rx.text("Total Earned"),
                ),
                rx.box(
                    rx.text("47,000 CR"),
                    rx.text("Active Value"),
                ),
                rx.box(
                    rx.text("71%"),
                    rx.text("Completion Rate"),
                ),
                columns="3",
                spacing="4",
                width="100%",
            ),
            
            rx.hstack(
                rx.button("ALL (5)"),
                rx.button("AVAILABLE (2)"),
                rx.button("ACTIVE (1)"),
                rx.button("COMPLETED (1)"),
                rx.button("FAILED (1)"),
            ),
            
            rx.box(
                rx.hstack(
                    rx.text("#TRAD-447"),
                    rx.text("PROCUREMENT"),
                    rx.spacer(),
                    rx.text("Active"),
                ),
                rx.text("Cosmic Syndicate"),
                rx.text("Deliver 20 units of refined Fuel to Andromeda Station to resupply long-haul freighters."),
                rx.hstack(
                    rx.text("20x Fuel"),
                    rx.text("X1-ANDROMEDA-7"),
                    rx.text("47,000 CR"),
                ),
                rx.vstack(
                    rx.text("Delivery Progress"),
                    rx.progress(value=50),
                    rx.text("10 / 20"),
                    align_items="start",
                ),
                rx.hstack(
                    rx.text("On Accept: +5,000 CR"),
                    rx.text("On Fulfill: +42,000 CR"),
                    rx.text("16h 0m remaining"),
                    rx.spacer(),
                    rx.button("Deliver"),
                ),
            ),
            
            flex="1",
            padding="2em 3em",
            overflow_y="auto",
            height="100vh",
        ),
        
        width="100%",
        min_height="100vh",
        direction="row",
    )


app = rx.App()
app.add_page(dashboard_view, route="/")
app.add_page(fleet_view, route="/fleet")
app.add_page(shipyard_view, route="/shipyard")
app.add_page(contracts_view, route="/contracts")
app.add_page(index, route="/demo")
app.add_page(cards_view, route="/cards")

