# 🌐 Web Corporativa GEBMIND

Aplicación web desarrollada con [Streamlit](https://streamlit.io/) para la presentación de información corporativa, contacto y visualización interactiva de locales en un mapa.

## 🚀 Funcionalidades

- Página de inicio con logotipo y descripción del producto.
- Formulario de contacto funcional.
- Información de la empresa y datos de contacto.
- Mapa interactivo con locales geolocalizados desde un archivo CSV.
- Filtros por tipo de negocio y puntuación media.

## 📂 Estructura del proyecto

```
web/
├── main.py                  # Archivo principal con toda la lógica de la aplicación
├── assets/
│   ├── logo.png             # Logotipo de la empresa
│   └── locales.csv          # Datos geolocalizados de negocios
├── requirements.txt         # Lista de dependencias
├── README.md                # Este archivo
```

## 📦 Requisitos

- Python 3.8 o superior
- pip

## 🛠️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/gebmind-web.git
cd gebmind-web
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución local

Lanza la aplicación desde terminal:

```bash
streamlit run main.py
```

Esto abrirá tu navegador por defecto en `http://localhost:8501`.

## 🗺️ Visualización en mapa

La sección de mapa permite visualizar los locales cargados desde `assets/locales.csv`, utilizando [Folium](https://python-visualization.github.io/folium/) con filtros interactivos por tipo de negocio y puntuación mínima.

## ✉️ Formulario de contacto

El formulario permite a los usuarios enviar mensajes. Puedes conectar el envío a un sistema SMTP o servicios como [FormSubmit](https://formsubmit.co/) para evitar el uso de contraseñas en código.

## 🌐 Despliegue (opcional)

Puedes desplegar esta app fácilmente en:

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Render](https://render.com/)
- [Railway](https://railway.app/)

## 📍 Ejemplo de mapa

![Ejemplo de mapa interactivo](assets/mapa_preview.png)  <!-- Reemplaza si tienes una imagen -->

## 🧑‍💻 Autor

**GEBMIND GeoBusiness**  
Desarrollado por el equipo de tecnología e innovación.

---

¿Quieres añadir integración con bases de datos o autenticación para usuarios? ¡Estamos listos para seguir creciendo! 🚀
