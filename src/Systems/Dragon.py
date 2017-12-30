from .. import Grammar, Symbols, Rules

class Dragon(Grammar.Grammar):
    """
    https://en.wikipedia.org/wiki/L-system#Example_6:_Dragon_curve
    """

    def __init__(self):

        x = Symbols.Constant('X')
        y = Symbols.Constant('Y')
        f = Symbols.Constant('F')
        plus = Symbols.Constant('+')
        minus = Symbols.Constant('-')

        r1 = Rules.SimpleRule(x, Symbols.String([x, plus, y, f, plus]))
        r2 = Rules.SimpleRule(y, Symbols.String([minus, f, x, minus, y]))

        super(Dragon, self).__init__(Symbols.String([f, x]), [x, y,f, plus, minus], [r1, r2])
