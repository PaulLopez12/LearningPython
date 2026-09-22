import reflex as rx
import link_bio.utils as utils
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.views.sponsors import sponsors

@rx.page(
    title= utils.index_title,
    description= utils.index_description,
    image= utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
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

