from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import wget
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
    cja = 0
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
                driver.get('https://punchsubs.net/projeto/2525/aico-incarnation')
                id = driver.page_source
                sopa = BeautifulSoup(id, 'html.parser')
                cja+=1
                print()
                print()
                print()
                print(cja)
                print()
                print()
                print()
                #break
                img = 0
                test = sopa.find_all("img", class_='card-img-top rounded screen')

                for clicks in test:
                    img+=1
                    print(clicks)
                    
                    driver.find_element(By.XPATH, '//*[@id="cards-episodios"]/ul[1]/li['+str(img)+']/div[1]/img').click()
                    
                    driver.find_element(By.XPATH, '//*[@id="nav-fullhd-tab"]').click()
                    
                    id = driver.page_source
                    sopa = BeautifulSoup(id, 'html.parser')
                    download = sopa.find_all("a", class_='link-mirror')
                    f = 0
                    for g in download:
                        if('vip' in download[f]):
                            print('Link verdadeiro')
                            href = download[f].get('href')
                            wget.download(href)
                        else:
                            pass
                        f+=1
                    driver.find_element(By.XPATH, '//*[@id="metodosDownloadModal"]/div/div/div[1]/button').click()
                    
                    
                    
                    '''
                    driver.find_element(By.XPATH, '//*[@id="nav-hd-tab"]').click()
                    id = driver.page_source
                    sopa = BeautifulSoup(id, 'html.parser')
                    zip_link = sopa.find_all("a", class_='link-mirror')
                    zip = zip_link[0].get('href')
                    wget.download(zip)
                    
                    driver.find_element(By.XPATH, '//*[@id="nav-sd-tab"]').click()
                    id = driver.page_source
                    sopa = BeautifulSoup(id, 'html.parser')
                    zip_link = sopa.find_all("a", class_='link-mirror')
                    zip = zip_link[0].get('href')
                    wget.download(zip)
                    '''
                    
                    
                

        
    
    
    

 

Login()





