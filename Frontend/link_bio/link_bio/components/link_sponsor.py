import reflex as rx
from link_bio.components.tittle import tittle
import link_bio.styles.styles as styles

def link_sponsor(image : str, url : str, alt : str) -> rx.Component:
    return rx.link(
        rx.image(
            height = styles.Size.VERYBIG.value,
            src = image,
            width = "auto",
            alt=alt
        ),
        href= url,
        is_external= True
    )