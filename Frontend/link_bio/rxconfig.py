import reflex as rx

config = rx.Config(
    app_name="link_bio",
    api_url="https://link-bio-teal-wood.reflex.run/",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)