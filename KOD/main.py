import fnmatch
from datetime import datetime
import numpy as np

import re
import json
import matplotlib.pyplot as plt

woj_list = []
nop_list = []
zach_list = []
zach_dict_list = []
full_dictList = []
symptoms_dict = {'Zaczerwienienie i bolesność': 0, 'Gorączka': 0, 'Drgawki': 0, 'Wymioty': 0, 'Omdlenie': 0}
with open('../160221.json', 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)


class NOP(object):
    def __init__(self):
        self.date = ""
        # datetime.strptime(date, "%d.%m.%Y")
        self.wojewodztwo = ""
        self.powiat = ""
        self.plec = ""
        self.objawy = ""

    def EnterData(self, date, wojewodztwo, powiat, plec, objawy):
        self.date = date
        self.wojewodztwo = wojewodztwo
        self.powiat = powiat
        self.plec = plec
        self.objawy = objawy

    def getGender(self):
        self.plec
        return plec


i = 1
a = NOP()
L = []
kobiety=[]
mezczyzni=[]
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
    a = (id, date, wojewodztwo, powiat, plec, objawy)
    L.append(a)
    full_dictList.append(nop["DESCRIPTION"])
    woj_list.append(nop["VOIVODESHIP"])
    if nop["VOIVODESHIP"] == "zachodniopomorskie":
        zach_list.append(nop)
    if nop["GENDER"] == "M" or nop["GENDER"] == "m":
        mezczyzni.append(nop)
    if nop["GENDER"] == "K" or nop["GENDER"] == "k":
        kobiety.append(nop)
    if nop["VOIVODESHIP"] == "zachodniopomorskie":
        zach_dict_list.append(nop["DESCRIPTION"])

print(symptoms_dict)



lM = 0
# lista mezczyzn w NOP
for a in L:
    if (a.__contains__('M')):
        lM += 1

# lista kobiet w NOP
lK = 0
for a in L:
    if (a.__contains__('K')):
        # print(a)
        lK += 1
        # print(lK)

# zad 1
for a in L:
    print(a)
# zad 2
print(20 * "-")
print("\n Zadanie 2.1 \n Ile łącznie NOPów zostało wczytanych? ", len(L))
print(20 * "-")
print("\n Zadanie 2.2 \n Ile z nich dotyczy kobiet? ", lK)
print(20 * "-")
print("\n Zadanie 2.3 \n Ile z nich dotyczy mężczyzn? ", lM)
lPom = 0

# print("Zapis do pliku tekstowego")
f = open("../plik.txt", mode="r+")

for a in L:
    if (a.__contains__('pomorskie')):
        # print(a)
        lPom += 1
        f.write(str(a) + "\n")
# print(lPom)

f.close()

plik = open('../plik.txt')
try:
    tekst = plik.read()
finally:
    plik.close()

print(20 * '-')
x = (tekst.count("temp."))
y = (tekst.count("temperatu"))
z = (tekst.count("gorączka"))
lGor = x + y + z

print(" Zadanie 3.0\n Liczba osób, która w województwie pomorskim miała gorączkę: ", lGor)

f = open("../odpowiedzi.txt", mode="w")
f.write(
    "Zadanie 2.1\nIle łącznie NOPów zostało wczytanych?:  1950\nZadanie 2.2\nIle z nich dotyczy kobiet?:  1675\nZadanie 2.3\n Ile z nich dotyczy mężczyzn?:  265\nZadanie 3.0\n Liczba osób, która w województwie pomorskim miała gorączkę?:  8")
f.close()

# zad 4
print(20 * "-")
print(" Zadanie 4.0\nZestawienie województw: ")
print(woj_list)
pom = woj_list.count("pomorskie")
kujpom = woj_list.count("kujawsko-pomorskie")
lubel = woj_list.count("lubelskie")
lubu = woj_list.count("lubuskie")
maz = woj_list.count("mazowieckie")
malop = woj_list.count("małopolskie")
opo = woj_list.count("opolskie")
podka = woj_list.count("podkarpackie")
podla = woj_list.count("podlaskie")
warma = woj_list.count("warmińsko-mazurskie")
wlkp = woj_list.count("wielkopolskie")
zachpom = woj_list.count("zachodniopomorskie")
lodzkie = woj_list.count("łódzkie")
slaskie = woj_list.count("śląskie")
swieto = woj_list.count("świętokrzyskie")

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

print(20 * "-")
print("Zadanie 5:")
ind = 29
mod = 16
print("Wyznaczenie swojego województwa, nr indeksu to: ", 62929, "przez modulo: ", mod)
woj_ind = ind.__mod__(mod)
print("Numer województwa to:", woj_ind, "\nWytypowane wojewodztwo to: Zachodniopomorskie")
print("Dane dotyczące województwa zachodniopomorskiego: \n", zach_list)

print(20 * "-")

from collections import Counter

# print(Counter("this is a sent this is not a word".split()))
# Counter({"a": 2, "this": 2, "is": 2, "word": 1, "not": 1, "sent": 1})

print("Posortowane objawy według ilości wystąpień w woj. zachodniopomorskim: ")
# print(zach_dict_list)
# print(Counter(zach_dict_list).most_common(len(zach_dict_list)))
# utworzenie tablicy na posortowane według ilości wystąpień
posort_zach_list = []
posort_zach_list.append((Counter(zach_dict_list).most_common(len(zach_dict_list))))
# wyświetlenie zawartości nowej tablicy
print(posort_zach_list)
print("\nZapisuje wynik do pliku zachodniopomorskie.txt")
f = open("../zachodniopomorskie.txt", mode="w+")
f.write(str(posort_zach_list))
print("wykonano!")
f.close()

