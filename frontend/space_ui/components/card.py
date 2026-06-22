import reflex as rx
from src.traders.domain.entities.system import System


def system_card(system: System) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(system.symbol, size="4"),
            rx.badge(system.type, color_scheme="blue", variant="surface"),
            rx.text(f"Sector: {system.sector_symbol}", size="2"),
            rx.hstack(
                rx.text(f"X: {system.x}", size="1", color_scheme="gray"),
                rx.text(f"Y: {system.y}", size="1", color_scheme="gray"),
                spacing="2",
            ),
            rx.text(f"Constellation: {system.constellation}", size="1"),
            spacing="2",
            align_items="start",
        ),
        width="250px",
    )
