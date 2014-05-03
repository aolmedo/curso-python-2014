#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import doctest


def promedio(valores):
    """Calcula el promedio de una lista de números
    
    >>> print promedio([20, 30, 70])
    40.0
    """
    return sum(valores, 0.0) / len(valores)

print "Pruebas con doctest: " 

print doctest.testmod() #valida automáticamente las pruebas integradas

print "Pruebas con unittest: "

class PromedioTestCase(unittest.TestCase):
    
    def test_promedio(self):
        self.assertEquals(40.0, promedio([20, 30, 70]))
        self.assertEquals(4.3, round(promedio([1, 5, 7]), 1))
        self.assertRaises(ZeroDivisionError, promedio, [])
        self.assertRaises(TypeError, promedio, 20, 30, 70)
        
if __name__ == '__main__':
    unittest.main() #llamarlo de la linea de comando ejecuta todas las pruebas
