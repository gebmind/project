# main.py

import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

# Configuración general de la página
st.set_page_config(page_title="Gebmind", page_icon="🌐", layout="wide")

# Definir rutas base de carpetas (según tu estructura real)
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
DATA_DIR = os.path.join(ASSETS_DIR, "data")
MAPS_DIR = os.path.join(ASSETS_DIR, "maps")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
MODELS_DIR = os.path.join(ASSETS_DIR, "models")  
INFORMES_DIR = os.path.join(ASSETS_DIR, "informes")

# Función para cargar imágenes de forma segura
def load_image(image_name):
    image_path = os.path.join(IMAGES_DIR, image_name)
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
opcion = st.sidebar.radio("", ("Inicio", "Recomendador IA", "Base de datos", "Nuestros mapas", "Resultados del Modelo", "Contacto", "Quiénes Somos"))

# --- Página de Inicio ---
if opcion == "Inicio":
    st.title("Bienvenido a Gebmind")
    st.header("Encuentra el Local Perfecto para tu Negocio")   

    st.subheader("▻ Nuestro Producto")
    st.write("""
    Ofrecemos soluciones innovadoras para la transformación digital de tu negocio.
    Nuestra plataforma usa Inteligencia Artificial para analizar datos y encontrar las mejores opciones de locales.
    """)    
    st.subheader("▻ ¿Por qué elegirnos?")
    st.write("""
    Elegir la ubicación adecuada es clave para el éxito de cualquier empresa.
    En Gebmind analizamos datos demográficos, socioeconómicos y de competencia para ayudarte a tomar la mejor decisión.
    """)    
    st.subheader("▻ ¿Cómo te ayudamos?")
    st.write("""
    - **Análisis Demográfico:** Datos de población y nivel socioeconómico.
    - **Análisis de la Competencia:** Identifica negocios similares.
    - **Información de Locales:** Características, precios y fotos.
    """)

