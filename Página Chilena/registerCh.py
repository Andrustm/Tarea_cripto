from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook 
import time


nombre="fsdafdsa"
apellido="fdssdaas"
codigop="53075"
fechan="23111998"
mail="digav87538@settags.com"
contra="hjkfdhgkjdhgkjfdghkdjghfjkghj"


driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("https://tibiachile.cl/")
driver.set_window_size(1024, 600)
driver.maximize_window()

time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/p/a").click()
time.sleep(3)

correo= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form[1]/fieldset/div/p[2]/span/input")
correo.clear()
correo.send_keys(mail)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form[1]/fieldset/div/p[3]/input[2]").click()
time.sleep(3)

ortesia=driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/form/fieldset[1]/p[1]/input[1]").click()
time.sleep(1)

name= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/form/fieldset[1]/p[2]/input")
name.clear()
name.send_keys(nombre)
time.sleep(1)

lastname= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/form/fieldset[1]/p[3]/input")
lastname.clear()
lastname.send_keys(apellido)
time.sleep(1)


pssw= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/form/fieldset[1]/p[5]/input")
pssw.clear()
pssw.send_keys(contra)
time.sleep(1)

fecha1=driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/form/fieldset[1]/p[6]/select[1]/option[24]")
fecha1.click()

time.sleep(1)

fecha1=driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/form/fieldset[1]/p[6]/select[2]/option[12]")
fecha1.click()
time.sleep(1)

fecha1=driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/form/fieldset[1]/p[6]/select[3]/option[25]")
fecha1.click()
time.sleep(1)

driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/form/fieldset[1]/p[7]/input").click()
time.sleep(1)

driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/form/fieldset[1]/p[8]/input").click()
time.sleep(1)

driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/form/p/input[4]").click()









