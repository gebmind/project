
# GEBMIND Data Pipeline

Este repositorio contiene el flujo completo de trabajo para la obtención, procesamiento, modelado y visualización de datos del sector HORECA en Madrid.

## Estructura del Proyecto

- **01_get_data.ipynb**: Obtención de datos generales (barrios, códigos postales y coordenadas).
- **01_get_data_HORECA.ipynb**: Extracción de datos específicos de locales de restauración mediante la API de Google Places.
- **02_preprocessing.ipynb**: Limpieza, categorización y preparación de datos.
- **03_modelling.ipynb**: Entrenamiento de modelos predictivos para clasificación de negocios.
- **04_maps.ipynb**: Visualización interactiva de resultados en mapas.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/gebmind.git
   cd gebmind
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta los notebooks en el siguiente orden:
1. 01_get_data.ipynb
2. 01_get_data_HORECA.ipynb
3. 02_preprocessing.ipynb
4. 03_modelling.ipynb
5. 04_maps.ipynb

## Tecnologías

- Python 3.8+
- Pandas, NumPy
- Scikit-learn
- Folium, Geopandas
- Matplotlib

## Contribución

¡Las contribuciones son bienvenidas! Abre un issue o envía un pull request.

## Licencia

Este proyecto está licenciado bajo la MIT License.

---

*Desarrollado por GEBMIND.*
