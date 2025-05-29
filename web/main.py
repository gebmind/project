import streamlit as st
from PIL import Image

# Configuración general
st.set_page_config(page_title="Gebmind", page_icon="🌐", layout="centered")

# Sidebar con navegación manual

st.sidebar.image("assets/logo.png", width=100)
st.sidebar.title("Navegación")
opcion = st.sidebar.radio("", ("Inicio", "Mapa de Locales", "Contacto", "Quiénes Somos"))

# --- Página de Inicio ---
if opcion == "Inicio":
    st.title("Bienvenido a nuestra web")

    image = Image.open("assets/logo.png")
    st.image(image, width=200)

    st.subheader("Nuestro producto")
    st.write("""
    Ofrecemos soluciones innovadoras para facilitar la transformación digital de tu negocio.
    Nos centramos en calidad, eficiencia y soporte personalizado.
    """)

# --- Página de Mapa de Locales ---
elif opcion == "Mapa de Locales":
    import folium
    from streamlit_folium import st_folium
    import pandas as pd

    st.subheader("Mapa interactivo")

    # Cargar datos
    df = pd.read_csv("assets/locales.csv")
    df['puntuacion_media'] = df['puntuacion_media'].fillna(0)
    df['numero_reviews'] = df['numero_reviews'].fillna(0).astype(int)

    # Filtros avanzados
    tipos = df['tipo_negocio'].dropna().unique().tolist()
    tipo_seleccionado = st.sidebar.multiselect("Tipo de negocio", tipos)

    puntuacion_range = st.sidebar.slider(
        "Puntuación media",
        min_value=0.0,
        max_value=5.0,
        value=(3.0, 5.0),
        step=0.1
    )

    reviews_range = st.sidebar.slider(
        "Número de reviews",
        min_value=0,
        max_value=120000,
        value=(200, 4000),
        step=100
    )

    # Aplicar filtros
    df_filtrado = df[
        (df['tipo_negocio'].isin(tipo_seleccionado)) &
        (df['puntuacion_media'].between(*puntuacion_range)) &
        (df['numero_reviews'].between(*reviews_range))
    ]

    # Crear mapa
    mapa = folium.Map(location=[40.4167, -3.7033], zoom_start=14)
    folium.TileLayer('cartodb positron').add_to(mapa)

    for _, row in df_filtrado.iterrows():
        popup_text = f"""
        <b>{row['nombre']}</b><br>
        Dirección: {row['direccion']}<br>
        Puntuación: {row['puntuacion_media']}<br>
        Reviews: {row['numero_reviews']}<br>
        Tipo: {row['tipo_negocio']}
        """
        folium.Marker(
            location=[row['latitud'], row['longitud']],
            popup=popup_text,
            tooltip=row['nombre'],
            icon=folium.Icon(icon="building", prefix="fa", color="blue")
        ).add_to(mapa)

    st_folium(mapa, width=700, height=500)

# --- Página de Contacto ---
elif opcion == "Contacto":
    st.subheader("Formulario de Contacto")

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
    st.subheader("Quiénes Somos")
    st.write(""" Somos un equipo apasionado por la tecnología y la aplicacion de la IA para el ahorro y mejora de los
             sistemas actuales empresariales.

    - **Empresa**:      GEBMIND S.L.
    - **Descripción**:  Proveedor de soluciones tecnológicas y consultoría.
    - **Dirección**:    Madrid, España
    - **Correo**:       gebmind@gmail.com
    - **Teléfono**:     +34 616 391 289
    """)