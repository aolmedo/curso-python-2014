class List(list):
    """Clase de lista mejorada
    """ 
    def first(self):
        return self[0]

    def second(self):
        return self[1]

    def third(self):
        return self[2]

    def fourth(self):
        return self[3]

    def collect(self, aFunction):
        return map(aFunction, self)

    def select(self, aFunction):
        return filter(aFunction, self)

    def reject(self, aFunction):
        pass
