import pandas as pd
from sodapy import Socrata
from selenium import webdriver
#from selenium.webdriver.support.ui import Select

# Links file
links = pd.read_excel('..\Inputs\enlaces.xlsx', engine='openpyxl')


# Chrome path to web scraping
chrome_path = r"C:\Users\kmili\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)


# Download data: Fiscal - Tasa cupon cero
tasa_cupon_cero = links.loc[19, 'Fuente']
driver.get(tasa_cupon_cero)

driver.find_element_by_xpath("//*[@id='saw_766908_3']/option[text()='tableView!3']").click()

