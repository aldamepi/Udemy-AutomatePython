#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 15:03:38 2022

@author: albertomengual
"""
import random, sys
import pyperclip as ppc
 


ord('a') # retorna el codigo unicode de un carácter
chr(98) # retorna el caracter de un código unicode
chr(1114111)
chr(115)
ord('ñ')




# Tuples are immutable data types

familia = ('mama','papa','hermano','hermana','perrito','abuelita') # tupla () inmutable
len(familia)
min(familia)
max(familia)
familia.count('perrito')





# Lists are mutable data types

lf = list(familia) # lista [] mutable
list(enumerate(familia,start=1))

lf.index('g') # indica la primera ocurrencia
              # se le puede indicar desde y hasta donde buscar
lf.index('perrito') # only the first coincidence
familia[0].index('m',1)
lf[4].index('t',3,4) # Error, hasta el último sin incluirlo

lf.append(['abuelito', 'spam']) # agrega UN valor completo
lf.insert(1,'papa') #
lf.extend(['gatito','bacon']) # !!! la diferencia entre append y extend:
                              # extend agrega los valores un iterable

# Metodos nuevos en la 3.3:
lf.clear() # elimina todos los elementos de la lista
lf.copy() # crea una copia superficial de la lista con distinto id 
          # ¿sublistas? -> referencias    



lf.remove('abuelito') # only the first coincidence in case of duplicates

lf.pop(1) # retorna y elimina el elmento del índice

lf.reverse() #
list(reversed(lf[2])) # reversed() retorna un iterador
lf.sort() #
lf.sort(reverse=True) #
sorted(lf[0]) #

del lf[6:len(lf)+1] #
lf




# Strings are immutable sequence data types of single character strings

cadena = ', '.join(familia) #crea una cadena de un iterable
cadena.index('papa')
cadena[6]
cadena[6:10]
cadena[6:10:2]
'xxx' in cadena
cadena.index(',',6)

# Modify a string:
cadena2 = cadena[:6] + 'mama' +  cadena[10:]


cadena.title()
cadena.upper()
cadena.lower()
cadena.count('a')
cadena.replace('a','i',4)






def monoV(nv): # sustituye la vocales de la cadena por el argumento
    vocales = ('a','e','i','o','u')
    c2 = cadena
    for v in vocales:
        c2 = c2.replace(v,nv)
    print(c2)



sum(range(101)) # suma cada uno de los valores en una sequencia
', '.join(familia)





# vocal = 'i'

# for elem in lf:
#     print(elem)
#     if vocal in elem:
#         print('Eliminar: ' + elem)
#         lf.remove(elem)
# print('Hecho!')  # ¿pot qué no borra abuelita? Porque al borrar un elemento
                 # de la lista cambia el indice de los siguientes elementos.
                 # Hay que eliminarlos ¿¿todos a la vez?? o por orden inverso.
        

# idxd = []  ## No consigo eliminarlos varios a la vez
# elemd = []
# for c, elem in enumerate(lf):
#     print(elem)
#     if vocal in elem:
#         print('Eliminar: ' + elem)
#         elemd.append(elem)
#         #idxd.append(c)
        
# #idxd = [str(i) for i in idxd] # comprension de listas
# ## idxd = list(map(str, l)) # funcion map
# #del lf[slice(idxd)]
# lf.remove(elemd)
# print('Hecho!')  

    
tuple([cadena])

type(familia)
type(lf)
type(cadena)



##########
# map() # ver ejemplo junto a comprension de listas - 
        # ???? Como se define una función para poder aplicarla con un map
        # se puede meter un metodo a un map??
        
        # supongo que tiene que ser aplicable a un elemento y tener return value

###########

def quitprogram():
    print('Hello')
    sys.exit()
    print('Goodbye')
    
random.randint(1,10)


ppc.copy('Hello world!')
ppc.paste()


vocal = 'i'

def eliminaSiVocal():
    for elem in reversed(lf):
        print(elem)
        if vocal in elem:
            print('Eliminar: ' + elem)
            lf.remove(elem)
    print('Hecho!')


def eSV(vocal,lista):
    for elem in reversed(lista): #recorre la lista al reves con un iterador
        print(elem)
        if vocal in elem:
            print('Eliminar: ' + elem)
            lista.remove(elem)
    print('Hecho!')


def eSV2(vocal,lista):
    for i in range(len(lista)-1,-1,-1):
        if vocal in lista[i]:
            print(lista.pop(i))
    print('Hecho!')










