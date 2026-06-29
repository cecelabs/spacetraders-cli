import reflex as rx

from space_ui.presentation.sidebar import sidebar


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
