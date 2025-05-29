
# 🧠 GEBMIND · Localización Inteligente de Negocios

Este repositorio contiene un proyecto de análisis de datos y machine learning orientado a la **localización óptima de negocios en Madrid**. Combinamos datos públicos, APIs geoespaciales y modelos predictivos para ofrecer una herramienta que identifica las mejores zonas según densidad, valoración y contexto competitivo.

---

## 📁 Estructura del Proyecto

| Notebook                     | Descripción |
|-----------------------------|-------------|
| `01_get_data_HORECA.ipynb`  | Extracción masiva de **establecimientos de restauración** en Madrid utilizando la API de Google Places. Incluye gestión de paginación, palabras clave específicas y exportación a CSV. |
| `01_get_data.ipynb`         | Versión genérica para extracción de distintos tipos de negocios, adaptable a cualquier categoría o área. |
| `02_preprocessing.ipynb`    | Limpieza y categorización de los datos, creación de nuevas variables (densidad, distancia al centro, normalización de valoraciones) y exportación final del dataset procesado. |
| `03_modeling.ipynb`         | Entrenamiento de un modelo **Random Forest** para predecir la calidad de localización de cada negocio según sus características. Incluye importancia de variables y métricas de evaluación. |
| `04_maps.ipynb`             | Visualización geoespacial interactiva con **Folium**. Se muestran los negocios clasificados por nivel de predicción en un mapa de Madrid. |

---

## 🔧 Tecnologías Utilizadas

- **Python** · Pandas, Scikit-learn, Folium, GeoPandas
- **Google Maps API** · Extracción por código postal y palabras clave
- **Machine Learning** · Clasificación con Random Forest
- **Visualización** · Mapas interactivos y análisis exploratorio

---

## 🚀 Objetivo del Proyecto

📍 Localizar de forma automática las mejores zonas para abrir un negocio mediante:

- Análisis de densidad y competencia
- Clasificación por valoración y reviews
- Modelos de predicción basados en datos históricos
- Visualización dinámica e interpretativa

---

## 📊 Ejemplo de Variables Clave

- `dist_city_center_km`: Distancia al centro de Madrid
- `density_1000m`: Densidad de negocios similares en 1 km
- `valoracion_norm`: Valoración normalizada
- `cluster_zone`: Segmentación por zonas homogéneas

---

## 🧭 Resultados Esperados

- Dataset procesado listo para modelado
- Mapa visual con predicción por localización
- Recomendaciones por zona y categoría de negocio

---

## 📌 Cómo Empezar

1. Crea tu entorno con Conda o venv.
2. Añade tu clave de Google Maps API en un archivo `.env`.
3. Ejecuta los notebooks en orden numérico (01 → 04).

---

## 📬 Contacto

¿Tienes dudas o quieres colaborar?  
[GitHub](https://github.com/gebmind)

---