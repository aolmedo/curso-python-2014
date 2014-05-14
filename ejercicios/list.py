#!/usr/bin/python
# -*- coding: utf-8 -*-

class List(list):
    """Clase de lista mejorada
    """
    @property
    def first(self):
        return self[0]

    @property
    def second(self):
        return self[1]

    @property
    def third(self):
        return self[2]

    @property
    def fourth(self):
        return self[3]

    @property
    def last(self):
	self[-1]

    def collect(self, aFunction):
        return map(aFunction, self)

    def select(self, aFunction):
        return filter(aFunction, self)

    def reject(self, aFunction):
        pass
