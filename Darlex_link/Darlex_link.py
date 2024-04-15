
import reflex as rx

from Darlex_link.components.footer import footer
from Darlex_link.components.navbar import navbar
from Darlex_link.views.header.header import header
from Darlex_link.views.header.links.links import links
from Darlex_link.views.sponsors.sponsors import sponsors
import Darlex_link.styles.styles as styles
from Darlex_link.styles.styles import Size as Size
class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            ),
        ),
        footer()
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="DarlexDEv",
    description="Desarrollador Web python"
    )