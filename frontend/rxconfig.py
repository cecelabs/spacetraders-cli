import reflex as rx
import config_direcciones


config = rx.Config(
    app_name="space_ui",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)