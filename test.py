f = open('links.json', 'r')
f = f.read().split('}')
import time
colum = 0
cont = 0
import re
for col in f:
    #print(col)
    #time.sleep(3)
    col = col.split(',')
    cont = cont +1
    print(col)
    print('-------------------------------')
    print()
    print()
        
    a = 12
    x = '' 
    #time.sleep(2)
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
            print('Link de download: ' +col[Collum][10:100].replace('"','').replace('\\',''))
            print(col[Collum+1][10:100].replace('"','').replace('\\',''))
            time.sleep(2)
            break
    
        
            
    
    #link
    
        
        
        
        
