#Librerias
from selenium import webdriver
#Para realizar operacion hasta que todos los elementos de html carguen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd

#Opciones de navegacion
options = webdriver.ChromeOptions()
#modo incognito
options.add_argument('--incognito')
#inicia maximizado
options.add_argument('--start-maximized')
#deshabilita extensiones
#options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\BARBARA\\Desktop\\AutomationSearchFlights\\chromedriver'

driver = webdriver.Chrome(driver_path, chrome_options=options)

#Inicia navegador
driver.get('https://www.google.com/flights?hl=es')