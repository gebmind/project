import streamlit as st
import os
from PIL import Image

# Configuración general
st.set_page_config(page_title="Gebmind", page_icon="🌐", layout="centered")

# Sidebar con navegación manual

st.sidebar.image("assets/logo.png", width=100)
st.sidebar.title("Navegación")
opcion = st.sidebar.radio("", ("Inicio", "Mapa de Locales", "Contacto", "Quiénes Somos"))

# --- Página de Inicio ---
if opcion == "Inicio":
    st.title("Bienvenido a nuestra web, encuentra el local perfecto para Triunfar")

    col1, col2 = st.columns([1, 2])  # Divide en dos columnas con proporciones 1:2

    image = Image.open("assets/logo.png")
    st.image(image, width=200)
    st.subheader("Gebmind te ayuda a crecer.")

    with col1:
        st.subheader("Nuestro producto")
        st.write("""
        Ofrecemos soluciones innovadoras para facilitar la transformación digital de tu negocio.
        Nos centramos en calidad, eficiencia y soporte personalizado.
        Nuestra plataforma utiliza inteligencia artificial para analizar datos y ofrecerte las mejores opciones de locales comerciales.
        """)

    with col2:
        st.subheader("La clave para el éxito de tu negocio está en la ubicación ideal.")
        st.write("""
        En Gebmind, entendemos que elegir el local adecuado es el primer paso crucial para el éxito de tu empresa o negocio autónomo.
        Te ofrecemos una búsqueda inteligente y personalizada, basada en análisis exhaustivos de datos demográficos, socioeconómicos y de la competencia.
        """)
        st.write("""
        Nuestro objetivo es proporcionarte información valiosa para que tomes la decisión más informada y encuentres ese espacio único donde tu negocio pueda prosperar.
        """)

    st.subheader("¿Cómo te ayudamos?")
    st.markdown("""
    - **Análisis Demográfico Avanzado:** Conoce la población, la distribución por edades y el nivel socioeconómico de las zonas de interés.
    - **Evaluación de la Competencia:** Identifica negocios similares en la zona y analiza su presencia.
    - **Información Detallada de Locales:** Accede a características, precios y fotografías de los locales disponibles.
    """)

    st.subheader("¡Empieza hoy mismo a encontrar tu local ideal!")
    
# --- Página de Mapas de Información ---
if opcion == "Mapa de Locales":
    st.title("Mapa de Locales Disponibles")

    st.markdown("""
    Aquí puedes ver una serie de mapas generados con nuestra Inteligencia Artificial y nuestra base de datos como ejemplo.
    Lo que ves son mapas de Madrid, pero podemos generar mapas de cualquier ciudad o zona que necesites.
    """)

    # Definir ruta de los mapas
    mapas_dir = os.path.join("assets", "maps")

    # Lista de archivos HTML de mapas
    mapas_html = [
        "mapa_barrios_restauracion.html",
        "mapa_barrios.html",
        "mapa_madrid_barrios_locales.html",
        "mapa_categorias.html",
        "mapa_densidad.html",
        "mapa_ponderado.html",
        "mapa_predicciones_modelo.html",
        "mapa_valoracion_puntos.html",
    ]

    st.subheader("🧩 Vista conjunta de mapas")

    # Mostrar los mapas en cuadrícula
    num_columnas = 2
    columnas = st.columns(num_columnas)

    for i, nombre_mapa in enumerate(mapas_html):
        col = columnas[i % num_columnas]
        html_path = os.path.join(mapas_dir, nombre_mapa)
        with col:
            st.markdown(f"**{nombre_mapa.replace('_', ' ').replace('.html', '').title()}**")
            if os.path.exists(html_path):
                with open(html_path, "r", encoding="utf-8") as f:
                    html_content = f.read()
                st.components.v1.html(html_content, height=450, scrolling=False)
            else:
                st.warning(f"No se encontró el archivo: {nombre_mapa}")

# --- Página de Contacto ---
if opcion == "Contacto":
    st.subheader("Formulario de Contacto")
    st.markdown("¿Tienes alguna pregunta o necesitas ayuda personalizada?")
    st.markdown("¡No dudes en contactarnos!")

    with st.form("formulario_contacto"):
        nombre = st.text_input("Nombre")
        correo = st.text_input("Correo electrónico")
        mensaje = st.text_area("Mensaje")
        enviado = st.form_submit_button("Enviar")

    if enviado:
        if nombre and correo and mensaje:
            # Aquí puedes integrar SMTP o usar un servicio externo
            st.success("Gracias por tu mensaje. Te responderemos pronto.")
        else:
            st.warning("Por favor, rellena todos los campos.")

# --- Página de Quiénes Somos ---
elif opcion == "Quiénes Somos":
    st.subheader("Conoce a Gebmind")

    col_imagen, col_texto = st.columns([1, 2])

    #with col_imagen:
        #st.image("assets/equipo_gebmind.jpg", width=300) # Reemplaza con una imagen de tu equipo o empresa

    with col_texto:
        st.write("""
        En Gebmind, somos un equipo **apasionado por la tecnología** y la **aplicación de la Inteligencia Artificial** para transformar y optimizar los sistemas empresariales actuales.
        Creemos firmemente en el poder de la innovación para generar un **ahorro significativo** y una **mejora continua** en los procesos de nuestros clientes.
        """)
        st.write("""
        Nuestra misión es facilitar la **transformación digital** de negocios como el tuyo, ofreciendo soluciones **innovadoras**, **eficientes** y con un **soporte personalizado** que marca la diferencia.
        """)

    st.subheader("Nuestros Valores")
    col_valores1, col_valores2, col_valores3 = st.columns(3)
    with col_valores1:
        st.markdown("**Innovación**")
        st.write("Buscamos constantemente nuevas formas de aplicar la tecnología para resolver desafíos empresariales.")
    with col_valores2:
        st.markdown("**Compromiso**")
        st.write("Estamos dedicados al éxito de nuestros clientes y trabajamos codo a codo para alcanzar sus objetivos.")
    with col_valores3:
        st.markdown("**Excelencia**")
        st.write("Nos esforzamos por ofrecer soluciones de la más alta calidad y un servicio impecable.")

    st.subheader("Nuestro Equipo")
    st.write("""
    - **Empresa**:      GEBMIND S.L.
    - **Descripción**:  Proveedor de soluciones tecnológicas y consultoría.
    - **Dirección**:    Madrid, España
    - **Correo**:       gebmind@gmail.com
    - **Teléfono**:     +34 616 391 289
    """)
