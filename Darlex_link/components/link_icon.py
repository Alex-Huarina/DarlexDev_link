import reflex as rx
from Darlex_link.styles.styles import Size as Size

def link_icon (image:str, url:str, alt:str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            src=image,
            width=Size.LARGE.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )