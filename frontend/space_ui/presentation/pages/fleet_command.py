import reflex as rx

from space_ui.presentation.sidebar import sidebar


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
