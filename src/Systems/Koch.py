from .. import Grammar, Symbols, Rules

class Koch(Grammar.Grammar):
    """
    https://en.wikipedia.org/wiki/L-system#Example_4:_Koch_curve
    """

    def __init__(self):

        f = Symbols.Constant('F')
        plus = Symbols.Constant('+')
        minus = Symbols.Constant('-')

        r = Rules.SimpleRule(f, Symbols.String([f, plus, f, minus, f, minus, f, plus, f]))

        super(Koch, self).__init__(f, [f, plus, minus], [r])
