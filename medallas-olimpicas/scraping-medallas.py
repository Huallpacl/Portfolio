# scraping-medallas.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os
import re

# Configuración inicial del driver
def iniciar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecuta sin abrir ventana
    chrome_options.add_argument("--disable-gpu")
    service = Service()  # Usará el chromedriver ya instalado
    return webdriver.Chrome(service=service, options=chrome_options)

# Crear carpeta data si no existe
os.makedirs("medallas-olimpicas/data", exist_ok=True)

# URL objetivo
URL = "https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table"

# Función para limpiar nombres de países
def limpiar_pais(nombre):
    nombre = re.sub(r"\[.*?\]", "", nombre)  # elimina [ ... ]
    nombre = re.sub(r"\(.*?\)", "", nombre)  # elimina ( ... )
    return nombre.strip()

# Extraer tabla de Wikipedia
def extraer_medallero(driver):
    driver.get(URL)
    time.sleep(3)  # Esperar carga de página

    tabla = driver.find_element(By.CLASS_NAME, "wikitable")
    filas = tabla.find_elements(By.TAG_NAME, "tr")

    datos = []
    for fila in filas[1:]:  # Saltar encabezado
        columnas = fila.find_elements(By.TAG_NAME, "td")
        if len(columnas) >= 6:
            pais = limpiar_pais(columnas[0].text.strip())
            participacion = columnas[1].text.strip()
            oro = columnas[2].text.strip()
            plata = columnas[3].text.strip()
            bronce = columnas[4].text.strip()
            total = columnas[5].text.strip()
            datos.append([pais, participacion, oro, plata, bronce, total])

    df = pd.DataFrame(datos, columns=["País", "Participaciones", "Oro", "Plata", "Bronce", "Total"])
    return df

# Guardar CSV
def guardar_csv(df):
    ruta_salida = "medallas-olimpicas/data/medallas.csv"
    df.to_csv(ruta_salida, index=False)
    print(f"Archivo guardado en {ruta_salida}")

# Main
if __name__ == "__main__":
    driver = iniciar_driver()
    df_medallas = extraer_medallero(driver)
    driver.quit()
    guardar_csv(df_medallas)
