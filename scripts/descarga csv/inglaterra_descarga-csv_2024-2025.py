import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# 👉 TUS CREDENCIALES PARA FOOTYSTATS
USERNAME = 'sebaGonzila'  
PASSWORD = '4247266'  

# 👉 CONFIGURACIÓN DE LA PREMIER LEAGUE 2024/2025
PREMIER_LEAGUE_ID = 12325  # ⚽ ID único de la Premier League 2024/2025

# 👉 CARPETA DONDE SE GUARDARÁN LOS ARCHIVOS CSV
download_path = r"C:\bartidata\bartidata-docs\data\inglaterra\2024_2025"

# 👉 CREAR LA CARPETA SI NO EXISTE
if not os.path.exists(download_path):
    os.makedirs(download_path)

# 👉 CONFIGURACIÓN DE CHROMEDRIVER
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_path,  # 📂 Descargas en esta carpeta
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
})

# 👉 INICIAR WEBDRIVER (Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://footystats.org/login')

# 👉 INICIO DE SESIÓN
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(USERNAME)
driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
driver.find_element(By.ID, 'register_account').submit()

# 👉 ESPERAR QUE SE COMPLETE EL LOGIN
time.sleep(5)

# 👉 URLs DE DESCARGA PARA PREMIER LEAGUE 2024/2025
csv_urls = [
    f'https://footystats.org/c-dl.php?type=league&comp={PREMIER_LEAGUE_ID}',   # Datos de la liga
    f'https://footystats.org/c-dl.php?type=teams&comp={PREMIER_LEAGUE_ID}',    # Datos de los equipos
    f'https://footystats.org/c-dl.php?type=players&comp={PREMIER_LEAGUE_ID}',  # Datos de los jugadores
    f'https://footystats.org/c-dl.php?type=matches&comp={PREMIER_LEAGUE_ID}'     # Datos de los partidos
]

# 👉 DESCARGA DE ARCHIVOS CSV
for url in csv_urls:
    driver.get(url)
    time.sleep(5)  # Espera para evitar bloqueos

# 👉 CERRAR EL NAVEGADOR
driver.quit()

print(f"✅ Descarga completada. Archivos guardados en: {download_path}")
