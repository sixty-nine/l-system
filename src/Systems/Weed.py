from .. import Grammar, Symbols, Rules

class Weed(Grammar.Grammar):
    """
    http://paulbourke.net/fractals/lsys_weed/
    """

    def __init__(self):

        f = Symbols.Constant('F')
        x = Symbols.Constant('X')
        y = Symbols.Constant('Y')
        plus = Symbols.Constant('+')
        minus = Symbols.Constant('-')
        c1 = Symbols.Constant('[')
        c2 = Symbols.Constant(']')

        # F -> FF-[XY]+[XY]
        # X -> +FY
        # Y -> -FX

        r1 = Rules.SimpleRule(f, Symbols.String([f, f, minus, c1, x, y, c2, plus, c1, x, y, c2]))
        r2 = Rules.SimpleRule(x, Symbols.String([plus, f, y]))
        r3 = Rules.SimpleRule(y, Symbols.String([minus, f, x]))

        super(Weed, self).__init__(f, [f, x, y, plus, minus, c1, c2], [r1, r2, r3])
