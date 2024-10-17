import feladatok
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