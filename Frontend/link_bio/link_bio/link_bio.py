import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.views.sponsors.sponsors import sponsors

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = styles.Size.BIG.value,
                padding = styles.Size.BIG.value
            )
        ),
        rx.center(
            footer()
        ),
        background_image = "url('/bg_dark_pattern.png')"
    )



app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Mouredev | Te enseño programación y desarrollo de software",
    description="Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador frelance full-stack y divulgador",
    image="logo_symbol.svg"
    )
app._compile()