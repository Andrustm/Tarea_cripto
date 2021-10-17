from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook 
import time

mail="novado9443@otozuz.com"
contra="isjPHt4K"
newpass="qawsedrftg"

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("https://tibiachile.cl/")
driver.set_window_size(1024, 600)
driver.maximize_window()

time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/p/a").click()
time.sleep(1)
correo= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form[2]/fieldset/div/p[1]/span/input")
correo.clear()
correo.send_keys(mail)
time.sleep(1)

pssw= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form[2]/fieldset/div/p[2]/span/input")
pssw.clear()
pssw.send_keys(contra)
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form[2]/fieldset/div/p[4]/input[2]").click()
time.sleep(2)

driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/ul/li[3]/a").click()
time.sleep(2)
pssw2=driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form/fieldset/p[5]/input")
pssw2.clear()
pssw2.send_keys(contra)
time.sleep(1)
new= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form/fieldset/p[6]/input")
new.clear()
new.send_keys(newpass)
time.sleep(1)
conf= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form/fieldset/p[7]/input")
conf.clear()
conf.send_keys(newpass)
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form/fieldset/p[9]/input").click()