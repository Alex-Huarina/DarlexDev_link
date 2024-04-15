import reflex as rx
from Darlex_link.components.link_icon import link_icon
from Darlex_link.components.info_text import info_text
from Darlex_link.styles.styles import Size as Size
from Darlex_link.styles.styles import Color as Color
from Darlex_link.styles.styles import TextColor as TextColor
import Darlex_link.constants as const
import datetime

def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.chakra.avatar(
                name="Alex", 
                size="xl",
                src="avatar.webp",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.chakra.vstack(
                rx.chakra.heading(
                    "ALEX HUARINA",
                    size="lg"
                ),
                rx.chakra.text(
                    "@DarlexDev",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.chakra.hstack(
                    link_icon(
                        "icons/twitch.svg",
                        const.INSTAGRAM_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        const.INSTAGRAM_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        const.INSTAGRAM_URL,
                        "GitHub"
                    ),
                    spacing=Size.DEFAULT.value,
                ),
                align_items="start",
            ),
            spacing=Size.DEFAULT.value,
        ),
        rx.chakra.flex(
            info_text(
                f"{experience()}", 
                "años de experiencias"
            ),
            rx.chakra.spacer(),
            info_text(
                "+2", 
                "años de experiencias"
            ),
            rx.chakra.spacer(),
            info_text(
                "+2", 
                "años de experiencias"
            ),
            width="100%",
            
        ),
        rx.chakra.text(f"""Soy egresado de la carrera ingeniería de sistemas de la Universidad Tecnológica Boliviana y estoy apasionado por la tecnología y el desarrollo web desde hace más de {experience()}. Me especializo en el desarrollo tanto front-end como back-end, así como en ciberseguridad. Me encanta estar al día con las últimas tendencias tecnológicas y aprender algo nuevo""",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value,
        ),
        spacing=Size.BIG.value,
        align_items="start",
    )

def experience() -> int:
    return "+2"
