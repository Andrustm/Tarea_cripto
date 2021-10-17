from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook 
import time

mail="novado9443@otozuz.com"

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("http://www.supersol.es/")
driver.set_window_size(1024, 600)
driver.maximize_window()

time.sleep(4)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/a/em").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/form/fieldset/div[4]/a").click()
time.sleep(2)
correo= driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/input")
correo.clear()
correo.send_keys(mail)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/span/em/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/a").click()