# --- Página de Recomendador IA ---
elif opcion == "Recomendador IA":
    st.title("Recomendador IA para nuevos negocios")

    # Cargar el dataset de referencia correcto
    df_reference_path = os.path.join(DATA_DIR, "locales_enriquecido_muestra.csv")
    df_reference = pd.read_csv(df_reference_path)

    # Cargar el modelo entrenado
    model_path = os.path.join(MODELS_DIR, "random_forest_model.pkl")
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    # Formulario de entrada
    nombre_cliente = st.text_input("Ingresa tu nombre o el nombre de tu empresa (opcional)")
    categoria_negocio = st.selectbox("Seleccione la categoría de negocio:", df_reference['categoria_negocio'].unique())
    codigo_postal = st.number_input("Ingrese el código postal:", min_value=28000, max_value=28055, step=1)

    if st.button("1️⃣ Generar recomendación"):
        # Filtrar datos de referencia por código postal
        df_cp = df_reference[df_reference['codigo_postal'] == codigo_postal]

        if not df_cp.empty:
            features = [
                'puntuacion_media', 'numero_reviews', 'categoria_id',
                'density_500m', 'density_1000m', 'density_2000m',
                'ratio_500m_2km', 'dist_city_center_km', 'local_density_1km',
                'dist_city_center_km^2', 'density_1000m^2',
                'valoracion_norm', 'valoracion_por_cercania',
                'competencia_count', 'competencia_rating'
            ]

            user_data = df_cp[features].mean().to_frame().T
            categoria_mode = df_cp[df_cp['categoria_negocio'] == categoria_negocio]['categoria_id'].mode()
            if not categoria_mode.empty:
                user_data['categoria_id'] = categoria_mode[0]
            else:
                user_data['categoria_id'] = df_cp['categoria_id'].mode()[0]

            # Predicción
            valoracion_predicha = model.predict(user_data)[0]
            valoracion_media_zona = df_cp['valoracion'].mean()
            competencia_count = df_cp['competencia_count'].mean()
            competencia_rating = df_cp['competencia_rating'].mean()

            # Guardar resultados en session_state
            st.session_state['valoracion_predicha'] = valoracion_predicha
            st.session_state['valoracion_media_zona'] = valoracion_media_zona
            st.session_state['competencia_count'] = competencia_count
            st.session_state['competencia_rating'] = competencia_rating
            st.session_state['codigo_postal'] = codigo_postal
            st.session_state['categoria_negocio'] = categoria_negocio
            st.session_state['nombre_cliente'] = nombre_cliente

            # Mostrar resultados
            st.success(f"La valoración esperada para un negocio de categoría '{categoria_negocio}' en el CP {codigo_postal} es: {valoracion_predicha:.2f}")
            fig, ax = plt.subplots()
            bars = ax.bar(['Predicción', 'Media Zona'], [valoracion_predicha, valoracion_media_zona], color=['green', 'gray'])
            ax.set_ylabel('Valoración')
            ax.set_title('Comparativa de Valoración')
            st.pyplot(fig)
            st.info(f"Nivel de competencia promedio en la zona: {competencia_count:.0f} locales similares con una media de {competencia_rating:.2f} estrellas.")
        else:
            st.warning("No hay datos suficientes para el código postal ingresado.")

    # Botón para descargar el informe PDF
    if 'valoracion_predicha' in st.session_state:
        if st.button("2️⃣ Generar informe PDF"):
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d")

            # Limpiar el nombre del cliente para el archivo
            nombre_cliente = st.session_state.get('nombre_cliente', '')
            nombre_cliente_limpio = nombre_cliente.strip().replace(" ", "_") if nombre_cliente else "SinNombre"

            output_filename = f"GEBMIND_CP{st.session_state['codigo_postal']}_{timestamp}_{nombre_cliente_limpio}.pdf"

            # Crear la carpeta "informes" si no existe
            os.makedirs(INFORMES_DIR, exist_ok=True)
            
            # Construir la ruta completa del archivo
            output_path = os.path.join(INFORMES_DIR, output_filename)

            # Crear el PDF
            c = canvas.Canvas(output_path, pagesize=letter)
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, 750, "Informe de recomendación GEBMIND")
            c.setFont("Helvetica", 12)
            c.drawString(50, 720, f"Código Postal: {st.session_state['codigo_postal']}")
            c.drawString(50, 700, f"Categoría de Negocio: {st.session_state['categoria_negocio']}")
            c.drawString(50, 680, f"Valoración esperada: {st.session_state['valoracion_predicha']:.2f}")
            c.drawString(50, 660, f"Media de la zona: {st.session_state['valoracion_media_zona']:.2f}")
            c.drawString(50, 640, f"Competencia promedio: {st.session_state['competencia_count']:.0f} locales similares")
            c.drawString(50, 620, f"Valoración media de competencia: {st.session_state['competencia_rating']:.2f} estrellas")
            c.save()
            
            # Leer el archivo para la descarga
            with open(output_path, "rb") as f:
                pdf_bytes = f.read()
            st.success("✅ Informe generado correctamente. ¡Ahora puedes descargarlo!")
            st.download_button(
                label="Descargar Informe PDF",
                data=pdf_bytes,
                file_name=output_filename,
                mime="application/pdf"
            )

