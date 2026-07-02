import reflex as rx

from space_ui.components.cards.stat_card import stat_card
from space_ui.presentation.sidebar import sidebar

data = [
    {"name": "00h", "uv": 120},
    {"name": "04h", "uv": 180},
    {"name": "08h", "uv": 150},
    {"name": "12h", "uv": 220},
    {"name": "16h", "uv": 190},
    {"name": "20h", "uv": 260},
    {"name": "24h", "uv": 240},
]

def area_simple():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        width="100%",
        height=200,
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
                stat_card("Total Credits", "1,240,500 CR", "+14.2%", "green"),
                stat_card("Active Ships", "5 vessels", None),
                stat_card("Pending Contracts", "3 missions", "-1", "red"),
                stat_card("Systems Charted", "12 sectors", "+2", "blue"),
                columns="4",
                spacing="4",
                width="100%",

            ),

            rx.grid(
                rx.box(
                    rx.text("CREDIT FLOW – 24H"),
                    rx.text("+14.2%"),
                    area_simple(),
                    padding="1.2em",
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
