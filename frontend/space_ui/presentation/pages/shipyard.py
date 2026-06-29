import reflex as rx

from space_ui.components.cards.shipyard_card import ship_card
from space_ui.presentation.sidebar import sidebar

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
