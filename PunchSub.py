import os
import time
import re
import platform
try:
    from bs4 import BeautifulSoup
except:
    print('Library is missing "bs4" and "BeautifulSoup"')
    print('installing library')
    os.system('pip install bs4')
    from bs4 import BeautifulSoup
try:
    from urllib.request import urlopen
    import urllib.request
except:
    print('Library is missing "urlopen", "urllib" and "request"')
    print('installing library')
    os.system('pip install urlopen urllib')
    from urllib.request import urlopen
    import urllib.request
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except:
    print('Library is missing "Selenium"')
    print('installing library')
    os.system('pip install selenium')



#login
login = ''
password = ''
link = 'https://punchsubs.net/buscar-projeto/anime'

                

        
def wget(URL, Name, Episode):
    
    if(str(platform.system()) == 'Linux'):
        print('-__________________iniciando wget__________________-')
        Name = Name.replace('/','\\') + '_' + Episode
        print(Name)
        print('wget -c -O "Animes/' + Name + '" "' + URL + '"')
        print('mkdir "Animes/' + Name + '"')
        input()
        a = os.popen('mkdir "Animes/' + Name + '"').read()
        print('wget -c --tries=50 -O "Animes/' + Name + '" -U \'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4\' ' + URL)
        a = os.popen('wget -c -O "Animes/' + Name + '" "' + URL + '"').read()
        print(a)
        input()
        #wget -c --tries=50  -O "Animes/.hack\\\\Quantum_1"  -U 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4' http://cdn-direct-feral1.punchsubs.net/anime/b/battery/sd/PUNCH_Battery_-_10_SD.mp4\?st\=KRyHHUm0XAx0eZrcu9VF_w\&time\=1566062480

        
    if (platform.system() == 'Windows'):
        os.popen('wget.exe '+url)
    else:
        print('Não testados em outros sistemas operacionas, altere no código')
        
        

#selenium navegator
driver = webdriver.Chrome()

def Login():
    print('Login')
    driver.get(link)
    driver.find_element(By.XPATH, '//*[@id="login-form-toggle"]').click()
    Login = driver.find_element_by_xpath('//*[@id="form-login"]/input[1]'); Login.send_keys(login)
    Password = driver.find_element_by_xpath('//*[@id="form-login"]/input[2]'); Password.send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="form-login"]/input[3]').click()


def ReaderAnimes(Cont, f):
    col = f[Cont]
    print(col)
    #for col in f:
    col = col.split(',')
    #print(col)
    a = 12
    NameOFAnime = ''
    while('"' not in NameOFAnime):
        NameOFAnime = col[1][11:a]
        a+=1
    print('Anime name:                '+NameOFAnime.replace('"',''))
    #numero de episodeos
    NumberEpisodes = re.compile('[0-9]+').findall(col[2])
    NumberEpisodes = NumberEpisodes[0]
    print('Number of episodes:        '+ str(NumberEpisodes))
    for Collum in range(20):
        if('link' in col[Collum]):
            LinkDownAnime = 'https://punchsubs.net/'+col[Collum][10:1000].replace('"','').replace('\\','')
            LinkDownImage = col[Collum+1][10:1000].replace('"','').replace('\\','')
            print('Download link:             '+LinkDownAnime)
            print('Anime icon:                '+LinkDownImage)
            print('__________________________________________________________________________________________')
            #time.sleep(2)
            return (str(LinkDownAnime), str(LinkDownImage), str(NameOFAnime.replace('"','')), str(NumberEpisodes), str(Cont)) 
            #break


def OpenSite(Link, NameAnime, Episodes):
    driver.get('https://punchsubs.net/projeto/3054/boku-no-hero-academia-all-might-rising-the-animation')
    id = driver.page_source
    sopa = BeautifulSoup(id, 'html.parser')
    #capturar link por link
    episodes = 0
    Icon = sopa.find_all("img", class_='card-img-top rounded screen')
    for click in Icon:

        episodes+=1

        images = str(click).split(' ')
        images = images[7].replace('src="','').replace('"/>','')

        if('https://' not in images):
            images = 'https://punchsubs.net'+images
        try:            
            driver.find_element(By.XPATH, '//*[@id="cards-episodios"]/ul[1]/li['+str(episodes)+']/div[1]/img').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="nav-sd-tab"]').click()

        except:
            print('Erro Ao clicar no icon')
            print('Number episode erro:      '+str(episodes))
            print('Anime name:               '+ NameAnime)
            print('Total episodes:           '+ Episodes)

        id = driver.page_source
        sopa = BeautifulSoup(id, 'html.parser')
        download = sopa.find_all("a", class_='link-mirror')
        f=0
        for g in download:
            if('vip' in str(download[f]) and 'http:' in str(download[f])):
                print('Link verdadeiro')
                var = str(download[f]).split(' ')
                for split in var:
                    if('href=' in split):
                        href = str(split).replace('href="', '').replace('"', '')
                        break
                    else:
                        pass
                if(f == 0 or f == 7):
                    print('muito grande')
                    print(str(f))
                else:
                    print('efetuando download')
                    #href = str(download[f]).get('href')
                    #wget.download(href)
                    wget(str(href), str(NameAnime), str(episodes))
                    #Download(href, 1, name, 'SD', int(resp)-int(episodes)+1)
            else:
                pass
            f+=1
        driver.find_element(By.XPATH, '//*[@id="metodosDownloadModal"]/div/div/div[1]/button').click()


        
        '''
        
        for g in download:
            print(download[f])
            print('_________________________________________________________________')
            if('vip' in str(download[f]) and 'http:' in str(download[f])):
                #print(download[f])
                
                if('fullhd' in str(download[f]) or 'FullHD' in str(download[f])):
                        print('efetuando download FullHd')
                        #href = download[f].get('href')
                        #Download(href, 1, name, 'FullHd', int(resp)-int(episodes)+1)
                        print('FullHd')
                if('hd' in str(download[f]) or 'HD' in str(download[f])):
                        print('efetuando download HD')
                        #href = download[f].get('href')
                        #Download(href, 1, name, 'HD', int(resp)-int(episodes)+1)
                        print('Hd')
                        
                print('Link: '+str(download[f]))
                if('sd' in str(download[f]) or 'SD' in str(download[f])):
                        print('efetuando download SD')
                        href = str(download[f]).get('href')
                        #Download(href, 1, name, 'SD', int(resp)-int(episodes)+1)
                        print(href)
                        wget(str(href), NameAnime, episodes)
                else:
                        pass
                f+=1
        '''
        



            
        #print('link das imagens dos episodeos: '+ str(images))
        #print()
        
    

    
#Open arq
f = open('links.json', 'r')
f = f.read().split('}')
x = 3760
Login()
for x in range(3768):
    print(x)
    LinkDown, LinkImage, NameAnime, Episodes, Number = ReaderAnimes(x, f)
    print(LinkDown)
    OpenSite(LinkDown, NameAnime, Episodes)
    #print(LinkDown, LinkImage, NameAnime, Episodes, Number)


