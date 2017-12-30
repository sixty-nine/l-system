from Symbols import Symbol, Constant, String
from Rules import Rule, SimpleRule

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

    def __str__(self):
        res = []
        for r in self.rules:
            res.append(str(self.rules[r]))
        return '%s { Axiom: %s; Rules: %s }' % (self.__class__.__name__, str(self.string), ', '.join(res))

    def pretty(self):
        return str(self) \
            .replace('; ', '\n\n  ').replace('{', '{\n ') \
            .replace('}', '\n}\n').replace(', ', ',\n    ') \
            .replace('Rules:', 'Rules:\n   ')

class SimpleGrammar(Grammar):

    def __init__(self, axiom, rules_arr):

        start = []
        symbols = {}
        rules = []

        for s in axiom:
            symbol = self._add_symbol(symbols, s)
            start.append(symbol)

        for r in rules_arr:
            if r[1] != '=': raise ValueError('Malformed rule: ' + r)
            symbol = self._add_symbol(symbols, r[0])
            rule = []
            for s in r[2:]:
                s =self._add_symbol(symbols, s)
                rule.append(s)
            rules.append(SimpleRule(symbol, String(rule)))

        super(SimpleGrammar, self).__init__(String(start), symbols.values(), rules)

    def _add_symbol(self, symbols, value):
        if value in symbols.keys():
            return symbols[value]

        symbols[value] = Constant(value)
        return symbols[value]
