import reflex as rx
from link_bio.components.tittle import tittle
from link_bio.components.link_sponsor import link_sponsor
import link_bio.constants as const

def sponsors() -> rx.Component:
    return rx.vstack(
        tittle("Colaboran"),
        rx.flex(
            link_sponsor("elgato.png", 
                        const.ELGATO_URL,
                        ""),
            link_sponsor("mvp.png",
                        const.MVP_URL,
                        ""),
            link_sponsor("githubstar.png", 
                        const.GITHUB_STAR_URL,
                        ""),
            spacing="5",
            flex_wrap = "wrap",
            width = "100%",
            align="center"
        ),
        width = "100%",
        align_items="start",
        spacing="3"
    )