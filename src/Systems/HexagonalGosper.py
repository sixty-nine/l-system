from .. import Grammar, Symbols, Rules

class HexagonalGosper(Grammar.Grammar):
    """
    http://paulbourke.net/fractals/hexagonal_gosper/
    """

    def __init__(self):

        x = Symbols.Constant('X')
        y = Symbols.Constant('Y')
        f = Symbols.Constant('F')
        plus = Symbols.Constant('+')
        minus = Symbols.Constant('-')

        r1 = Rules.SimpleRule(x, Symbols.String([x, plus, y, f, plus, plus, y, f, minus, f, x, minus, minus, f, x, f, x, minus, y, f, plus]))
        r2 = Rules.SimpleRule(y, Symbols.String([minus, f, x, plus, y, f, y, f, plus, plus, y, f, plus, f, x, minus, minus, f, x, minus, y]))

        super(HexagonalGosper, self).__init__(Symbols.String([x, f]), [x, y, f, plus, minus], [r1, r2])
