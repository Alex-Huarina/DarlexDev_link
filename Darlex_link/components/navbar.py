import reflex as rx
import Darlex_link.styles.styles as styles
from Darlex_link.styles.styles import Size as Size
from Darlex_link.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.box(
            rx.chakra.span(
                "Darlex",
                color=Color.PRIMARY.value
            ),
            rx.chakra.span(
                "Dev",
                color=Color.SECONDARY.value
            ),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )