
# 🌐 Web Corporativa GEBMIND

Aplicación web desarrollada con [Streamlit](https://streamlit.io/) para la presentación de resultados de modelos predictivos, contacto corporativo y visualización interactiva de locales en un mapa.

## Funcionalidades principales

- Página de inicio con logotipo y presentación del producto.
- Visualización de resultados de modelos predictivos (reportes y gráficos generados).
- Visualización de mapas interactivos de locales con filtros por categorías y puntuaciones.
- Formulario de contacto funcional.
- Información de la empresa y valores.

## Estructura del proyecto

```
gebmind/
├── streamlit/
│   ├── main.py                  # Archivo principal de Streamlit con toda la lógica
│   └── assets/
│       ├── logo.png             # Logotipo de la empresa
│       ├── gebmindteam.png      # Imagen del equipo
│       ├── images/              # Imágenes generadas por el modelo (gráficos)
│       ├── maps/                # Mapas HTML generados
│       └── data/                # CSVs y archivos de datos
├── models/
│   ├── rf_classifier_smote.pkl  # Modelo Random Forest con SMOTE
│   └── classification_report.csv # Reporte de clasificación exportado
├── requirements.txt             # Lista de dependencias
├── README.md                    # Este archivo
```

## Requisitos

- Python 3.10 o superior
- pip
- Navegador web moderno

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/gebmind.git
cd gebmind/streamlit
```

2. Instala las dependencias:

```bash
pip install -r ../requirements.txt
```

## Ejecución local

Ejecuta la aplicación desde la carpeta `streamlit`:

```bash
streamlit run main.py
```

Esto abrirá automáticamente el navegador en `http://localhost:8501`.

## Visualización de mapas

La sección de mapas permite visualizar locales y datos de negocio cargados desde los archivos CSV en `assets/data/`, usando [Folium](https://python-visualization.github.io/folium/). Cada mapa incluye leyendas y filtros relevantes para una toma de decisiones informada.

## Visualización de resultados del modelo

La app muestra reportes de clasificación (`classification_report.csv`) y gráficos de importancia de variables y curvas ROC, generados y almacenados en la carpeta `models/` y `assets/images/`.

## Formulario de contacto

El formulario permite a los usuarios enviar mensajes. Puedes integrar el envío con un servidor SMTP externo o usar servicios como [FormSubmit](https://formsubmit.co/) para gestionar los correos electrónicos.

## Información de contacto

En la sección **Quiénes Somos** se muestra información clave de la empresa, incluyendo la imagen del equipo (`gebmindteam.png`).

## Despliegue (opcional)

Puedes desplegar esta app en:

- [Streamlit Community Cloud](https://streamlit.io/cloud)
- [Render](https://render.com/)
- [Railway](https://railway.app/)

## Autor

**GEBMIND GeoBusiness**  
Desarrollado por el equipo de Tecnología e Innovación.

---

¿Quieres añadir autenticación de usuarios o bases de datos? ¡Estamos listos para crecer juntos! 🚀
