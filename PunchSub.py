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
    #abrir lista de animes
    f = open('links.json', 'r')
    f = f.read().split('}')
    
    #Capturando vetor
    for col in f:
        col = col.split(',')
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
                #pegar link de download, imagem e abrir o link do anime
                link = 'https://punchsubs.net/'+col[Collum][10:100].replace('"','').replace('\\','')
                print('Link de download: ' + link)
                print('Link de Imagem: '+ col[Collum+1][10:1000].replace('"','').replace('\\',''))

                
                #abrir link do anime
                driver.get('https://punchsubs.net/projeto/2525/aico-incarnation')
                id = driver.page_source
                sopa = BeautifulSoup(id, 'html.parser')
                print()
                print()
                print()
                print()
                print()
                
                #break

                #capturar link por link
                img = 0
                test = sopa.find_all("img", class_='card-img-top rounded screen')

                for clicks in test:
                    img+=1
                    print('link das imagens dos episodeos: '+ str(clicks))
                    print()
                    print()
                    
                    driver.find_element(By.XPATH, '//*[@id="cards-episodios"]/ul[1]/li['+str(img)+']/div[1]/img').click()
                    time.sleep(0.5)
                    driver.find_element(By.XPATH, '//*[@id="nav-sd-tab"]').click()
                    
                    id = driver.page_source
                    sopa = BeautifulSoup(id, 'html.parser')
                    download = sopa.find_all("a", class_='link-mirror')
                    f = 0
                    for g in download:
                        if('vip' in str(download[f]) and 'http:' in str(download[f])):
                            print()
                            print('Link verdadeiro')
                            if(f == 0 or f == 7):
                                print('muito grande')
                                print(str(f))
                                print()
                            else:
                                print('efetuando download')
                                href = download[f].get('href')
                                wget.download(href)
                        else:
                            print()
                            print('falso')
                            print()
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





