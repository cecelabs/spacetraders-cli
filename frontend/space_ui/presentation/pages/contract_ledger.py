import reflex as rx

from space_ui.presentation.sidebar import sidebar


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
