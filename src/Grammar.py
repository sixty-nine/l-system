from Symbols import Symbol, String
from Rules import Rule

class Grammar(object):
    def __init__(self, start_symbol, alphabet = [], rules = []):
        self.alphabet = []
        self.rules = {}
        self.generation = 0

        if isinstance(start_symbol, Symbol):
            self.string = String([start_symbol])
        elif isinstance(start_symbol, list):
            self.string = String(start_symbol)
        elif isinstance(start_symbol, String):
            self.string = start_symbol
        else:
            raise ValueError('Invalid start symbol')

        for symbol in alphabet:
            self.add_symbol(symbol)

        for rule in rules:
            self.add_rule(rule)

    def add_symbol(self, symbol):
        if not isinstance(symbol, Symbol): raise ValueError('Invalid symbol')
        self.alphabet.append(symbol)

    def add_rule(self, rule):
        if not isinstance(rule, Rule): raise ValueError('Invalid rule')
        self.rules[rule.symbol] = rule

    def run(self, count = 1):
        for i in xrange(count):
            self._do_run()
        return self

    def _do_run(self):
        self.generation += 1
        res = String()
        for item in self.string:
            if item in self.rules:
                for s in self.rules[item].apply():
                    res.add_item(s)
            else:
                res.add_item(item)
        self.string = res
