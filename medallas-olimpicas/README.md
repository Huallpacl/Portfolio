# Análisis de Medallas Olímpicas

Este proyecto explora los datos históricos de medallas obtenidas por los países en los Juegos Olímpicos (edición verano). Utiliza scraping, limpieza de datos y análisis visual para descubrir patrones, tendencias y comparaciones significativas.

## 📋 Consideraciones Iniciales

- Solo se consideran registros de países con al menos una medalla en un evento olímpico de verano.
- Rusia, el Imperio Ruso y la URSS se incluyen dentro del continente Europeo, en línea con su tratamiento histórico.
- Los datos cubren desde las primeras ediciones modernas (1896) hasta la actualidad (2024), con medallas clasificadas en oro, plata, bronce y total.

## 🛠 WorkFlow

## 1. Recopilación de datos:
-Se utilizó "Selenium" para realizar web scrapping de diferentes tablas históricas de medalleros olímpicos de verano (fuente: Wikipedia (EN))
- El scraping automatizado extrajo datos de medallas por país y edición.
- Los datos fueron guardados en archivos csv para su posterior análisis.

## 📁 Estructura del Proyecto

```
medallas-olimpicas/
│
├── data/ # Datos utilizados en los análisis
│ ├── medallas_historicas.csv
│ └── pais_continente.csv
│
├── notebooks/ # Notebooks Jupyter con los análisis
│ ├── analisis-medallas.ipynb # Análisis general
│ ├── analisis_top10.ipynb # Top 10 países históricos
│ └── analisis-medallas-historicas.ipynb # Bonus de frecuencia y ranking
│
├── images/ # Visualizaciones exportadas (PNG)
│ └── frecuencia_en_top10.png
│
├── src/ # Scripts (scraping y preparación)
│
└── README.md
```
## ✨ Análisis Realizados

- **Análisis General de Medallas:** evolución de las medallas totales por año y país.
- **Top 10 Países Históricos:** identificación de los países con más medallas en distintos años.


## 📊 Visualizaciones Destacadas

Las imágenes generadas en los análisis están guardadas en la carpeta `/images` para que puedan verse directamente en el repositorio.

- ![Apariciones en top 10 de paises más frecuentes](images/top10_apariciones.png)

## ⚙️ Tecnologías Usadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebooks

## 🚀 Cómo usar este repositorio

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/medallas-olimpicas.git
   cd medallas-olimpicas
2. Abrir las notebooks en Jupyter o VS Code.

3. Ejecutar las celdas para ver y generar los gráficos.   