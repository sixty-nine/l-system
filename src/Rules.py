from Symbols import String

class Rule(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def apply(self):
        return String([self.symbol])

    def __str__(self):
        return str(self.symbol) + ' --> ' + str(self.apply())

class SimpleRule(Rule):
    def __init__(self, symbol, string):
        super(SimpleRule, self).__init__(symbol)
        if not isinstance(string, String): raise ValueError('Invalid string')
        self.string = string
    def apply(self):
        return self.string

