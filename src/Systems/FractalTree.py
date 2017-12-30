from .. import Grammar, Symbols, Rules

class FractalTree(Grammar.Grammar):
    """
    https://en.wikipedia.org/wiki/L-system#Example_2:_Fractal_(binary)_tree
    """

    def __init__(self):

        v0 = Symbols.Constant('0')
        v1 = Symbols.Constant('1')
        c1 = Symbols.Constant('[')
        c2 = Symbols.Constant(']')

        r1 = Rules.SimpleRule(v1, Symbols.String([v1, v1]))
        r2 = Rules.SimpleRule(v0, Symbols.String([v1, c1, v0, c2, v0]))

        super(FractalTree, self).__init__(v0, [v0, v1, c1, c2], [r1, r2])
