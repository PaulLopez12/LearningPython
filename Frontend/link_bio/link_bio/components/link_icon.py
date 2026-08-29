import reflex as rx
import link_bio.styles.styles as styles


def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
        src=image,
        width=styles.Size.LARGE.value,
        height=styles.Size.LARGE.value,
        alt=alt
        ),
        href=url,
        is_external=True,
        width = "100%",
    )