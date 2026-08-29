import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.constants as const

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(
                src="logo.svg",
                width = "auto",
                height = styles.Size.LARGE.value,
                justify = "start",
                alt="Mouredev logo"),
            href=const.MOUREDEV_URL
            ),
        position="sticky",
        bg=Color.DARK.value,
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.DEFAULT.value,
        z_index="999",
        top="0" #siempre aparece la barra arriba al hace scroll,
    )