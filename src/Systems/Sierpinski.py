from .. import Grammar, Symbols, Rules

class Sierpinski(Grammar.Grammar):
    """
    https://en.wikipedia.org/wiki/L-system#Example_5:_Sierpinski_triangle
    """

    def __init__(self):

        f = Symbols.Constant('F')
        g = Symbols.Constant('G')
        c1 = Symbols.Constant('+')
        c2 = Symbols.Constant('-')

        r1 = Rules.SimpleRule(f, Symbols.String([f, c2, g, c1, f, c1, g, c2, f]))
        r2 = Rules.SimpleRule(g, Symbols.String([g, g]))

        super(Sierpinski, self).__init__(Symbols.String([f, c2, g, c2, g]), [f, g, c1, c2], [r1, r2])
