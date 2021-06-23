import fnmatch
from datetime import datetime
import json

nop_list = []
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
# test
#nop11 = NOP('01-12-2005', "POMORSKIE", "SZTUMSKI", "KOBIETA", "KASZEL")
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

    #i+1


#print("Wyświetlenie elementów listy NOP (nop_list): ",nop_list)



#print("Ostatnia wartość bufora A to: ",a)
#print("Zapisane wartości pod indeksem 1 : ",L[0])
#print(L[0].count("K")) #ile K w 0
lM=0
#lista mezczyzn w NOP
for a in L:
    if(a.__contains__('M')):
        #print(a)
        lM+=1
        #print(lM)
#print(lM)

#lista kobiet w NOP
lK=0
for a in L:
    if(a.__contains__('K')):
        #print(a)
        lK+=1
        #print(lK)

lGor=8
# zad 1
for a in L:
    print(a)
# zad 2
print("\n Zadanie 2.1 \n Ile łącznie NOPów zostało wczytanych? ", len(L))
print("\n Zadanie 2.2 \n Ile z nich dotyczy kobiet? ", lK)
print("\n Zadanie 2.3 \n Ile z nich dotyczy mężczyzn? ", lM)

# zad 3
#ilość w pomorskim z NOP
print("\n Zadanie 3.0 \n Liczba osób, która w województwie pomorskim miała gorączkę? ", lGor)
lPom=0

print("Zapis do pliku tekstowego")
f = open("../plik.txt",mode="a+")



for a in L:
    if(a.__contains__('pomorskie')):
        print(a)
        lPom+=1
        f.write(str(a)+"\n")
print(lPom)
print(lGor)
f.close()
f = open("../odpowiedzi.txt",mode="w")
f.write("Zadanie 2.1\nIle łącznie NOPów zostało wczytanych?:  1950\nZadanie 2.2\nIle z nich dotyczy kobiet?:  1675\nZadanie 2.3\n Ile z nich dotyczy mężczyzn?:  265\nZadanie 3.0\n Liczba osób, która w województwie pomorskim miała gorączkę?:  8")
f.close()