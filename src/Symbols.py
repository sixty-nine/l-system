class Symbol(object):
    def __init__(self):
        pass

class Constant(Symbol):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class String(object):
    """
    A string of Symbols
    """
    def __init__(self, items = []):
        self._items = []
        for item in items:
            self.add_item(item)

    def add_item(self, item):
        if not isinstance(item, Symbol): raise ValueError('The item must be a Symbol')
        self._items.append(item)

    def __iter__(self):
       for item in self._items:
          yield item

    def __str__(self):
        res = ''
        for item in self._items:
            res += str(item)
        return res

