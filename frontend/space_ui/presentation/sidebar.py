import reflex as rx


def sidebar_item(icon_tag: str, label: str, href: str, active: bool = False) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon_tag, size=18, color="#00d2ff" if active else "#64748b"),
            rx.text(
                label,
                color="#f8fafc" if active else "#94a3b8",
                font_size="0.9em",
                font_weight="semibold" if active else "normal",
            ),
            rx.spacer() if active else rx.box(),
            rx.icon("chevron-right", size=14, color="#00d2ff") if active else rx.box(),
            width="100%",
            padding="0.75em 1em",
            background_color="#0c1724" if active else "transparent",
            border_radius="md",
            border="1px solid #1e293b" if active else "1px solid transparent",
            align_items="center",
            spacing="3",
            _hover={"background_color": "#0d1b2a", "transition": "0.2s"},
        ),
        href=href,
        underline="none",
        width="100%",
    )


def sidebar(active_page: str = "shipyard") -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.icon("navigation", color="#00d2ff", size=24),
                padding="6px",
                background_color="#0d243a",
                border_radius="md",
            ),
            rx.vstack(
                rx.text("STELLAR NAV", color="#00d2ff", font_weight="bold", font_size="1.1em", letter_spacing="0.05em"),
                rx.text("Command v4.2", color="#64748b", font_size="0.75em", margin_top="-4px"),
                spacing="0",
                align_items="start",
            ),
            align_items="center",
            spacing="3",
            margin_bottom="1.5em",
        ),

        rx.vstack(
            rx.text("NAVIGATION", color="#475569", font_size="0.7em", font_weight="bold", letter_spacing="0.1em", margin_bottom="0.5em"),
            sidebar_item("layout-dashboard", "Dashboard", href="/", active=(active_page == "dashboard")),
            sidebar_item("rocket", "Fleet Command", href="/fleet", active=(active_page == "fleet")),
            sidebar_item("warehouse", "Shipyard", href="/shipyard", active=(active_page == "shipyard")),
            sidebar_item("file-text", "Contract Ledger", href="/contracts", active=(active_page == "contracts")),
            align_items="stretch",
            spacing="1",
            width="100%",
        ),

        rx.spacer(),

        rx.vstack(
            rx.hstack(
                rx.box(
                    background_color="#10b981",
                    width="8px",
                    height="8px",
                    border_radius="50%",
                    box_shadow="0 0 8px #10b981",
                ),
                rx.text("CONNECTED", color="#94a3b8", font_size="0.75em", font_weight="bold", letter_spacing="0.05em"),
                align_items="center",
                spacing="2",
                margin_bottom="0.5em",
            ),
            rx.vstack(
                rx.text("Credits Available", color="#64748b", font_size="0.75em"),
                rx.text("1,240,500 CR", color="#10b981", font_weight="bold", font_size="1.15em"),
                background_color="#0c1724",
                border="1px solid #1e293b",
                border_radius="lg",
                padding="1em",
                width="100%",
                align_items="start",
                spacing="1",
            ),
            align_items="start",
            width="100%",
        ),

        width="260px",
        background_color="#080c15",
        border_right="1px solid #1e293b",
        padding="1.5em",
        height="100vh",
        position="sticky",
        top="0",
        spacing="6",
        align_items="stretch",
    )
