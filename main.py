import feladatok
import veletlenszamos_listak
lista=[12, 21,56, 32, -5, -23, 35]

print("1. feladat")
db:int=feladatok.poz_szamok_szama(lista)
print(f"A pozitív számok száma {db}")

print("2. feladat")
ossz:int=feladatok.negativszamok_osszege(lista)
print(f"A neatív számok összege {ossz}")

print("3. feladat")
atlag:float=feladatok.ottel_oszthato(lista)
print(f"A lista átlaga: {atlag}")

print("10 érmedobás")
elista=veletlenszamos_listak.tiz_ermedobas()
print(f"A dobások: {elista}")

print("Fej dobások")
fej=veletlenszamos_listak.fej_dobas(elista)
print(f"Ennyi fej dobás van {fej}")

print("Kockadobások")
klista=veletlenszamos_listak.kockadobas()
print(f"A dobások listája: {klista}")

print("Az egyesek száma")
db=veletlenszamos_listak.szamolas(klista, 1)
print(f"Az egyesek száma: {db}")

print("A kettesek száma")
db=veletlenszamos_listak.szamolas(klista, 2)
print(f"A kettesek száma: {db}")

print("A hármasok száma")
db=veletlenszamos_listak.szamolas(klista, 3)
print(f"A hármasok száma: {db}")

print("A ngyesek száma")
db=veletlenszamos_listak.szamolas(klista, 4)
print(f"A négyesek száma: {db}")

print("Az ötösök száma")
db=veletlenszamos_listak.szamolas(klista,5)
print(f"Az ötösök száma: {db}")

print("A hatosok száma")
db=veletlenszamos_listak.szamolas(klista, 6)
print(f"A hatosok száma: {db}")

print("A cinkelt dobások száma")
clista=veletlenszamos_listak.cinkelt_kocka()
print(f"A dobások: {clista}")