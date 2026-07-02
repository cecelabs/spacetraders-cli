import reflex as rx

from space_ui.components.cards.contract_card import contract_card
from space_ui.presentation.sidebar import sidebar

contracts_data = [
    {
        "id": "#TRAD-447",
        "type": "PROCUREMENT",
        "status": "Active",
        "organitation": "Cosmic Syndicate",
        "order": "Deliver 20 units of refined Fuel to Andromeda Station to resupply long-haul freighters.",

        "fuel": "20x Fuel",
        "location": "X1-ANDROMEDA-7",
        "credits": "47,000 CR",
        "status_order": "Delivery Progress",
        "status_order_num": 50,
        "items": "10 / 20",

        "on_accept": "On Accept: +5,000 CR",
        "on_fulfill": "On Fulfill: +42,000 CR",
        "time_left": "16h 0m remaining"
    },
]


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

            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("ALL (5)", value="all"),
                    rx.tabs.trigger("AVAILABLE (2)", value="available"),
                    rx.tabs.trigger("ACTIVE (1)", value="active"),
                    rx.tabs.trigger("COMPLETED (1)", value="completed"),
                    rx.tabs.trigger("FAILED (1)", value="failed"),
                ),
                default_value="all",
            ),

            rx.flex(
                contract_card(contracts_data[0]),
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
