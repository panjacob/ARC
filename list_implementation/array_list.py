from list_implementation.my_list import MyList
from list_implementation.singleton import singleton


@singleton
class ArrayList(MyList):
    def __init__(self):
        self.elements = []

    def push(self, value):
        self.elements.append(value)

    def remove(self, value):
        self.elements.remove(value)

    def insert(self, index, value):
        self.elements = self.elements[:index] + [value] + self.elements[index:]

    #   self.elements.index(index, value)

    def search(self, value):
        return self.elements.index(value)

    def merge(self, new_list):
        self.elements += new_list.items()

    def items(self):
        return self.elements

    def even(self):
        result = []
        for el in self.elements:
            if el % 2 == 0:
                result.append(el)
        return result

    def odd(self):
        result = []
        for el in self.elements:
            if el % 2 == 1:
                result.append(el)
        return result
