import reflex as rx
import datetime 
import link_bio.styles.styles as styles
from link_bio.styles.colors import TextColor as TextColor
import link_bio.constants as const
from link_bio.components.link_icon import link_icon
from link_bio.styles.colors import Color as Color

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="logo_symbol.svg",
                height = styles.Size.BIG.value,
                weight = styles.Size.BIG.value,
                alt = "Logotipo de Mouredev. Una \"eme\" entre llaves."),
        rx.link(
            rx.box(
                f"© 2014-{datetime.date.today().year} ",
                rx.text(
                    "MoureDev by Brais Moure",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                " v5.",
                padding_top=styles.Size.DEFAULT.value
            ),
            href=const.MOUREDEV_URL,
            is_external=True,
            font_size=styles.Size.MEDIUM.value,
            trim="both"
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=styles.Size.LARGE.value,
                    width=styles.Size.LARGE.value,
                    alt="Logo GitHub"
                ),
                rx.text(
                    "Building software with ♥ from Galicia to the world.",
                    font_size=styles.Size.MEDIUM.value,
                    margin_top="0"
                )
            ),
            href=const.REPO_URL,
            is_external=True,
            trim="both"
        ),
        rx.text(
            "Con el apoyo de",
            rx.image(
                src=f"/raiola_networks.svg",
                on_click=rx.redirect(
                    const.RAIOLA_NETWORKS_URL,
                    is_external=True
                ),
                width="200px",
                height="100%",
                cursor="pointer",
                padding_x=styles.Size.MEDIUM.value,
                alt="Logo Raiola Networks"
            ),
            font_size=styles.Size.MEDIUM.value,
            display="flex",
            align_items="center"
        ),
        align="center",
        padding_bottom=styles.Size.VERYBIG.value,
        padding_x=styles.Size.BIG.value,
        color=TextColor.BODY.value
    )