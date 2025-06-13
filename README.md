# GEBMIND — Localización Inteligente para Negocios

Bienvenido a **GEBMIND**, una plataforma integral que te ayuda a encontrar el local perfecto para tu negocio utilizando Inteligencia Artificial y análisis de datos.

[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 Descripción del Proyecto

El proyecto combina **modelos predictivos**, **análisis de datos** y **visualizaciones interactivas** para ofrecer un análisis completo de la mejor ubicación comercial.

Incluye:
- 📊 Modelado predictivo con Random Forest (SMOTE y otros métodos)
- 📈 Gráficos y visualizaciones clave (Curva ROC, Importancia de Variables, etc.)
- 🗺️ Mapas interactivos de análisis de barrios y locales
- 💻 Interfaz web con **Streamlit** profesional y moderna

---

## Estructura del Proyecto

```
GEBMIND/
│
├── data/                  <- Datos de entrada y preprocesamiento
│   └── locales_procesado.csv
│
├── models/                <- Modelos entrenados y resultados
│   ├── rf_classifier.pkl
│   ├── classification_report.csv
│   └── feature_importance.png
│
├── assets/                <- Recursos de la aplicación Streamlit
│   ├── logo.png
│   ├── images/
│   │   └── gebmindteam.png
│   └── maps/
│       └── [mapas generados].html
│
├── notebooks/             <- Notebooks de modelado y análisis
│   ├── 01_get_data.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modelado.ipynb
│   └── 04_maps.ipynb
│
├── streamlit/
│   └── main.py            <- Aplicación principal en Streamlit
│
└── README.md              <- Este archivo
```

---

## Instrucciones de Uso

1. **Instalar dependencias** (preferiblemente en un entorno virtual):

```bash
conda create -n gebmind python=3.11
conda activate gebmind
pip install -r requirements.txt
```

2. **Ejecutar Notebooks** para procesamiento y modelado:

```bash
jupyter notebook
```

3. **Lanzar la aplicación Streamlit**:

```bash
cd streamlit
streamlit run main.py
```

4. **Abrir en el navegador**:
```
http://localhost:8501/
```

---

## Recomendaciones y Buenas Prácticas

**Carpetas organizadas** para evitar errores de rutas.  
**Modelos y reportes generados** se guardan en la carpeta `models/`.  
**Imágenes y mapas** organizados en `assets/images/` y `assets/maps/`.  
**Código limpio y comentado** en Notebooks y Streamlit para facilitar su mantenimiento.  
**Archivo .env o configuración de seguridad** (opcional) para manejar claves o accesos privados si es necesario.  

---

## Contacto

¿Tienes preguntas o sugerencias? ¡Contáctanos!  
- ✉️ **Correo**: gebmind@gmail.com
- 📍 **Ubicación**: Madrid, España
- 📞 **Teléfono**: +34 616 391 289

---

Desarrollado por **GEBMIND** © 2025
