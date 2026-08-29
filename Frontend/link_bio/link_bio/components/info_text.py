import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def info_text(tittle : str, body : str) -> rx.Component:
    return rx.box(
        rx.text(rx.text.strong(tittle, color=Color.PRIMARY.value), " ",body),
        font_size=styles.Size.MEDIUM.value,
        color = TextColor.BODY.value
    )