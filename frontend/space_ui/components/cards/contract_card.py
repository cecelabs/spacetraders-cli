import reflex as rx

def contract_card(contract_data:dict) -> rx.Component:
    return  rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.text("#TRAD-447"),
                        rx.text("PROCUREMENT"),
                        rx.spacer(),
                        rx.text("Active"),
                        width="100%"
                    ),

                    rx.divider(),

                    rx.text("Cosmic Syndicate"),
                    rx.text(
                        "Deliver 20 units of refined Fuel to Andromeda Station to resupply long-haul freighters."
                    ),

                    rx.hstack(
                        rx.text("20x Fuel"),
                        rx.text("X1-ANDROMEDA-7"),
                        rx.text("47,000 CR"),
                    ),

                    rx.vstack(
                        rx.text("Delivery Progress"),
                        rx.progress(value=50),
                        rx.text("10 / 20"),
                        width="100%"
                    ),

                    rx.hstack(
                        rx.text("On Accept: +5,000 CR"),
                        rx.text("On Fulfill: +42,000 CR"),
                        rx.text("16h 0m remaining"),
                        rx.spacer(),
                        rx.button("Deliver"),
                        width="100%"
                    ),
                ),
                margin="1em",
            )