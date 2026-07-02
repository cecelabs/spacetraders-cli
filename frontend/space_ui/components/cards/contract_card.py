import reflex as rx

from space_ui.domain.entities.contract import Contract


def contract_card(contract_data: Contract) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.text(contract_data.id),
                rx.text(contract_data.type),
                rx.spacer(),
                rx.text(contract_data.status),
                width="100%"
            ),

            rx.divider(),

            rx.text(contract_data.faction_symbol),
            rx.text(contract_data.order),

            rx.hstack(
                rx.text(contract_data.fuel),
                rx.text(contract_data.location),
                rx.text(contract_data.credits),
            ),

            rx.vstack(
                rx.text(contract_data.status_order),
                rx.progress(value=contract_data.status_order_num),
                rx.text(contract_data.items),
                width="100%"
            ),

            rx.hstack(
                rx.text(contract_data.on_accept),
                rx.text(contract_data.on_fulfill),
                rx.text(contract_data.expiration),
                rx.spacer(),
                rx.button("Deliver"),
                width="100%"
            ),
        ),
        margin="1em",
    )
