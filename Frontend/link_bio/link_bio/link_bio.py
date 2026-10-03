import reflex as rx
import link_bio.styles.styles as styles
from link_bio.pages.index import index
from link_bio.pages.courses import courses
from link_bio.api.api import api_app


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    api_transformer=api_app,
)