# --- Página de Base de datos ---
elif opcion == "Base de datos":
    st.title("Explora nuestras base de datos")

    # Listar los CSV disponibles en la carpeta data
    csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]
    if not csv_files:
        st.warning("No hay archivos CSV disponibles en la carpeta de datos.")
    else:
        # Selector de archivo CSV en la barra lateral
        selected_csv = st.sidebar.selectbox("Selecciona el archivo CSV:", csv_files)

        # Cargar el archivo CSV seleccionado
        csv_path = os.path.join(DATA_DIR, selected_csv)
        df = pd.read_csv(csv_path)

        st.sidebar.subheader("Filtros de Búsqueda")

        # Filtro por Nombre (input de texto)
        nombre_filtro = st.sidebar.text_input("Nombre del local (parcial):", "")

        # Filtro por Categoría (desplegable)
        if 'categoria_negocio' in df.columns:
            categorias_disponibles = df["categoria_negocio"].dropna().unique()
            categoria_filtro = st.sidebar.selectbox("Categoría del negocio:", ["Todas"] + list(categorias_disponibles))
        else:
            categoria_filtro = "Todas"

        # Filtro por Código Postal (formato 5 dígitos)
        if 'codigo_postal' in df.columns:
            codigo_postal = st.sidebar.text_input("Código Postal (formato 5 dígitos):", "")
            if codigo_postal and not codigo_postal.isdigit():
                st.sidebar.warning("El Código Postal debe ser numérico.")
            elif codigo_postal and len(codigo_postal) != 5:
                st.sidebar.warning("El Código Postal debe tener 5 dígitos.")
        else:
            codigo_postal = ""

        # Filtro por puntuación_media
        if 'puntuacion_media' in df.columns:
            min_puntuacion = float(df['puntuacion_media'].min())
            max_puntuacion = float(df['puntuacion_media'].max())
            puntuacion_range = st.sidebar.slider(
                "Puntuación:",
                min_value=min_puntuacion,
                max_value=max_puntuacion,
                value=(min_puntuacion, max_puntuacion)
            )
        else:
            puntuacion_range = (0, 5)

        # Filtro por numero_reviews
        if 'numero_reviews' in df.columns:
            min_reviews = int(df['numero_reviews'].min())
            max_reviews = int(df['numero_reviews'].max())
            reviews_range = st.sidebar.slider(
                "Número de reviews:",
                min_value=min_reviews,
                max_value=max_reviews,
                value=(min_reviews, max_reviews)
            )
        else:
            reviews_range = (0, 100)

        # Filtrar DataFrame según criterios
        filtered_df = df.copy()

        # Filtrar por Nombre
        if nombre_filtro and 'nombre' in filtered_df.columns:
            filtered_df = filtered_df[filtered_df['nombre'].str.contains(nombre_filtro, case=False, na=False)]

        # Filtrar por Categoría
        if categoria_filtro != "Todas" and 'categoria_negocio' in filtered_df.columns:
            filtered_df = filtered_df[filtered_df['categoria_negocio'] == categoria_filtro]

        # Filtrar por Código Postal
        if codigo_postal and codigo_postal.isdigit() and len(codigo_postal) == 5 and 'codigo_postal' in filtered_df.columns:
            filtered_df = filtered_df[filtered_df['codigo_postal'] == int(codigo_postal)]

        # Filtrar por puntuación_media y numero_reviews
        if 'puntuacion_media' in filtered_df.columns and 'numero_reviews' in filtered_df.columns:
            filtered_df = filtered_df[
                (filtered_df['puntuacion_media'] >= puntuacion_range[0]) &
                (filtered_df['puntuacion_media'] <= puntuacion_range[1]) &
                (filtered_df['numero_reviews'] >= reviews_range[0]) &
                (filtered_df['numero_reviews'] <= reviews_range[1])
            ]

        # Seleccionar solo las columnas a mostrar
        columnas_mostrar = [col for col in [
            'nombre',
            'direccion',
            'codigo_postal',
            'puntuacion_media',
            'numero_reviews',
            'tipo_negocio',
            'categoria_negocio',
            'valoracion'
        ] if col in filtered_df.columns]

        filtered_df = filtered_df[columnas_mostrar]

        # Mostrar resultados
        st.dataframe(filtered_df)

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
    st.title("Resultados del Modelo Predictivo")

    # Mostrar reporte de clasificación (CSV)
    report_path = os.path.join(DATA_DIR, "classification_report.csv")
    if os.path.exists(report_path):
        st.success("Reporte de clasificación cargado correctamente.")
        report_df = pd.read_csv(report_path)
        st.dataframe(report_df)
    else:
        st.warning("Reporte de clasificación no disponible.")

    st.subheader("Visualizaciones del Modelo")

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
            col.warning(f"Imagen no encontrada: {img_name}")

# --- Página de Contacto ---
elif opcion == "Contacto":
    st.subheader("Formulario de Contacto")
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
            st.warning("Por favor, completa todos los campos.")

# --- Página de Quiénes Somos ---
elif opcion == "Quiénes Somos":
    st.subheader("Conoce a Gebmind")

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

        st.subheader("Información de Contacto")
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
Desarrollado por Gebmind © 2025  
""")