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
driver.get('https://www.latamairlines.com/cl/es')

#Click en ida/vuelta
#en 5 seg si no encuentra elemento se detiene programa
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID,
    'btnTripTypeCTA')))\
        .click()

#Click en ida/vuelta
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID,
    'btnTripType0')))\
        .click()

#Click en Ingresa Origen
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID,
    'txtInputOrigin_field')))\
        .click()

#escribe en Ingresa Origen
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    'input#txtInputOrigin_field')))\
    .send_keys('Santiago de Chile, SCL - Chile')

#click en origen escrito
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID,
    'btnItemAutoComplete_0')))\
        .click()

#click en Ingresa Destino
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID,
    'txtInputDestination_field')))\
        .click()

#escribe en Ingresa Destino
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    'input#txtInputOrigin_field')))\
    .send_keys('Auckland, AKl - Nueva Zelandia')

#click en Destino
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID,
    'btnItemAutoComplete_0')))\
        .click()

