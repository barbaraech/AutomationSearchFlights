#Librerias
from selenium import webdriver
#Para realizar operacion hasta que todos los elementos de html carguen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

#Click en ida/vuelta
#en 5 seg si no encuentra elemento se detiene programa
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    'button.VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-Bz112c-UbuQg VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe LQeN7 BobFtf'.replace(' ','.'))))\
        .click()