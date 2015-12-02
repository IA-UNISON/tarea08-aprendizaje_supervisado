#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
id3.py
------------

Arbol de decisión tipo ID3

"""

__author__ = 'juliowaissman'


import math


class NodoID3(object):
    """
    Nodo para un árbol de desición tipo ID3.

    """
    def __init__(self, clase, atributo=None):
        self.clase = clase
        self.atributo = atributo
        self.hijos = {}

    def asigna(self, x):
        """
        Asignación individual tipo ID3, 

        """
        if not self.hijos or not self.atributo or x[self.atributo] not in self.hijos.keys():
            return self.clase
        return self.hijos[x[self.atributo]].asigna(x)

    def __str__(self):
        """
        Representacion del nodo

        """
        def indenta(texto):
            """ Toma una cadena multilineas y agrega un tab despues de cada salto de linea """
            return '\t'+texto.replace('\n', '\n\t')

        if not self.hijos:
            return "\nla clase es: " + str(self.clase)
        cadena = ''
        for hijo in self.hijos:
            cadena += '\nSi atributo '+str(self.atributo)+' es '+str(hijo)+' entonces '+indenta(str(self.hijos[hijo]))
        return cadena


def moda(lista):
    """
    Devuelve el valor que mas se repite en una lista

    """
    return max(lista, key=lambda elemento: lista.count(elemento))


class ArbolDecision(object):
    """
    Arbol de desición sencillo

    """
    def __init__(self, atributos):
        """
        Para inicializar el arbol de decisión es necesario
        incluir una lista de atributos tal que para cada atributo en la posición i:

            A[i] = [val_1, val_2, ..., val_{n_i}]

        """
        self.atributos = atributos
        self.numero_nodos = 0
        self.numero_hojas = 0
        self.raiz = None

    def entrena(self, datos, clases):
        """
        Manda llamar la función recursiva para realizar un árbol
        """
        self.raiz = self.construye_arbol(datos, clases, [], moda(clases))

    def construye_arbol(self, datos, clases, atributos_utilizados, clase_default, prepoda=(0, 1.0, 0.0001)):
        """
        Construye un árbol de forma recursiva utilizando el método
        clásico

        """
        self.numero_nodos += 1

        if len(datos) <= prepoda[0] or len(atributos_utilizados) == len(self.atributos):
            self.numero_hojas += 1
            return NodoID3(clase_default)

        clase_actual = moda(clases)
        if 1.0 * clases.count(clase_actual) / len(clases) >= prepoda[1]:
            self.numero_hojas += 1
            return NodoID3(clase_actual)

        atributo, ganancia_informacion = self.selecciona_atributo(datos, clases, atributos_utilizados)
        if ganancia_informacion <= prepoda[2]:
            self.numero_hojas += 1
            return NodoID3(clase_actual)

        nodo = NodoID3(clase_actual, atributo)
        atributos_utilizados.append(atributo)

        for val in self.atributos[atributo]:
            nodo.hijos[val] = self.construye_arbol([x for x in datos if x[atributo] == val],
                                                   [t for (t,x) in zip(clases,datos) if x[atributo] == val],
                                                   atributos_utilizados,
                                                   clase_actual)
        atributos_utilizados.pop()
        return nodo

    def selecciona_atributo(self, datos, clases, revisados):
        """
        Selecciona el atributo que ofrece la mejor partición
        de acuerdo al criterio de ganancia de la información.

        En este método se utiliza como medida de impureza la entropía.
        """

        def entropia(clases):
            """
            Función de entropia.
            Devuelve la entropia y el número de elementos con que se contaba.

            """
            lista = [clases.count(i) for i in set(clases)]
            acc = len(clases)

            entropia_calculada = 0
            for val in lista:
                if val > 0:
                    entropia_calculada -= (1.0 * val / acc) * math.log(1.0 * val / acc, 2)
            return entropia_calculada, acc
            # return (reduce(lambda x,y: x - y, [(1.0 * val / acc) * math.log(1.0 * val / acc, 2)
            #                                    for val in lista if val > 0]),
            #         acc)

        entropia_padre, nt = entropia(clases)
        mejor_ganancia_de_informacion = 0
        atributo = 0

        for i in range(len(self.atributos)):
            if i in revisados:
                continue
            ganancia_informacion = entropia_padre

            for valor_posible in self.atributos[i]:
                if valor_posible in set([x[i] for x in datos]):
                    entropia_hijo, nh = entropia([t for (t, x) in zip(clases, datos) if x[i] == valor_posible])
                    ganancia_informacion -= (1.0 * nh / nt) * entropia_hijo

            if ganancia_informacion > mejor_ganancia_de_informacion:
                mejor_ganancia_de_informacion, atributo = ganancia_informacion, i

        return atributo, mejor_ganancia_de_informacion

    def reconoce(self, datos):
        """
        Reconoce la clase de un conjunto de datos

        """
        return [self.raiz.asigna(dato) for dato in datos]

    def __str__(self):
        """
        Función para representar el árbol

        """
        return str(self.raiz)


if __name__ == '__main__':

    # Para probarlo vamos empezar con el clásico problema de ir o no a jugar golf
    #
    # La última columna de los datos es la clase (Si o No), los otros atributos son
    # Cielo, Temperatura, Humedad, Viento respectivamente.
    #
    # Nuestro árbol no maneja nombres de los atributos pero no es dificil hacerlo

    golf =  [['Sol'   , 'Alta' , 'Alta'  , 'Debil' , 'No'],
             ['Sol'   , 'Alta' , 'Alta'  , 'Fuerte', 'No'],
             ['Nubes' , 'Alta' , 'Alta'  , 'Debil' , 'Si'],
             ['Lluvia',	'Suave', 'Alta'  , 'Debil' , 'Si'],
             ['Lluvia',	'Baja' , 'Normal', 'Debil' , 'Si'],
             ['Lluvia', 'Baja' , 'Normal', 'Fuerte', 'No'],
             ['Nubes' ,	'Baja' , 'Normal', 'Fuerte', 'Si'],
             ['Sol'   ,	'Suave', 'Alta'  , 'Debil' , 'No'],
             ['Sol'   ,	'Baja' , 'Normal', 'Debil' , 'Si'],
             ['Lluvia',	'Suave', 'Normal', 'Debil' , 'Si'],
             ['Sol'   , 'Suave', 'Normal', 'Fuerte', 'Si'],
             ['Nubes' ,	'Suave', 'Alta'  , 'Fuerte', 'Si'],
             ['Nubes' , 'Alta' , 'Normal', 'Debil',  'Si'],
             ['Lluvia',	'Suave', 'Alta'  , 'Fuerte', 'No']]

    datos = [dato[:-1] for dato in golf]
    clases = [dato[-1] for dato in golf]

    atributos = [set([dato[i] for dato in datos]) for i in range(len(datos[0]))]

    arbol = ArbolDecision(atributos)
    arbol.entrena(datos, clases)
    print "-----------------------------------------------------------------------"
    print "             Arbol de decision encontrado tipo ID3                     "
    print "-----------------------------------------------------------------------"
    print arbol