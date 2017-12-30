from .. import Grammar, Symbols, Rules

class Hilbert(Grammar.Grammar):
    """
    https://en.wikipedia.org/wiki/Hilbert_curve
    """

    def __init__(self):

        a = Symbols.Constant('A')
        b = Symbols.Constant('B')
        f = Symbols.Constant('F')
        plus = Symbols.Constant('+')
        minus = Symbols.Constant('-')

        r1 = Rules.SimpleRule(a, Symbols.String([minus, b, f, plus, a, f, a, plus, f, b, minus]))
        r2 = Rules.SimpleRule(b, Symbols.String([plus, a, f, minus, b, f, b, minus, f, a, plus]))

        super(Hilbert, self).__init__(a, [a, b, f, plus, minus], [r1, r2])
