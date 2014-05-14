#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from list import List

class ListTestCase(unittest.TestCase):
    """Test de la implementación de la lista extendida
    	con las funcionalidades que tiene en smalltalk
    """
    def test_first_notEmptyList(self):
	aList = List([1])
	self.assertEquals(1, aList.first)

    def test_first_emptyList(self):
	aList = List()
	self.assertRaises(IndexError, lambda: aList.first)

    def test_second_listAtLeastTwoElement(self):
	aList = List([1, 2])
	self.assertEquals(2, aList.second)

    def test_second(self):
	aList = List()
	self.assertRaises(IndexError, lambda: aList.second)

    def test_select(self):
	aList = List([1, 2, 3, 4, 5, 6])
	filter_list = [False, True, True, False, False, True]
	aFunction = lambda x: filter_list[aList.index(x)]

	self.assertEquals(aList, aList.select(lambda x: True))
	self.assertEquals([], aList.select(lambda x: False))

	self.assertEquals([2, 3, 6], aList.select(aFunction))







if __name__ == '__main__':
    unittest.main()
