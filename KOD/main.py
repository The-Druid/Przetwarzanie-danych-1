import fnmatch
from datetime import datetime
import numpy as np
import json
import matplotlib.pyplot as plt
woj_list = []
nop_list = []
zach_list=[]
zach_dict_list=[]
full_dictList=[]
with open('../160221.json', 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)


class NOP(object):
    def __init__(self):
        self.date = ""
        #datetime.strptime(date, "%d.%m.%Y")
        self.wojewodztwo = ""
        self.powiat = ""
        self.plec = ""
        self.objawy = ""

    def EnterData(self,date, wojewodztwo, powiat, plec, objawy):
        self.date=date
        self.wojewodztwo=wojewodztwo
        self.powiat=powiat
        self.plec=plec
        self.objawy=objawy
    def getGender(self):
        self.plec
        return plec

i=1
a=NOP()
L=[]
for nop in data['NOP']:
   # print(nop["ID"])
    id = nop["ID"]
   # print(nop["DATE"])
    date = nop["DATE"]
   # print(nop["VOIVODESHIP"])
    wojewodztwo = nop["VOIVODESHIP"]
   # print(nop["REGION"])
    powiat = nop["REGION"]
   # print(nop["GENDER"])
    plec = nop["GENDER"]
   # print(nop["DESCRIPTION"])
    objawy = nop["DESCRIPTION"]
    nop_list.append(nop)
    a=(id,date,wojewodztwo,powiat,plec,objawy)
    L.append(a)
    full_dictList.append(nop["DESCRIPTION"])
    woj_list.append(nop["VOIVODESHIP"])
    if nop["VOIVODESHIP"]=="zachodniopomorskie":
        zach_list.append(nop)
    if nop["VOIVODESHIP"]=="zachodniopomorskie":
        zach_dict_list.append(nop["DESCRIPTION"])

lM=0
#lista mezczyzn w NOP
for a in L:
    if(a.__contains__('M')):
        lM+=1


#lista kobiet w NOP
lK=0
for a in L:
    if(a.__contains__('K')):
        #print(a)
        lK+=1
        #print(lK)


# zad 1
for a in L:
    print(a)
# zad 2
print(20*"-")
print("\n Zadanie 2.1 \n Ile łącznie NOPów zostało wczytanych? ", len(L))
print(20*"-")
print("\n Zadanie 2.2 \n Ile z nich dotyczy kobiet? ", lK)
print(20*"-")
print("\n Zadanie 2.3 \n Ile z nich dotyczy mężczyzn? ", lM)
lPom=0

#print("Zapis do pliku tekstowego")
f = open("../plik.txt",mode="r+")

for a in L:
    if(a.__contains__('pomorskie')):
        #print(a)
        lPom+=1
        f.write(str(a)+"\n")
#print(lPom)

f.close()

plik = open('../plik.txt')
try:
	tekst = plik.read()
finally:
	plik.close()

print(20*'-')
x=(tekst.count("temp."))
y=(tekst.count("temperatu"))
z=(tekst.count("gorączka"))
lGor=x+y+z
print(" Zadanie 3.0\n Liczba osób, która w województwie pomorskim miała gorączkę: ",lGor)

f = open("../odpowiedzi.txt",mode="w")
f.write("Zadanie 2.1\nIle łącznie NOPów zostało wczytanych?:  1950\nZadanie 2.2\nIle z nich dotyczy kobiet?:  1675\nZadanie 2.3\n Ile z nich dotyczy mężczyzn?:  265\nZadanie 3.0\n Liczba osób, która w województwie pomorskim miała gorączkę?:  8")
f.close()

#zad 4
print(20*"-")
print(" Zadanie 4.0\nZestawienie województw: ")
print(woj_list)
pom=woj_list.count("pomorskie")
kujpom=woj_list.count("kujawsko-pomorskie")
lubel=woj_list.count("lubelskie")
lubu=woj_list.count("lubuskie")
maz=woj_list.count("mazowieckie")
malop=woj_list.count("małopolskie")
opo=woj_list.count("opolskie")
podka=woj_list.count("podkarpackie")
podla=woj_list.count("podlaskie")
warma=woj_list.count("warmińsko-mazurskie")
wlkp=woj_list.count("wielkopolskie")
zachpom=woj_list.count("zachodniopomorskie")
lodzkie=woj_list.count("łódzkie")
slaskie=woj_list.count("śląskie")
swieto=woj_list.count("świętokrzyskie")


print("Kujawsko-Pomorskie: ", kujpom)
print("Lubelskie", lubel)
print("Lubuskie: ", lubu)
print("Mazowieckie: ", maz)
print("Małopolskie: ", malop)
print("Opolskie: ", opo)
print("Podkarpackie: ", podka)
print("Podlaskie: ", podla)
print("Warmińsko-Mazurskie: ", warma)
print("Wielkopolskie: ", wlkp)
print("Zachodniopomorskie: ", zachpom)
print("Łódzkie: ", lodzkie)
print("Śląskie: ", slaskie)
print("Świętokrzyskie: ", swieto)

print(20*"-")
print("Zadanie 5:")
ind=29
mod=16
print("Wyznaczenie swojego województwa, nr indeksu to: ",62929,"przez modulo: ",mod)
woj_ind=ind.__mod__(mod)
print("Numer województwa to:",woj_ind, "\nWytypowane wojewodztwo to: Zachodniopomorskie")
print("Dane dotyczące województwa zachodniopomorskiego: \n",zach_list)

print(20*"-")

from collections import Counter
#print(Counter("this is a sent this is not a word".split()))
#Counter({"a": 2, "this": 2, "is": 2, "word": 1, "not": 1, "sent": 1})

print("Posortowane objawy według ilości wystąpień w woj. zachodniopomorskim: ")
#print(zach_dict_list)
#print(Counter(zach_dict_list).most_common(len(zach_dict_list)))
#utworzenie tablicy na posortowane według ilości wystąpień
posort_zach_list=[]
posort_zach_list.append((Counter(zach_dict_list).most_common(len(zach_dict_list))))
#wyświetlenie zawartości nowej tablicy
print(posort_zach_list)
print("\nZapisuje wynik do pliku zachodniopomorskie.txt")
f = open("../zachodniopomorskie.txt",mode="w+")
f.write(str(posort_zach_list))
print("wykonano!")
f.close()


#Zad 5
print("Zadanie 5 \n Wykres kołowy z ilością osób, które doświadczyły NOP")
slices = [lK,lM]
descrLabel = ['Liczba Kobiet','Liczba Mężczyzn']
kolory=['r','g']
plt.pie(slices,labels = descrLabel,colors=kolory,autopct="%.2f")
plt.title("Procent kobiet i mężczyzn, którzy doświadczyli NOP.\n")
plt.get_current_fig_manager().set_window_title('Zadanie 5. Wykres Kołowy')
plt.show()


#zad 6

#zły trop
#print(full_dictList)
print(20*'--')
posortFull_dictList=[]
posortFull_dictList.append((Counter(full_dictList).most_common(len(full_dictList))))
print(posortFull_dictList)


#trzeba będzie utworzyć nową liste, zawierającą liste objawów (edytowaną) . wedle konwencji "Zaczerwienienie i bolesność" => ‘zaczerwienienie i krótkotrwała bolesność
#użyje funkcji .decode lub .replace

podm_dictList=[]
