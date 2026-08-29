import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.styles.colors import TextColor as TextColor

def newsletter() -> rx.Component:
    return rx.vstack(
        rx.html(
            "<iframe src='https://subscribe-forms.beehiiv.com/84ec1259-e16b-41b4-be33-d1f2dd2cf53e' class='beehiiv-embed' data-test-id='beehiiv-embed' title='Formulario de suscripción newsletter mouredev' width='100%' height='110px' frameborder='0' scrolling='no' allowtransparency='true' style='width: 100%; height: 110px; margin: 0; border-radius: 0px !important; background-color: transparent; color-scheme: normal;'></iframe>",
            width = "100%",
            height = "100px"
        ),
        rx.hstack(
            rx.icon("mail_check"),
            rx.text("Más de 100.000 personas ya siguen mis consejos semanales",
                    color = TextColor.BODY.value),
            align="center"
        ),
        width = "100%",
        spacing="2"
    )