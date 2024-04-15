import reflex as rx
from Darlex_link import constants as const
from Darlex_link.components.link_button import link_button
from Darlex_link.components.title import title
from Darlex_link.styles.styles import Size


def links() -> rx.Component:
    return rx.chakra.vstack(
        title("Comunidad"),

        link_button(
            "Twitch",
            "Directos de lunes a viernes",
            "icons/twitch.svg",
            "https://twitch.tv"
        ),
        link_button(
            "YouTube(primer canal)",
            "Tutoriales semanales",
            "icons/twitch.svg",
            "https://youtube.com"
        ),
        link_button(
            "Discord",
            "Hola",
            "icons/twitch.svg",
            "https://youtube.com"
        ),

        title("Comunidad"),

        link_button(
            "Twitch",
            "Directos de lunes a viernes",
            "icons/twitch.svg",
            "https://twitch.tv"
        ),
        link_button(
            "YouTube(primer canal)",
            "Tutoriales semanales",
            "icons/twitch.svg",
            "https://youtube.com"
        ),
        link_button(
            "Discord",
            "Hola",
            "icons/twitch.svg",
            "https://youtube.com"
        ),

        title("Contacto"),

        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia",
            "icons/twitch.svg",
            "https://youtube.com"
        ),
        link_button(
            "Gmail",
            "Hola",
            "icons/twitch.svg",
            f"mailto:{const.EMAIL}",
        ),

        width ="100%",
        spacing=Size.MEDIUM.value,
    )