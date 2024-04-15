import reflex as rx
import Darlex_link.styles.styles as styles
from Darlex_link.styles.styles import Size as Size

def link_button (title:str, body:str, image:str, url:str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.button(
            rx.chakra.hstack(
                rx.chakra.image(
                    src=image,
                    width=styles.Size.LARGE.value,
                    height=styles.Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.chakra.vstack(
                    rx.chakra.text(
                        title, 
                        style=styles.button_title_style
                    ),
                    rx.chakra.text(
                        body, 
                        style=styles.button_body_style
                    ),
                    align_items="start",
                    spacing=Size.SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right = Size.SMALL.value
                ),
                whidth="100%"
            ),
        ),
        href=url,
        is_external=True,
        width ="100%",
    )