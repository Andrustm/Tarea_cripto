from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook 
import time

mail="novado9443@otozuz.com"
contra="1513939"
newpass="qawsedrftg"

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("http://www.supersol.es/")
driver.set_window_size(1024, 600)
driver.maximize_window()

time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/a/em").click()
time.sleep(2)
correo= driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/form/fieldset/div[1]/input")
correo.clear()
correo.send_keys(mail)
time.sleep(1)
pssw= driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/form/fieldset/div[2]/input")
pssw.clear()
pssw.send_keys(contra)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/form/fieldset/div[3]/input").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/form/fieldset/div[1]/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/form/fieldset/div[7]/div/div[1]/input").click()
time.sleep(1)
conact= driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/form/fieldset/div[9]/input")
conact.clear()
conact.send_keys(contra)
time.sleep(1)
newcon= driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/form/fieldset/div[10]/input")
newcon.clear()
newcon.send_keys(newpass)
time.sleep(1)
conf=driver.find_element_by_xpath("//html/body/div/div[2]/div[2]/div/div/form/fieldset/div[11]/input")
conf.clear()
conf.send_keys(newpass)
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/form/fieldset/div[13]/input").click()