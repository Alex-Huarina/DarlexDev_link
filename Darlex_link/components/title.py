import reflex as rx
import Darlex_link.styles.styles as styles


def title (text:str) -> rx.Component:
    return rx.chakra.heading(
        text,
        size="lg",
        style=styles.title_style
    )
    