import reflex as rx


def stat_card(
    label: str,
    value: str,
    change: str | None = None,
    color_scheme: str = "green",
) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.text(label),
                rx.cond(
                    change,
                    rx.badge(
                        change,
                        color_scheme=color_scheme,
                    ),
                ),
                justify="between",
                width="100%",
            ),
            rx.heading(value),
            align="start",
            spacing="2",
        ),
        width="100%",
    )