import reflex as rx



def grid_element(icon_text:str, texto:str )-> rx.Component:

    return rx.hstack(
                    rx.icon(icon_text, color="#00d2ff", size=14),
                    rx.text(texto, color="#f8fafc", font_size="0.8em"),
                    align_items="center",
                    spacing="2",
                )

def ship_card(ship: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon("rocket", color="#00d2ff", size=18),
                    padding="8px",
                    background_color="#0d243a",
                    border_radius="md",
                ),
                rx.vstack(
                    rx.text(ship["symbol"], color="#f8fafc", font_weight="bold", font_size="0.95em"),
                    rx.text(ship["type"], color="#64748b", font_size="0.75em", margin_top="-4px"),
                    spacing="0",
                    align_items="start",
                ),
                rx.spacer(),
                rx.badge(
                    ship["class"],
                    variant="outline",
                    color_scheme=ship["badge_color"],
                    font_size="0.7em",
                    border_radius="md",
                ),
                align_items="center",
                width="100%",
            ),

            rx.text(
                ship["description"],
                color="#94a3b8",
                font_size="0.8em",
                line_height="1.4",
                min_height="40px",
            ),

            rx.grid(
                grid_element(icon_text="zap", texto=f"Speed {ship['speed']}"),
                grid_element(icon_text="package" ,texto=f"Cargo {ship['cargo']}"),
                grid_element(icon_text="circle", texto=f"Fuel {ship['fuel']}"),
                grid_element(icon_text="cpu", texto=f"Modules {ship['modules']}"),
                columns="2",
                spacing="3",
                width="100%",
                border_top="1px solid #1e293b",
                border_bottom="1px solid #1e293b",
                padding_y="3",
            ),

            rx.vstack(
                rx.text("Available at:", color="#64748b", font_size="0.75em", font_weight="medium"),
                rx.hstack(
                    *[
                        rx.badge(
                            loc,
                            variant="outline",
                            color_scheme="cyan",
                            font_size="0.75em",
                            padding="2px 6px",
                            border_radius="md",
                        )
                        for loc in ship["locations"]
                    ],
                    spacing="2",
                ),
                align_items="start",
                spacing="1",
                width="100%",
            ),

            rx.hstack(
                rx.text(f"{ship['price']:,} CR", color="#10b981", font_weight="bold", font_size="1.05em"),
                rx.spacer(),
                rx.button(
                    rx.hstack(
                        rx.text("Purchase", font_size="0.8em", font_weight="bold"),
                        rx.icon("chevron-right", size=14),
                        align_items="center",
                        spacing="1",
                    ),
                    variant="outline",
                    color_scheme="blue",
                    size="2",
                    cursor="pointer",
                    _hover={"background_color": "#0d243a"},
                ),
                align_items="center",
                width="100%",
                padding_top="2",
            ),

            spacing="4",
            align_items="start",
        ),
        background_color="#0c1524",
        border="1px solid #1e293b",
        padding="1.25em",
        border_radius="lg",
        width="100%",
    )