# Zad 5
print("Zadanie 5 \n Wykres kołowy z ilością osób, które doświadczyły NOP")
slices = [lK, lM]
descrLabel = ['Liczba Kobiet', 'Liczba Mężczyzn']
kolory = ['r', 'g']
plt.pie(slices, labels=descrLabel, colors=kolory, autopct="%.2f")
plt.title("Procent kobiet i mężczyzn, którzy doświadczyli NOP.\n")
plt.get_current_fig_manager().set_window_title('Zadanie 5. Wykres Kołowy')
plt.savefig('..\wykres_zadanie_6.png')
plt.show()

# zad 6
# print(full_dictList)
print( '----------Tworzenie kategorii NOP- dopasowywanie wyrażeń----------------')
podm_dictList = []
currentWord = "gorączka"
pozostale_nopy=[]
# define search string
#Drgawki
patternDrg = re.compile("[Dd]rgawki[.,]")
#Wymioty
patternWym = re.compile("[Ww]ymioty[.,]")
#Goraczka
patternGor = re.compile("[Gg]or[aą]czka")
patternTemp=re.compile("[Tt]emp[*]")
#Omglenie
patternOmdl = re.compile("[Oo]mdleni[ea]")
patternUtr=re.compile("[Uu]trata")
patternPrzyt=re.compile("[Pp]rzytomno[śs]ci")
#Zzaczerwienienie i krótkotrwała bolesność’

patternZacz = re.compile("[Zz]aczerwienieni[ea]")
patternBole = re.compile("[Bb]olesno[śs][ćc]")
pozostale=0
for nop in full_dictList:
    if patternGor.search(nop) or patternTemp.search(nop):
        #print ("%s DOPASOWANO DO KATEGORII GORĄCZKA " % nop)
        symptoms_dict['Gorączka']+=1
    elif patternDrg.search(nop):
        symptoms_dict['Drgawki'] +=1
        #print("%s DOPASOWANO DO KATEGORII DRGAWKI " % nop)
    elif patternWym.search(nop):
        symptoms_dict['Wymioty'] +=1
        #print("%s DOPASOWANO DO KATEGORII WYMIOTY " % nop)
    elif patternOmdl.search(nop) or patternUtr.search(nop) or patternPrzyt.search(nop):
        symptoms_dict['Omdlenie'] +=1
        #print("%s DOPASOWANO DO KATEGORII Omdlenia " % nop)
    elif patternZacz.search(nop) or patternBole.search(nop):
        #print("%s DOPASOWANO DO KATEGORII Zaczerwienienie i bolesność " % nop)
        symptoms_dict['Zaczerwienienie i bolesność'] +=1
    else:
        pozostale_nopy.append(nop)
        pozostale+=1
print("-=-Wypisanie kategorii i ilości wystąpień na liście NOP-=-\n",symptoms_dict) #wypisanie symptomów i ilości wystąpień
#print(pozostale_nopy)

#wykres
#wartości
zaczibol = symptoms_dict['Zaczerwienienie i bolesność']
gor = symptoms_dict['Gorączka']
drga = symptoms_dict['Drgawki']
wym = symptoms_dict['Wymioty']
omdl = symptoms_dict['Omdlenie']

print("                      Wartości: ",zaczibol,gor,drga,wym,omdl)
print("Pozostałe NOPY, nieprzypisane do rzadnej kategorii: ",(pozostale))
print("Suma powyższych: ",(zaczibol+gor+drga+wym+omdl+pozostale))
# print(zach_dict_list[::1])
# print(zach_dict_list[::-1]) #odwrócenie
# print(zach_dict_list[1:3]) #zakres
# Proszę przygotować wykres słupkowy, na którym ilościowo zostaną przedstawione wszystkie objawy wypisane w zadaniu 1
countries = ['Drgawki','Wymioty', 'Omdlenie','Gorączka', 'Zaczerwienienie i bolesność']
totalDeaths = [ drga,wym, omdl,gor, zaczibol]
plt.bar(countries, totalDeaths)
plt.title("Liczbowe przedstawienie danych z rozbiciem na kategorie NOP.\n\n")
plt.get_current_fig_manager().set_window_title('Zadanie 6. Wykres Słupkowy')
plt.ylabel('LICZBA PRZYPADKÓW',fontsize=12,color='red')
plt.xlabel('KATEGORIA OBJAWÓW',fontsize=12,color='purple')
plt.savefig('..\wykres_zadanie_7.png')
plt.show()
print(20*'-')
print("Zadanie 6-7 Wykresy")
#zadanie 8
#8 (1 pkt) Wykres liniowy z dwiema seriami:
#Proszę przygotować wykres liniowy, na którym będzie przestawiona zmiana ilości NOPów w
#czasie. Na osi X daty (dni), na osi Y ilość NOPów danego dnia. Wykres proszę przygotować z
#dwiema seriami – osobną dla mężczyzn, osobną dla kobiet. S
print(20*'-')
print("Zadanie 8")
print("Wykres liniowy z dwiema seriami")

print(len(kobiety))
import pylab as p
x = range(1, len(kobiety))
y = []
for i in x:
    y.append('X')
p.plot(x,y)
p.show()