#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 10 maj 2015

@author: Patrickjusz
'''
# 0 miasto | 1 sektor | 2 kod | 3 wies | 4 powiat | 5 wojewodztwo | 6 ulica




import csv
import itertools
import operator
import hashlib

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

#
listaTmp = []
listaRekordow = []
with open('miasta.txt', 'rb') as csvfile:
    csv = csv.reader(csvfile, delimiter=';', quotechar='"')
    for rekord in csv:
        listaTmp.append(rekord[0])
        listaRekordow.append(rekord)
        
    tmp = most_common(listaTmp)
licznik = 0
for miasto in listaTmp:
    if (miasto == tmp):
        licznik = licznik + 1
print "Najczesciej wystepujaca wartość: " + tmp + " (" + str(licznik) + ")"
#


# wielkoscTablicy = raw_input("Podaj wielkość tablicy haszującej: ")
wielkoscTablicy = (licznik * 1.5)
wielkoscTablicy = int(wielkoscTablicy)
tablicaElementow = []
iloscElementowCsv = 0
maxPesymistyczna = 0
uzywaneElementy = 0

def funkcjaHaszujaca(wartosc):
    m = hashlib.md5()
    m.update(str(wartosc))
    md55 = m.hexdigest()
    wartosc=wartosc+md55
    ciag = 0
    for i in range(len(wartosc)):
        ciag += ord(wartosc[i])
    return ciag % wielkoscTablicy

def funkcjaInicjalizacji(wiadomosc):
    print wiadomosc
    
funkcjaInicjalizacji("[!] Czyszczenie tablicy [" + str(wielkoscTablicy) + "]...")
for i in range(wielkoscTablicy):
    tablicaElementow.insert(i, ["0", ])
    

funkcjaInicjalizacji("[!] Inicjalizacja tablicy...")
for rekord in listaRekordow:
    iloscElementowCsv += 1
    pozycjaHash = funkcjaHaszujaca(rekord[0])
        
    if (tablicaElementow[pozycjaHash] == ["0", ]):
        tablicaElementow[pozycjaHash] = []
        uzywaneElementy += 1
            
    tabTmp = tablicaElementow[pozycjaHash]
    tablicaElementow[pozycjaHash] = tablicaElementow[pozycjaHash] + [rekord, ]
        
    if (len(tablicaElementow[pozycjaHash]) > maxPesymistyczna):
        maxPesymistyczna = len(tablicaElementow[pozycjaHash])
  

def benchmark():  
    minOptymistyczna = maxPesymistyczna
    for element in tablicaElementow:
        if (len(element) < maxPesymistyczna):
            minOptymistyczna = len(element)
            
    print "\n----------------------------------------"       
    print "Suma załadowanych rekordów: \t" + str(iloscElementowCsv)  
    print "Wyszukiwanie pesymistyczne: \t" + str(maxPesymistyczna)
    print "Wyszukiwanie optymistyczne: \t" + str(minOptymistyczna)
    print "----------------------------------------"
    
    iloscDo250 = 0
    iloscDo500 = 0
    iloscDo1000 = 0
    iloscDo2000 = 0
    iloscDo3000 = 0
    iloscDo4000 = 0
    iloscPowyzej4000 = 0
    
    for element in range(wielkoscTablicy):
        wielkosc = len(tablicaElementow[element])
        if (wielkosc < 251):
            iloscDo250 += 1
            continue
        if (wielkosc < 501):
            iloscDo500 += 1
            continue
        if (wielkosc < 1001):
            iloscDo1000 += 1
            continue
        if (wielkosc < 2001):
            iloscDo2000 += 1
            continue
        if (wielkosc < 3001):
            iloscDo3000 += 1
            continue
        if (wielkosc < 4001):
            iloscDo4000 += 1
            continue
        if (wielkosc > 4000):
            iloscPowyzej4000 += 1
            continue
        
        
    print "Wielkość tablicy:\t\t" + str(uzywaneElementy) + "/" + str(wielkoscTablicy) 
    print "\n0-250 elementów:\t\t" + str(round(iloscDo250 / float(wielkoscTablicy) * 100, 2)) + " %"
    print "251-500 elementów:\t\t" + str(round(iloscDo500 / float(wielkoscTablicy) * 100, 2)) + " %"
    print "501-1000 elementów:\t\t" + str(round(iloscDo1000 / float(wielkoscTablicy) * 100, 2)) + " %"
    print "1001-2000 elementów:\t\t" + str(round(iloscDo2000 / float(wielkoscTablicy) * 100, 2)) + " %"
    print "2001-3000 elementów:\t\t" + str(round(iloscDo3000 / float(wielkoscTablicy) * 100, 2)) + " %"
    print "3000-4000 elementów:\t\t" + str(round(iloscDo4000 / float(wielkoscTablicy) * 100, 2)) + " %"
    print "4001+ elementów:\t\t" + str(round(iloscPowyzej4000 / float(wielkoscTablicy) * 100, 2)) + " %"
    print "----------------------------------------"


benchmark()
# 0 miasto | 1 sektor | 2 kod | 3 wies | 4 powiat | 5 wojewodztwo | 6 ulica

import Tkinter
import tkMessageBox
from Tkinter import *
top = Tkinter.Tk()
top.title("| Tablice mieszajace | @Patrickjusz")

text = Text()
E1 = Entry(top, bd =5)

def get(event):
    komenduj()
    E1.delete(0,END)
    
E1.bind('<Return>', get)
parametr = ""
def komenduj():       
    komenda = E1.get().encode("utf-8")
    
    #if (komenda == "-q"):
        #break
    
    if (komenda != "-b"):
        pozycjaHash = funkcjaHaszujaca(komenda)
        iloscWynikow = 0
        
        text.delete(1.0, END) 
        for i in tablicaElementow[pozycjaHash]:
            
            if (i[0] != komenda):
                continue
            iloscWynikow += 1
            
            if (i[0]):
                print "-> Miasto: " + i[0]
                text.insert(INSERT, i[0]+" | ")
            if (i[5]):
                print "Województwo: " + i[5]
                text.insert(INSERT, i[5]+" | ")
            if (i[1]):
                print "Sektor: " + i[1]
                text.insert(INSERT, i[1]+" | ")
            if (i[4]):
                print "Powiat: " + i[4]
                text.insert(INSERT, i[4]+" | ")
            if (i[3]):
                print "Dzielnica: " + i[3]
                text.insert(INSERT, i[3]+" | ")
            if (i[6]):
                print "Ulica: " + i[6]
                text.insert(INSERT, i[6]+" | ")
            if (i[2]):
                print "Kod: " + i[2]
                text.insert(INSERT, i[2]+" | ")
                
            print "\n" 
            text.insert(INSERT, "\n")
            
        print "-> Ilosc przeszukań: " + str(iloscWynikow) + "/" + str(len(tablicaElementow[pozycjaHash]))
    else:
        benchmark()



def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")


L1 = Label(top, text="Wpisz miasto:")
L1.pack( side = LEFT)


E1.pack(side = LEFT)
parametr="Katowice"
E1.focus()        

B = Tkinter.Button(top, text ="Wyszukaj", command = komenduj)
B.pack(side = LEFT)
text.pack(side = RIGHT)
top.mainloop()
