from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook 
import time

mail="novado9443@otozuz.com"

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("https://tibiachile.cl/")
driver.set_window_size(1024, 600)
driver.maximize_window()

time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/p/a").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form[2]/fieldset/div/p[3]/a").click()
correo= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form/fieldset/p[1]/input")
correo.clear()
correo.send_keys(mail)
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form/fieldset/p[2]/input").click()