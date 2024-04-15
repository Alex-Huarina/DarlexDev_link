import reflex as rx
from Darlex_link.styles.styles import Size as Size

def Link_sponsor (imagen:str, url:str, alt:str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            src=imagen,
            height=Size.VERY_BIG.value,
            Width="auto",
            alt=alt
        ),
        href=url,
        is_external=True
    )