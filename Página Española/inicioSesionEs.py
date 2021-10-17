from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook 
import time

mail="novado9443@otozuz.com"
contra=["fgsdfsf","fsfdsjhks","fdsfjldfhsj","fsdjfdafkds","fkfdlsksalf","4982332942","fkdslfsldskf","fldksfksldkkl","54h3j543h54j3k","isjPHt4K"," 4kit44ki4"]

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")
driver.get("http://www.supersol.es/")
driver.set_window_size(1024, 600)
driver.maximize_window()

time.sleep(4)
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/a/em").click()


for i in contra:
    time.sleep(2)

    correo= driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/form/fieldset/div[1]/input")

    pssw= driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/form/fieldset/div[2]/input")
    correo.clear()
    correo.send_keys(mail)
    time.sleep(1)
    pssw.clear()
    pssw.send_keys(i)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/form/fieldset/div[3]/input").click()
    time.sleep(2)
    confirmar=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/a")
    if confirmar:
        confirmar.click()
        time.sleep(2)


