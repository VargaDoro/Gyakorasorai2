import random

'''Készíts függvényt mely az érmedobást szimulálja s legenerál 10 db fej vagy írástés az eredményt eltárolja
 egy listában. A függvény térjen vissza a listával.

 A továbbiakban ezzel a listával dolgozz az alábbi függvényekben:
 számold meg hány fej dobás van a listában'''

def tiz_ermedobas():
    elista=[]
    for i in range(0, 10, 1):
        dobas:int = int(random.random()*2+1)
        elista.append(dobas)

    return elista

def fej_dobas(elista):
    fej:int=0
    for i in range(0, len(elista), 1):
        if(elista[i]<2):
            fej+=1

    return fej


'''Készíts függvényt, mely a kockadobást szimulálja és legenerál 200bd véletlen kockadobást és az eredményt
eltároja egy listában. A függvény térjen vissza listával'''
def kockadobas():
    klista=[]
    for i in range(0, 200, 1):
        dobas:int = int(random.random()*6+1)
        klista.append(dobas)

    return klista

'''A továbbiakban ezze a listával dolgozz az alábbi függvényekben:
számold meg hányszor dobtunk egyest,kettest, ... hatost!'''

def szamolas(klista, szam):
    db:int=0
    for i in range(0, len(klista), 1):
        if(szam==klista[i]):
            db+=1

    return db

'''Készíts 'cinkelt' kockát! A hatost nagyobb valoszínűséggel dobja!
A cinkelt kockával is futtasd le a fenti függvényeidet! Kiderűl a csalás?'''

def cinkelt_kocka():
    clista=[]
    for i in range(0, 200, 1):
        ckocka:int = int(random.random()*8+1)
        if(6<ckocka):
            ckocka==6
            clista.append(ckocka)

    return clista