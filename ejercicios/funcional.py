#!/usr/bin/python
# -*- coding: utf-8 

maximo = lambda x, y: x > y and x or y

def maximoLista(lista):
    m = lista[0]
    for x in lista:
        m = maximo(m,x)


