import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
import link_bio.styles.styles as styles
from link_bio.styles.colors import TextColor as TextColor
import link_bio.constants as const
from link_bio.styles.colors import Color as Color

def header(details = True) -> rx.Component:
        return rx.vstack(
                rx.hstack(
                        rx.avatar(name="Brais Moure", 
                                size="7", 
                                src = "avatar.webp",
                                color = TextColor.BODY.value,
                                bg =Color.CONTENT.value,
                                padding = "2px",
                                border = "4px",
                                border_color = Color.PRIMARY.value,
                                style=styles.image_style),
                rx.vstack(
                        rx.text("Brais Moure", size="5", trim="end"),
                        rx.text("@mouredev", trim="start", color=TextColor.BODY.value),
                        rx.hstack(
                                link_icon("/icons/github.svg",
                                        const.GITHUB_URL,
                                        "icono de github"),
                                link_icon("/icons/x.svg",
                                        const.TWITTER_X_URL,
                                        "icono de twitter"),
                                link_icon("/icons/instagram.svg",
                                        const.INSTAGRAM_URL,
                                        "icono de instagram"),
                                link_icon("/icons/tiktok.svg",
                                        const.TIKTOK_URL,
                                        "icono de tiktok"),
                                link_icon("/icons/facebook.svg",
                                        const.FACEBOOK_URL,
                                        "icono de facebook"),
                                link_icon("/icons/spotify.svg",
                                        const.SPOTIFY_URL,
                                        "icono de spotify"),
                                link_icon("/icons/linkedin.svg",
                                        const.LINKEDIN_URL,
                                        "icono de linkedin")
                        )
                )
        ),
                rx.cond(
                        details,
                        rx.vstack(
                                rx.flex(
                                        info_text("16+", "años de experiencia"),
                                        rx.spacer(),
                                        info_text("150+", "aplicaciones creadas"),
                                        rx.spacer(),
                                        info_text("3M+", "seguidores"),
                                        width="100%",
                ),
                                rx.text("Soy ingeniero de software y divulgador. Te enseño programación e inteligencia artificial desde cero. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!", color = TextColor.BODY.value),
                                spacing="7"
                        )
                ),
                width="100%",
                spacing="7"
        )





