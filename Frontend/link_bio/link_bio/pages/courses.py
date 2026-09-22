import reflex as rx
import link_bio.utils as utils
from link_bio.routes import Route
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.courses_links import courses_links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.views.sponsors import sponsors

@rx.page(
    route=Route.COURSES.value,
    title= utils.courses_title,
    description= utils.courses_description,
    image= utils.preview,
    meta=utils.courses_meta
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                courses_links(),
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