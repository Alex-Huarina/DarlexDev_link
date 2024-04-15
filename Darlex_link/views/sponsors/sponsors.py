import reflex as rx
from Darlex_link.components.title import title
from Darlex_link.components.link_sponsor import Link_sponsor
import Darlex_link.constants as const
from Darlex_link.styles.styles import Size


def sponsors()-> rx.Component:
    return rx.chakra.vstack(
        title("Colaboran"),
        rx.chakra.responsive_grid(
            Link_sponsor(
                "favicon.ico",
                const.ELGATO_URL,
                "Logotipo de Elgato"
            ),
            Link_sponsor(
                "favicon.ico",
                const.MVP_URL,
                "Logotipo de Microsoft MVP"
            ),
            spacing=Size.LARGE.value,
            columns=[1,2]
        ),
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value,
    )