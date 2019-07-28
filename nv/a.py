from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import wget

link = 'https://punchsubs.net/buscar-projeto/anime'
login = 'fuedgabriel'
password = 'fuedqe2902'
driver = webdriver.Chrome()

img =0
print('Login')
driver.get(link)
driver.find_element(By.XPATH, '//*[@id="login-form-toggle"]').click()
Login = driver.find_element_by_xpath('//*[@id="form-login"]/input[1]'); Login.send_keys(login)
Password = driver.find_element_by_xpath('//*[@id="form-login"]/input[2]'); Password.send_keys(password)
driver.find_element(By.XPATH, '//*[@id="form-login"]/input[3]').click()

driver.get('https://punchsubs.net/projeto/3169/chokotto-anime-kemono-friends-3')

id = driver.page_source
sopa = BeautifulSoup(id, 'html.parser')
test = sopa.find_all("img", class_='card-img-top rounded screen')
for clicks in test:
    
    img+=1
    driver.find_element(By.XPATH, '//*[@id="cards-episodios"]/ul[1]/li['+str(img)+']/div[1]/img').click()
    driver.find_element(By.XPATH, '//*[@id="nav-fullhd-tab"]').click()
    
    id = driver.page_source
    sopa = BeautifulSoup(id, 'html.parser')
    download = sopa.find_all("a", class_='link-mirror')
    f = 0
    for g in download:
        if('vip' in str(download[f]) and 'http:' in str(download[f])):
            print('Link verdadeiro')
            if(f == 0 or f == 7):
                print('muito grande')
            else:
                href = download[f].get('href')
                wget.download(href)
        else:
            pass
        f+=1
    driver.find_element(By.XPATH, '//*[@id="metodosDownloadModal"]/div/div/div[1]/button').click()
        
    

























