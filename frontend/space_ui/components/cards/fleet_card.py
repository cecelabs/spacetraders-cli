import reflex as rx


def fleet_card(fleet_data: dict) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.icon(fleet_data["icon"]),
            rx.vstack(
                rx.text(fleet_data["name"]),
                rx.text(fleet_data["location"]),
            ),
            rx.spacer(),
            rx.text(fleet_data["status"]),
        ),
        rx.vstack(
            rx.text("Fuel"),
            rx.progress(value=fleet_data["fuel_value"]),
            rx.text(fleet_data["fuel_text"]),
            align_items="start",
        ),
        rx.vstack(
            rx.text("Cargo"),
            rx.progress(value=fleet_data["cargo_value"]),
            rx.text(fleet_data["cargo_text"]),
            align_items="start",
        ),
        rx.hstack(
            rx.button("Dock/Orbit"),
            rx.button("Refuel"),
            rx.button("Extract"),
        ),
    )
