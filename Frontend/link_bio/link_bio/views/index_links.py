import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.tittle import tittle
from link_bio.routes import Route
import link_bio.constants as const
from link_bio.components.link_sponsor import link_sponsor
from link_bio.components.newsletter import newsletter
from link_bio.styles.colors import Color as Color

def index_links() -> rx.Component:
    return rx.vstack(
        tittle("Comunidad"),
        link_button("Cursos gratis",
                    "Consulta mis tutoriales para aprender programación",
                    "/icons/code.svg", 
                    Route.COURSES.value,
                    Color.YELLOW.value),
        
        link_button("Mi academia", 
                    "Estudia la programación desde cero con mouredev pro",
                    "/icons/pro.svg", 
                    const.PRO_URL,
                    Color.ORANGE.value),
        
        link_button("Máster de Desarrollo con IA", 
                    "Acredítalo con titulación universitaria", 
                    "/icons/logo_symbol.svg", 
                    const.PAGE_IA_CURSO,
                    Color.GREEN.value),
        
        link_button("Discord", 
                    "El chat y los grupos de estudio de la comunidad", 
                    "/icons/discord.svg", 
                    const.DISCORD_URL),
        
        link_button("Youtube", 
                    "Cursos y tutoriales sobre desarrollo de software", 
                    "/icons/youtube.svg", 
                    const.YOUTUBE_URL),
        
        
        tittle("Newsletter"),
        link_button("mouredev.log();", 
                    "La newsletter de la comunidad para aprender, crecer y avanzar", 
                    "/icons/book.svg", 
                    const.NEWSLETTER_URL),
        newsletter(),
        rx.spacer(),
        
        tittle("Destacado"),    
        rx.hstack(
            link_sponsor("js_highlighted.png",
                        const.JS_COURSE_URL,
                        "Curso de Javascript"),
            link_sponsor("python_highlighted.png",
                        const.PYTHON_COURSE_URL,
                        "Curso de Python")
        ),
        rx.spacer(),
        
        tittle("Recursos y más"),
        link_button("Git y Github desde cero", 
                    "Aquí puedes comprar mi libro en formato físico y eBook", 
                    "/icons/git.svg", 
                    const.GIT_COURSE_URL),
                
        link_button("Twitch", 
                    "Transmisiones sobre programación y desarrollo",
                    "/icons/twitch.svg", 
                    const.TWITCH_URL),
                
        link_button("Youtube | Canal secundario", 
                    "Emisiones en directo destacadas",
                    "/icons/youtube.svg", 
                    const.YOUTUBE_SECONDARY_URL),
                
        link_button("Invítame un café", 
                    "¿Quieres ayudarme a que siga creando contenido?",
                    "/icons/coffee.svg", 
                    const.COFFEE_URL),
        
        
        tittle("Contacto"),
        link_button("MyPublicInbox", 
                    "Respuesta rápida y con preferencia", 
                    "/icons/checkemail.svg", 
                    const.MYPUBLICINBOX_URL),
        
        link_button("Email", 
                    const.EMAIL, 
                    "/icons/email.svg", 
                    f"mailto:{const.EMAIL}"),
        rx.spacer(),
        rx.spacer(),
        width = "100%",
    )