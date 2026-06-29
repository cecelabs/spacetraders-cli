import reflex as rx

from space_ui.components.cards.fleet_card import fleet_card
from space_ui.presentation.sidebar import sidebar

fleets_data = [
{
    "icon": "rocket",
    "name": "HORIZON-X1",
    "location": "COMMAND • X1-ANDROMEDA-7",
    "status": "Docked",
    "fuel_value": 100,
    "fuel_text": "1200/1200",
    "cargo_value": 56,
    "cargo_text": "45/80",
},
{
    "icon": "rocket",
    "name": "VEGA-II",
    "location": "HAULER • KRONOS-IV",
    "status": "In Transit",
    "fuel_value": 67,
    "fuel_text": "540/800",
    "cargo_value": 83,
    "cargo_text": "200/240",
}
]

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
                fleet_card(fleets_data[0]),
                fleet_card(fleets_data[1]),
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
