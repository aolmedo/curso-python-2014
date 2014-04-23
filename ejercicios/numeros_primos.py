#!/usr/bin/python
# -*- coding: utf-8 

def es_numero_primo(numero):
    return numero > 1 and len([n for n in range(2, numero-1) if numero % n == 0]) == 0


 t = [x for x in range(10000) if es_numero_primo(x)]
