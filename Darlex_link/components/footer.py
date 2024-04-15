import reflex as rx
import datetime
from Darlex_link.styles.colors import TextColor
from Darlex_link.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.image(
            src="favicon.ico",
            height=Size.VERY_BIG.value,
            weight=Size.VERY_BIG.value,
            alt="Logotipo de DarlexDev"
        ),
        rx.chakra.link(
            f"© {datetime.date.today().year} DarlexDev.",
            href="https://DarlexDev.com",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.chakra.text(
            "BUILDING SOFTWARE",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        padding_x=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value,
    )