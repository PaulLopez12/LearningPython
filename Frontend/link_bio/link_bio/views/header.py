import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.link_button import link_button
import link_bio.styles.styles as styles
from link_bio.styles.colors import TextColor as TextColor
import link_bio.constants as const
from link_bio.styles.colors import Color as Color

def header(details = True, live= False, live_title="") -> rx.Component:
        return rx.vstack(
                rx.hstack(
                        rx.box(
                                rx.cond(
                                        live,
                                        rx.link(
                                                rx.image(
                                                        src="/icons/twitch.svg",
                                                        height=styles.Size.DEFAULT.value,
                                                        width=styles.Size.DEFAULT.value,
                                                ),
                                        href=const.TWITCH_URL,
                                        is_external=True,
                                        class_name="blink",
                                        border_radius="50%",
                                        padding=styles.Size.SMALL.value,
                                        bg=Color.PURPLE.value,
                                        position="absolute",
                                        top=f"-{styles.Size.DEFAULT.value}",
                                        right=f"-{styles.Size.DEFAULT.value}",
                                        z_index="2"),
                                ),
                                rx.avatar(
                                        name="Brais Moure",
                                        size=styles.Spacing.MEDIUM_BIG.value,
                                        src="/avatar.webp",
                                        radius="none",
                                        color=TextColor.LIGHT.value,
                                        bg=Color.DARK.value,
                                        style=styles.image_style,
                                        alt="Avatar MoureDev"),
                        position="relative"),
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
                                rx.cond(
                                        True,
                                        link_button("En directo",
                                                live_title,
                                                "/icons/twitch.svg",
                                                const.TWITCH_URL,
                                                highlight_color=Color.PURPLE.value)),
                                rx.text("Soy ingeniero de software y divulgador. Te enseño programación e inteligencia artificial desde cero. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!", color = TextColor.BODY.value),
                                spacing="7"
                        )
                ),
                width="100%",
                spacing="7"
        )



