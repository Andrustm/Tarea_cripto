from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook 
import time


nombre="fsdafdsa"
apellido="fdssdaas"
codigop="53075"
fechan="23111998"
mail="novado9443@otozuz.com"
contra="qawsedrftg"
conf="qawsedrftg"

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("http://www.supersol.es/")
driver.set_window_size(1024, 600)
driver.maximize_window()

time.sleep(4)

driver.find_element_by_class_name("btnRegistro").click()
time.sleep(1)

name= driver.find_element_by_name("nombre")
name.clear()
name.send_keys(nombre)
time.sleep(1)

lastname= driver.find_element_by_name("apellidos")
lastname.clear()
lastname.send_keys(apellido)
time.sleep(1)

code= driver.find_element_by_name("codigoPostal")
code.clear()
code.send_keys(codigop)
time.sleep(1)

date= driver.find_element_by_name("fechaNacimiento")

date.send_keys(Keys.CONTROL, 'a')
date.send_keys(fechan)
time.sleep(5)

correo= driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div/form/fieldset/fieldset[1]/div[5]/input")
correo.clear()
correo.send_keys(mail)
time.sleep(5)

pssw= driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div/form/fieldset/fieldset[1]/div[6]/input")
pssw.clear()
pssw.send_keys(contra)
time.sleep(1)

psswc= driver.find_element_by_name("passConfirmar")
psswc.clear()
psswc.send_keys(conf)
time.sleep(1)

driver.find_element_by_name("aceptoCondiciones").click()
time.sleep(1)
driver.find_element_by_name("recibirPromosEmail").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div/form/fieldset/fieldset[1]/div[10]/input").click()











