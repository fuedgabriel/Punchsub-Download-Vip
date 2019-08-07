import os
import time
import re
try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install bs4')
    from bs4 import BeautifulSoup
try:
    from urllib.request import urlopen
except:
    os.system('pip install urlopen urllib')
    from urllib.request import urlopen
    import urllib.request
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except:
    os.system('pip install selenium')


import wget
#login
login = ''
password = ''
link = 'https://punchsubs.net/buscar-projeto/anime'

#Contadores
'''
import wget

print('Beginning file download with wget module')

url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
wget.download(url, '/Users/scott/Downloads/cat4.jpg')
'''

driver = webdriver.Chrome()
def Download(Direct, Worker, Name, FullHdSd, Ep):
    try:
        urllib.request.urlretrieve(Direct)
    except:
        print('Anime download erro: '+ str(Name))
        print('"uality: '+ str(FullHdSd))
        print('Episodeo: '+ str(Ep))
        
        
    


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
        name = '' 

        #nome
        while('"' not in name):
            name = col[1][11:a]
            a+=1
        print('Nome do anime: '+name)
        
        #numero de episodeos
        resp = re.compile('[0-9]+').findall(col[2])
        resp = resp[0]
        print('Número de episodeos: '+ str(resp))


    
        for Collum in range(20):
            try:
                
                if('link' in col[Collum]):
                    try:
                    
                        #pegar link de download, imagem e abrir o link do anime
                        link = 'https://punchsubs.net/'+col[Collum][10:1000].replace('"','').replace('\\','')
                        print('Link de download: ' + link)
                        print('Link de Imagem: '+ col[Collum+1][10:1000].replace('"','').replace('\\',''))
                        
                        #abrir link do anime
                        #https://punchsubs.net/projeto/2539/alice-or-alice-siscon-niisan-to-futago-no-imouto
                        driver.get(str(link))
                    except:
                        print('Erro na captura de link')
                        print('')
                    
                    id = driver.page_source
                    sopa = BeautifulSoup(id, 'html.parser')
                    
                
                    #break

                    #capturar link por link
                    episodes = 0
                    test = sopa.find_all("img", class_='card-img-top rounded screen')
            except:
                pass

                for clicks in test:
                    episodes+=1
                    images = str(clicks).split(' ')
                    images = images[7].replace('src="','').replace('"/>','')
                    if('https://' not in images):
                        images = 'https://punchsubs.net'+images
                    print('link das imagens dos episodeos: '+ str(images))
                    print()
                    print()
                    try:
                        
                        driver.find_element(By.XPATH, '//*[@id="cards-episodios"]/ul[1]/li['+str(episodes)+']/div[1]/img').click()
                        time.sleep(0.5)
                        driver.find_element(By.XPATH, '//*[@id="nav-sd-tab"]').click()
                    except:
                        print('Erro provavelmente finalizou os download de episódios de um anime.')
                        print('numeros baixados: '+str(episodes))
                        AllAnimeSolo()
                    
                    id = driver.page_source
                    sopa = BeautifulSoup(id, 'html.parser')
                    download = sopa.find_all("a", class_='link-mirror')
                    f = 0
                    for g in download:
                        if('vip' in str(download[f]) and 'http:' in str(download[f])):
                            print('Link verdadeiro')
                            if(f == 0 or f == 7):
                                print('muito grande')
                                print(str(f))
                                
                            else:
                                print('efetuando download')
                                href = download[f].get('href')
                                #wget.download(href)
                                Download(href, 1, name, 'SD', int(resp)-int(episodes)+1)
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





