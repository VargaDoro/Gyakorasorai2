#Adott egy lista lista=[12, 21,56 32, -5, -23, 35] az alábbi metódusok paraméterenként kapják a fenti listát.
#1. Hány pozitív szám van benne?
#2. Mennyi a negatív számok összege?
#3. Mennyi az 5-et osztható számok átlaga?

def poz_szamok_szama(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        '''print(lista[i])'''
        if(lista[i]>0):
            db+=1
        i+=1

    return db

def negativszamok_osszege(lista):
    i:int=0
    ossz:int=0
    while(i<len(lista)):
        if(lista[i]<0):
            ossz+=lista[i]
        i+=1

    return ossz

def ottel_oszthato(lista):
    i:int=0
    db:int=0
    osszeg:int=0
    while(i<len(lista)):
        if(lista[i]%5==0):
            db+=1
            osszeg+=lista[i]
        i+=1
    atlag=osszeg/db 
    return atlag       