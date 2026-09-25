import reflex as rx
from link_bio.styles.colors import Color

class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon: rx.Var[rx.Component]
    href: rx.Var[str]
    target: str = "_blank"
    badge: dict = {"dot": True, "color": Color.PRIMARY.value}


float_button = FloatButton.create