# Proyecto Final de Máster - Análisis de Locales de Madrid 🏙️

---

## 🚀 Descripción

Este proyecto tiene como objetivo principal analizar y clasificar locales de Madrid (restauración, hoteles, comercio) mediante:

✅ Extracción de datos desde la API de Google Maps y otras fuentes.  
✅ Preprocesamiento de datos (normalización, clustering, feature engineering).  
✅ Modelado predictivo con Random Forest para clasificar las valoraciones.  
✅ Visualización interactiva de resultados y mapas.

El resultado final se presenta como una **página web profesional** con:
- Secciones de introducción y explicación del proyecto.
- Descarga de datos CSV.
- Visualizaciones de resultados y gráficas.
- Mapas interactivos con Leaflet.js y Folium.
- Formulario de contacto para preguntas y sugerencias.

---

## 📂 Estructura del proyecto

```
mi_proyecto_web/
│
├── index.html
├── css/
│   └── styles.css
├── js/
│   └── maps.js
├── images/
│   └── gebmind_logo.png
├── maps/
│   ├── mapa_barrios_restauracion.html
│   ├── mapa_predicciones_modelo.html
│   ├── mapa_valoracion_colormap.html
│   ├── ...
├── data/
│   ├── locales.csv
│   ├── locales_restauracion.csv
│   ├── locales_procesado.csv
│   └── barrios.geojson (opcional)
```

---

## 📊 Datos

Los datos procesados se encuentran en la carpeta `/data/`, listos para descargar:
- `locales.csv` — Todos los locales de interés en Madrid.
- `locales_restauracion.csv` — Locales de restauración filtrados.
- `locales_procesado.csv` — Datos procesados con variables enriquecidas y normalizadas.

---

## 🗺️ Mapas

Los mapas interactivos se encuentran en la carpeta `/maps/`. Incluyen:
- Mapa por barrios de restauración.
- Mapa de predicciones del modelo.
- Mapa de valoración con colormap.
- Mapa de densidad de locales.
- (Opcional) Capa de barrios en formato GeoJSON exportado desde `.shp`.

---

## 🛠️ Requisitos y ejecución local

### Requisitos
- Python 3.x (para servidor local)
- (Opcional) GDAL para convertir archivos `.shp` a `.geojson`

### Ejecución local
```bash
# Desde la carpeta raíz del proyecto:
python -m http.server 8000
```

Abre tu navegador en:  
```
http://localhost:8000
```

---

## 🗂️ Conversión de shapefile a GeoJSON

Si necesitas convertir el shapefile `BARRIOS.shp` a GeoJSON para usarlo en Leaflet:
```bash
ogr2ogr -f GeoJSON barrios.geojson BARRIOS.shp
```
⚠️ Asegúrate de tener todos los archivos `.shp`, `.shx`, `.dbf`, `.prj` en la misma carpeta antes de ejecutar el comando.

---

## 📬 Contacto

Puedes contactarnos a través del formulario de contacto en la página o enviando un correo electrónico a: [gebmind@gmail.com)](mailto:gebmind@gmail.com).

---

¡Esperamos que este proyecto te resulte útil y disfrutes explorando los resultados! 🚀
