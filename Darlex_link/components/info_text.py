import reflex as rx
from Darlex_link.styles.colors import TextColor
from Darlex_link.styles.colors import Color as Color
from Darlex_link.styles.styles import Size as Size


def info_text (title:str, body:str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value,
        ),
        f" {body}+", 
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value,
        
    )