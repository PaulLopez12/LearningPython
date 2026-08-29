import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def link_button(tittle : str, body : str, image : str, url : str, highlight_color=None) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin = styles.Size.MEDIUM.value,
                    alt=tittle
                ),
                rx.vstack(
                    rx.text(tittle, style=styles.button_tittle_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing = "2",
                    align_items="start",
                    padding_right = styles.Size.SMALL.value
                    ),
                width = "100%"
                ),
            background_color=(
                highlight_color if highlight_color is not None else Color.PRIMARY.value
            )
            ),
        href=url,
        is_external=True,
        width = "100%"
    )

