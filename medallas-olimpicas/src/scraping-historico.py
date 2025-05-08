from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os

# Configuración inicial del driver
def iniciar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    service = Service()
    return webdriver.Chrome(service=service, options=chrome_options)

# Crear carpeta data si no existe
os.makedirs("medallas-olimpicas/data", exist_ok=True)

# Lista de años válidos (excluye años cancelados)
anos_olimpiadas = [1896, 1900, 1904, 1908, 1912,
                   1920, 1924, 1928, 1932, 1936,
                   1948, 1952, 1956, 1960, 1964,
                   1968, 1972, 1976, 1980, 1984,
                   1988, 1992, 1996, 2000, 2004,
                   2008, 2012, 2016, 2020, 2024]

# Generar las URLs correspondientes
urls_medalleros = [f"https://en.wikipedia.org/wiki/{ano}_Summer_Olympics_medal_table" for ano in anos_olimpiadas]

# Extraer medallas por año desde la tabla principal
def extraer_medallas_por_ano(driver, url, ano):
    driver.get(url)
    time.sleep(3)

    try:
        tablas = driver.find_elements(By.CLASS_NAME, "wikitable")
        tabla = None
        for t in tablas:
            headers = t.find_elements(By.TAG_NAME, "th")
            header_texts = [h.text.lower() for h in headers]
            if any("nation" in h or "noc" in h for h in header_texts):
                tabla = t
                break

        if tabla is None:
            print(f"No se encontró tabla en {ano}")
            return []

        filas = tabla.find_elements(By.TAG_NAME, "tr")[1:]
        medallas = []

        for fila in filas:
            columnas_th = fila.find_elements(By.TAG_NAME, "th")
            columnas_td = fila.find_elements(By.TAG_NAME, "td")

            if columnas_th and columnas_td and len(columnas_td) >= 5:
                try:
                    link = columnas_th[0].find_element(By.TAG_NAME, "a")
                    pais = link.text.strip()
                except:
                    pais = columnas_th[0].text.strip()

                oro = columnas_td[1].text.strip()
                plata = columnas_td[2].text.strip()
                bronce = columnas_td[3].text.strip()
                total = columnas_td[4].text.strip()
                medallas.append([ano, pais, oro, plata, bronce, total])

        # Mostrar ejemplo
        if medallas:
            print(f"Primeras filas extraídas de {ano}:")
            for fila in medallas[:3]:
                print(fila)

        return medallas
    except Exception as e:
        print(f"Error en {url}: {e}")
        return []

# Guardar CSV
def guardar_csv(df, nombre_archivo):
    ruta_salida = os.path.join("medallas-olimpicas", "data", nombre_archivo)
    df.to_csv(ruta_salida, index=False)
    print(f"Archivo guardado en {ruta_salida}")

# MAIN
if __name__ == "__main__":
    driver = iniciar_driver()
    datos_historicos = []

    for ano, url in zip(anos_olimpiadas, urls_medalleros):
        print(f"\nExtrayendo medallero de {ano}")
        medallas = extraer_medallas_por_ano(driver, url, ano)
        if medallas:
            datos_historicos.extend(medallas)

    driver.quit()

    # Crear DataFrame y guardar
    df = pd.DataFrame(datos_historicos, columns=["Año", "País", "Oro", "Plata", "Bronce", "Total"])
    guardar_csv(df, "medallas_historicas.csv")
