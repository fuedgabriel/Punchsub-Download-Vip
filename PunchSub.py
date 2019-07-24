from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import json
login = 'fuedgabriel'
password = 'fuedqe2902'
link = 'https://punchsubs.net/buscar-projeto/anime'

driver = webdriver.Chrome()

def Login():
    print('Login')
    driver.get(link)
    driver.find_element(By.XPATH, '//*[@id="login-form-toggle"]').click()
    Login = driver.find_element_by_xpath('//*[@id="form-login"]/input[1]'); Login.send_keys(login)
    Password = driver.find_element_by_xpath('//*[@id="form-login"]/input[2]'); Password.send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="form-login"]/input[3]').click()
    GetLinks()

    
def GetLinks():
    pass    
    
    
    



Login()


driver.get(link)
ids = driver.page_source
f = open('novo-arquivo.txt', 'r')
lista = f.split('{')


lista[1]


