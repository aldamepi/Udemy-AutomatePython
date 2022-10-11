#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:41:05 2022

@author: albertomengual
"""






# F STRINGS

name = 'Alberto'
age = 41

print(f"""esto es una prueba de {name},
para comprobar los "f-strings" y
    los "multine string".
El año proximo tendré {age+1} años.""")





############### STRING METHODS


spam = 'This is a sample text'


spam.capitalize() # El primer carácter de la cadena en mayuscula
print(spam.capitalize())


spam.casefold() # retorna un texto normalizado a minuscula. un lower con poderes

spam.lower() # retorna copia en minuscula

spam.swapcase() # devuelve copia case invertidos

spam.title() # Devuelve version titula. Primera mayuscula de cada palabra

spam.upper() # Todas mayuscuals



spam.islower() # True si todos minuscula y no vacio
spam.isupper() # True si todos mayuscula
spam.istitle() # True si todas las palabras forma de titulo


spam.isalpha() # True si alfabéticos (only letters) y al menos 1

spam.isalnum()  # True si todos los caracteres alfanumericos  (only letters
                # and numbers)
                # isalpha() or isdecimal() or isdigit() or isnumeric()
                 
spam.isascii() # True is vacía o todos ASCII

spam.isdecimal() # True si decimales (numeric characters) y al menos uno

bacon = '8453'
bacon = '8453.0'
bacon.isdecimal()

bacon.isdigit() # True si dígitos y al menos uno

bacon.isnumeric() # True si numerico y al menos uno

spam.isspace() # True si todos espacios en blanco (spaces, tabs, newlines and
               # not blank)


spam.isidentifier() # ????

spam.isprintable() # True si es imprimible






spam.endswith(('text', 'sample')) # retorna True o False
spam.index('t',1)
spam.endswith(('text', 'sample'),0,17)
spam.endswith(('text', 'sample'),0,16)


spam.startswith('This') # idem endswith pero al principio
spam.startswith('is',5) # los iterables de la tupla tienen que estar ordenados








'@'.join(spam)
'-'.join(bacon) # Retorna una concatenacion del string en el iterable pasado
                # pasado a la función (cadena, lista...)


spam.split() # by default, white spaces characters, tab or newline.
spam.split('is',1) # divide el string por n ocurrencias. En el resultado
                   # no aparecen las ocurrencias de la division.
                   # Devuelve una lista
''.join(spam.split())

spam.rsplit(' ',2) # igual que split pero empezando por la derecha


multitexto = "Esto es un texto de \ntres líneas\n"

multitexto.splitlines() # devuelve lista con las lineas. 
                        # no incluye como items las lineas vacias
                        # keepends = True -> conserva los separadores
multitexto.split('\n')
multitexto.splitlines(keepends=True)






spam.partition(' ') # divide string en la primera ocurrencia
spam.partition('sample') # devuelve tupla de tres elementos
spam.partition('sample')[2]

spam.rpartition('is') # divide por la útlima ocurrencia 






spam.center(60, '#') # centra el texto en una longitud especificada con un
                     # caracter opcional
(' ' + spam + ' ').center(60, '#')

bacon.ljust(40,'-') # alinea a la izquierda 

bacon.rjust(15,'0') # alinea a la derecha






spam.strip('tTx') # Elimina los caratereces especificados del principio y el 
                # final, por defecto ' '. No ordenados
spam.lstrip('hiTs') # elimina determinados caracteres al principio. 
                    # Por defecto ' '!! No ordenados !!
spam.rstrip('xett') # elimina determinados caracteres al final, no ordenados







spam.count('a', 0,10)
spam.count('a')
spam.count('hi')





spam.encode() # retorna un b-string: version codificada en bytes




spam. expandtabs() # cambia tabuladores por espacios






spam.find('is') # retorna el menor indice de la cadena donde está el parametro
spam.find('is',4) 
spam.find('e',9,17) # es como un index. retorna -1 si no encuentra nada

spam.index('t',1) # es como find pero retorna ValueError si no encuentra


spam.rfind('is') # retorna el mayor indice. si no -1

spam.rindex('t') # retorna el mayor indice. si no ValueError







spam.replace('sample', 'wonderful') 
spam.replace('e','i',1) # sustituye una cadena por otra n veces




str.maketrans() # retorna una tabla de traducción para str.translate
str.translate() # traduce cadenas segun una tabla de traducción ???




bacon.zfill(15) # zero fill, rellena de ceros a la izquierda







"The sum of 1 + 2 is {0}, not {1}".format(1+2,4) 
# realiza una operacion de formateo, convierte expresiones a texto. 
# es similar al f-string pero las expresiones son parametros y las marcas
# de reemplazo entre llaves son los indices (o nombres...) a dichos parametros.


spam.format_map() # ???????






' FORMATEO ESTILO PRINTF '.center(60,'#')
################## FORMATEO ESTILO PRINTF ##################
# ver tipos integrados













































































