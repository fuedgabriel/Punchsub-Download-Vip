from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
#login
login = 'fuedgabriel'
password = 'fuedqe2902'
link = 'https://punchsubs.net/buscar-projeto/anime'

#Contadores


#abrir lista de animes
f = open('links.json', 'r')
f = f.read().split('}')

driver = webdriver.Chrome()



def Login():
    print('Login')
    driver.get(link)
    driver.find_element(By.XPATH, '//*[@id="login-form-toggle"]').click()
    Login = driver.find_element_by_xpath('//*[@id="form-login"]/input[1]'); Login.send_keys(login)
    Password = driver.find_element_by_xpath('//*[@id="form-login"]/input[2]'); Password.send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="form-login"]/input[3]').click()
    AllAnimeSolo()

    
def AllAnimeSolo():
    colum = 0
    cont = 0
    #CApturando vetor
    for col in f:
        col = col.split(',')
        #cont = cont +1
        a = 12
        x = '' 

        #nome
        while('"' not in x):
            x = col[1][11:a]
            a+=1


        print('Nome do anime: '+x)    
        #numero de episodeos
        resp = re.compile('[0-9]+').findall(col[2])
        resp = resp[0]
        print('Número de episodeos: '+ str(resp))

    
        for Collum in range(20):
            if('link' in col[Collum]):
                print('Link de download: ' + col[Collum][10:100].replace('"','').replace('\\',''))
                print('Link de Imagem: '+ col[Collum+1][10:100].replace('"','').replace('\\',''))
                time.sleep(2)
                link = 'https://punchsubs.net/'+col[Collum][10:100].replace('"','').replace('\\','')
                driver.get(link)
                break
        
    
    
    

 

Login()





