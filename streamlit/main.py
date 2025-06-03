# main.py

import streamlit as st
import os
from PIL import Image
import pandas as pd

# Configuración general de la página
st.set_page_config(page_title="Gebmind", page_icon="🌐", layout="wide")

# Definir rutas base de carpetas (según tu estructura real)
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
DATA_DIR = os.path.join(ASSETS_DIR, "data")
MAPS_DIR = os.path.join(ASSETS_DIR, "maps")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
MODELS_DIR = os.path.join(ASSETS_DIR, "models")  # por si quieres usarlo más adelante

# Función para cargar imágenes de forma segura
def load_image(image_name):
    image_path = os.path.join(ASSETS_DIR, image_name)
    if os.path.exists(image_path):
        try:
            return Image.open(image_path)
        except Exception as e:
            st.warning(f"⚠️ No se pudo abrir la imagen {image_name}: {e}")
    else:
        st.warning(f"⚠️ Imagen no encontrada: {image_name}")
    return None

# Sidebar con logo y navegación
logo = load_image("gebmindlogo.png")
if logo:
    st.sidebar.image(logo, width=100)

st.sidebar.title("Navegación")
opcion = st.sidebar.radio("", ("Inicio", "Resultados del Modelo", "Mapas de Locales", "Contacto", "Quiénes Somos"))

# --- Página de Inicio ---
if opcion == "Inicio":
    st.title("Bienvenido a Gebmind: Encuentra el Local Perfecto para tu Negocio")

    col1, col2 = st.columns([1, 2])
    if logo:
        st.image(logo, width=200)

    with col1:
        st.subheader("🌟 Nuestro Producto")
        st.write("""
        Ofrecemos soluciones innovadoras para la transformación digital de tu negocio.
        Nuestra plataforma usa Inteligencia Artificial para analizar datos y encontrar las mejores opciones de locales.
        """)

    with col2:
        st.subheader("🔍 ¿Por qué elegirnos?")
        st.write("""
        Elegir la ubicación adecuada es clave para el éxito de cualquier empresa.
        En Gebmind analizamos datos demográficos, socioeconómicos y de competencia para ayudarte a tomar la mejor decisión.
        """)

    st.subheader("🚀 ¿Cómo te ayudamos?")
    st.markdown("""
    - **Análisis Demográfico:** Datos de población y nivel socioeconómico.
    - **Análisis de la Competencia:** Identifica negocios similares.
    - **Información de Locales:** Características, precios y fotos.
    """)

# --- Resultados del Modelo ---
elif opcion == "Resultados del Modelo":
    st.title("🔎 Resultados del Modelo Predictivo")

    report_path = os.path.join(DATA_DIR, "classification_report.csv")
    if os.path.exists(report_path):
        st.success("✅ Reporte de clasificación cargado correctamente.")
        report_df = pd.read_csv(report_path)
        st.dataframe(report_df)
    else:
        st.warning("⚠️ Reporte de clasificación no disponible.")

    st.subheader("📊 Visualizaciones del Modelo")

    imagenes = [
        ("feature_importance.png", "Importancia de Variables"),
        ("roc_curve_multiclase.png", "Curva ROC Multiclase"),
        ("roc_curve.png", "Curva ROC Clase Alta")
    ]

    cols = st.columns(len(imagenes))
    for i, (img_name, caption) in enumerate(imagenes):
        img_path = os.path.join(IMAGES_DIR, img_name)
        if os.path.exists(img_path):
            st.image(img_path, caption=caption, use_container_width=True)
        else:
            st.warning(f"⚠️ Imagen no encontrada: {img_name}")

# --- Página de Mapas de Locales ---
elif opcion == "Mapas de Locales":
    st.title("🗺️ Mapas Interactivos de Locales Disponibles")

    st.write("""
    Descubre nuestros mapas generados con Inteligencia Artificial.
    Explora información clave para tomar decisiones estratégicas.
    """)

    mapas_html = [
        ("mapa_barrios_restauracion.html", "Mapa Barrios Restauración"),
        ("mapa_barrios.html", "Mapa Barrios"),
        ("mapa_madrid_barrios_locales.html", "Mapa Madrid Barrios Locales"),
        ("mapa_categorias.html", "Mapa Categorías"),
        ("mapa_densidad.html", "Mapa Densidad"),
        ("mapa_ponderado.html", "Mapa Ponderado"),
        ("mapa_predicciones_modelo.html", "Mapa Predicciones Modelo"),
        ("mapa_valoracion_colormap.html", "Mapa Valoración Colormap"),
        ("mapa_valoracion_puntos.html", "Mapa Valoración Puntos")
    ]

    for nombre_archivo, titulo in mapas_html:
        st.subheader(f"🗂️ {titulo}")
        html_path = os.path.join(MAPS_DIR, nombre_archivo)
        if os.path.exists(html_path):
            with open(html_path, "r", encoding="utf-8") as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=500, scrolling=False)
        else:
            st.warning(f"⚠️ Mapa no encontrado: {nombre_archivo}")

# --- Página de Contacto ---
elif opcion == "Contacto":
    st.subheader("📬 Formulario de Contacto")
    st.markdown("¿Tienes preguntas o necesitas ayuda? ¡Contáctanos!")

    with st.form("formulario_contacto"):
        nombre = st.text_input("Nombre")
        correo = st.text_input("Correo Electrónico")
        mensaje = st.text_area("Mensaje")
        enviado = st.form_submit_button("Enviar")

    if enviado:
        if nombre and correo and mensaje:
            st.success("¡Gracias por tu mensaje! Te responderemos pronto.")
        else:
            st.warning("⚠️ Por favor, completa todos los campos.")

# --- Página de Quiénes Somos ---
elif opcion == "Quiénes Somos":
    st.subheader("👥 Conoce a Gebmind")

    col_texto, col_imagen = st.columns([2, 1])

    with col_texto:
        st.write("""
        En Gebmind somos un equipo apasionado por la tecnología y la Inteligencia Artificial.
        Queremos ayudarte a transformar tu negocio con análisis de datos y soporte personalizado.
        """)

        st.markdown("""
        **Nuestros valores:**
        - 🔬 Innovación constante para resolver desafíos.
        - 🤝 Compromiso con nuestros clientes.
        - 🥇 Excelencia en soluciones y atención.
        """)

        st.subheader("📌 Información de Contacto")
        st.write("""
        - **Empresa**: GEBMIND S.L.
        - **Descripción**: Proveedor de soluciones tecnológicas y consultoría.
        - **Dirección**: Madrid, España.
        - **Correo**: gebmind@gmail.com
        - **Teléfono**: +34 616 391 289
        """)

    with col_imagen:
        equipo_path = os.path.join(ASSETS_DIR, "gebmindteam.png")
        if os.path.exists(equipo_path):
            st.image(equipo_path, caption="Equipo Gebmind", use_container_width=True)
        else:
            st.warning("No se encontró la imagen del equipo.")

# --- Pie de Página ---
st.markdown("""
---
🌐 Desarrollado por Gebmind © 2025  
""")