import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "600px"

# Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css?family=Comfortaa:wght@500&display=swap",
]

class Size(Enum):
    SMALL = "0.5em" #em usa el tamaño de cada dispositivo
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERYBIG = "4em"

# Styles
BASE_STYLE = {
    "font_family" : Font.DEFAULT.value,
    "font_weight" : FontWeight.LIGHT.value,
    "background_color" : Color.DARK.value,
    "background:_image" : "url('/bg_dark_pattern.png')",
    "background_repeat": "repeat",
    "background_attachment": "fixed",
    rx.heading : {
        "color" : TextColor.HEADER.value,
        "font_weight" : FontWeight.MEDIUM.value,
        "font_family" : Font.TITTLE.value,
    },
    rx.button : {
        "width" : "100%",
        "height" : "100%",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value,
        "color" : TextColor.HEADER.value,
        "background_color" : Color.CONTENT.value,
        "cursor" : "pointer",
        "transition": "transform 0.05s ease",
        "box_shadow": f"3px 3px 0px 0px {Color.LIGHT.value}",
        "border": f"1px solid {Color.LIGHT.value}",
        "white_space" : "normal",
        "text_align" : "start",
        "_hover" : {
            "background_color" : Color.SECONDARY.value,
            "box_shadow": "none",
            "transform": "translate(3px, 3px)"
        }
    },
    rx.link : {
        "text_decoration" : "none",
        "_hover" : {} #indica un estado alternativo del link al pasar el mouse
    }
}

button_tittle_style = dict(
    font_family = Font.TITTLE.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size = Size.DEFAULT.value,
    color = TextColor.DARK.value
    
)

button_body_style = dict(
    font_weight = FontWeight.LIGHT.value,
    font_size = Size.MEDIUM.value,
    color = TextColor.DARK.value
)

tittle_style = dict(
    font_family = Font.TITTLE.value,
    width = "100%",
    padding_top = Size.DEFAULT.value,
    color = TextColor.HEADER.value
)

navbar_tittle_style = dict(
    font_family = Font.LOGO.value,
    font_weight = FontWeight.MEDIUM.value,
    font_size = Size.LARGE.value,
    weight = "bold"
)

image_style = {
    "border": f"1px solid {Color.LIGHT.value}",
    "box_shadow": f"3px 3px 0px 0px {Color.LIGHT.value}",
    "_hover": {
        "box_shadow": f"6px 6px 0px 0px {Color.LIGHT.value}",
        "transform": "translate(-3px, -3px)",
        }
    }