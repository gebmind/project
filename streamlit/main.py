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
    st.sidebar.image(logo, width=300)

st.sidebar.title("Navegación")
opcion = st.sidebar.radio("", ("Inicio", "Base de datos", "Nuestros mapas", "Resultados del Modelo", "Contacto", "Quiénes Somos"))

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

# --- Página de Base de datos ---
elif opcion == "Base de datos":
    st.title("Explora nuestra Base de Datos de Locales")

    # Cargar la base de datos desde el CSV
    csv_path = os.path.join(DATA_DIR, "locales_procesado.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)

        st.sidebar.subheader("Filtros de Búsqueda")

        # Filtro por Nombre (input de texto)
        nombre_filtro = st.sidebar.text_input("Nombre del local (parcial):", "")

        # Filtro por Categoría (desplegable)
        categorias_disponibles = df["categoria_negocio"].dropna().unique()
        categoria_filtro = st.sidebar.selectbox("Categoría del negocio:", ["Todas"] + list(categorias_disponibles))

        # Filtro por Código Postal (formato 5 dígitos)
        codigo_postal = st.sidebar.text_input("Código Postal (formato 5 dígitos):", "")
        if codigo_postal and not codigo_postal.isdigit():
            st.sidebar.warning("⚠️ El Código Postal debe ser numérico.")
        elif codigo_postal and len(codigo_postal) != 5:
            st.sidebar.warning("⚠️ El Código Postal debe tener 5 dígitos.")

        # Filtro por puntuación_media
        min_puntuacion = float(df['puntuacion_media'].min())
        max_puntuacion = float(df['puntuacion_media'].max())
        puntuacion_range = st.sidebar.slider(
            "Puntuación:",
            min_value=min_puntuacion,
            max_value=max_puntuacion,
            value=(min_puntuacion, max_puntuacion)
        )

        # Filtro por numero_reviews
        min_reviews = int(df['numero_reviews'].min())
        max_reviews = int(df['numero_reviews'].max())
        reviews_range = st.sidebar.slider(
            "Número de reviews:",
            min_value=min_reviews,
            max_value=max_reviews,
            value=(min_reviews, max_reviews)
        )

        # Filtrar DataFrame según criterios
        filtered_df = df.copy()

        # Filtrar por Nombre
        if nombre_filtro:
            filtered_df = filtered_df[filtered_df['nombre'].str.contains(nombre_filtro, case=False, na=False)]

        # Filtrar por Categoría
        if categoria_filtro != "Todas":
            filtered_df = filtered_df[filtered_df['categoria_negocio'] == categoria_filtro]

        # Filtrar por Código Postal
        if codigo_postal and codigo_postal.isdigit() and len(codigo_postal) == 5:
            filtered_df = filtered_df[filtered_df['codigo_postal'] == int(codigo_postal)]

        # Filtrar por puntuación_media y numero_reviews
        filtered_df = filtered_df[
            (filtered_df['puntuacion_media'] >= puntuacion_range[0]) &
            (filtered_df['puntuacion_media'] <= puntuacion_range[1]) &
            (filtered_df['numero_reviews'] >= reviews_range[0]) &
            (filtered_df['numero_reviews'] <= reviews_range[1])
        ]

        # Seleccionar solo las columnas a mostrar
        columnas_mostrar = [
            'nombre',
            'direccion',
            'codigo_postal',
            'puntuacion_media',
            'numero_reviews',
            'tipo_negocio',
            'categoria_negocio',
            'valoracion'
        ]
        filtered_df = filtered_df[columnas_mostrar]

        # Mostrar resultados
        st.dataframe(filtered_df)

    else:
        st.warning("⚠️ No se encontró el archivo locales_procesado.csv en la carpeta de datos.") 

# --- Página de Nuestros mapas ---
if opcion == "Nuestros mapas":
    st.title("Nuestros Mapas de Locales Disponibles")

    # Obtener lista de mapas disponibles (HTML o PNG en la carpeta de mapas)
    mapas_disponibles = [f for f in os.listdir(MAPS_DIR) if f.endswith(('.html', '.png'))]

    if mapas_disponibles:
        # Selector lateral
        mapa_seleccionado = st.sidebar.selectbox(
            "Selecciona un mapa:", 
            mapas_disponibles
        )

        # Construir la ruta completa
        mapa_path = os.path.join(MAPS_DIR, mapa_seleccionado)

        # Mostrar el mapa (según su extensión)
        if mapa_seleccionado.endswith('.html'):
            with open(mapa_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=600, scrolling=True)
        elif mapa_seleccionado.endswith('.png'):
            st.image(mapa_path, caption=mapa_seleccionado, use_column_width=True)
        else:
            st.warning("Formato de archivo no soportado.")
    else:
        st.warning("No se encontraron mapas en la carpeta.")

# --- Resultados del Modelo ---
elif opcion == "Resultados del Modelo":
    st.title("🔎 Resultados del Modelo Predictivo")

    # Mostrar reporte de clasificación (CSV)
    report_path = os.path.join(DATA_DIR, "classification_report.csv")
    if os.path.exists(report_path):
        st.success("✅ Reporte de clasificación cargado correctamente.")
        report_df = pd.read_csv(report_path)
        st.dataframe(report_df)
    else:
        st.warning("⚠️ Reporte de clasificación no disponible.")

    st.subheader("📊 Visualizaciones del Modelo")

    # Lista de imágenes y captions
    imagenes_resultados = [
        ("curvas_roc.png", "Curvas ROC"),
        ("distribucion_clases_original.png", "Distribución de Clases Original"),
        ("distribucion_clases_smote.png", "Distribución de Clases Después de SMOTE"),
        ("importancia_variables.png", "Importancia de Variables"),
        ("matriz_confusion.png", "Matriz de Confusión")
    ]

    # Mostrar imágenes en columnas con tamaño adaptativo
    cols = st.columns(len(imagenes_resultados))
    for col, (img_name, caption) in zip(cols, imagenes_resultados):
        img_path = os.path.join(IMAGES_DIR, img_name)
        if os.path.exists(img_path):
            with open(img_path, "rb") as file:
                img_bytes = file.read()
            # Cargar imagen con resolución original y usar el nuevo parámetro
            col.image(img_bytes, caption=caption, use_container_width=True)
        else:
            col.warning(f"⚠️ Imagen no encontrada: {img_name}")

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
        - **Redes Sociales**: [GitHub](https://github.com/gebmind) | [X](https://x.com/GebMind)
        """)

    with col_imagen:
        equipo_image = load_image("gebmindteam.png")
        if equipo_image:
            st.image(equipo_image, width=800)
        else:
            st.warning("No se encontró la imagen del equipo.")

# --- Pie de Página ---
st.markdown("""
---
🌐 Desarrollado por Gebmind © 2025  
""")