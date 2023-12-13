import locale
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
driver = webdriver.Chrome()

fechas = []
pib_anual = []
var_pib_percent = []

url = "https://datosmacro.expansion.com/pib/ecuador"
driver.get(url)
contenido = driver.page_source

soup = BeautifulSoup(contenido, 'html.parser')
tabla_pib = soup.find('table')
filas = tabla_pib.find_all('tr')

# Iterar sobre las filas para extraer los datos
for fila in filas[1:]:
    columnas = fila.find_all('td')
    fechas.append(columnas[0].text.strip())
    pib_dolares = (columnas[2].text.strip().replace("\xa0M$", ""))
    pib_anual.append(f"{pib_dolares}M$")
    var_pib_percent.append(columnas[3].text.strip())

# Imprime los datos
print("Fechas:")
for fecha in fechas:
    print(fecha)
print("PIB Anual:")
for pib in pib_anual:
    print(pib)
print("Var. PIB %:")
for var_pib in var_pib_percent:
    print(var_pib)

# Crear un DataFrame de pandas
df = pd.DataFrame({
    'Fecha': fechas,
    'PIB Anual': pib_anual,
    'Var. PIB %': var_pib_percent
})

# Guardar el DataFrame en un archivo CSV
df.to_csv('PIB_anual_Ecuador.csv', index=False)
print("¡Felicidades! Archivo CSV 'PIB_anual_Ecuador.csv' generado exitosamente.")

# Cierra el navegador
driver.quit()


#***********INTEGRANTES******************
#   -------LEMA LEON SARA----------
#   ------MONCADA VERA GENESIS-----
#  ------SALAGA GUALPA DAMARIS-----
#   -----SELLAN QUIÑONEZ CRISTELL---

