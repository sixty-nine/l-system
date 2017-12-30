from .. import Grammar, Symbols, Rules

class Algae(Grammar.Grammar):
    """
    https://en.wikipedia.org/wiki/L-system#Example_1:_Algae
    """

    def __init__(self):

        s1 = Symbols.Constant('A')
        s2 = Symbols.Constant('B')

        r1 = Rules.SimpleRule(s1, Symbols.String([s1, s2]))
        r2 = Rules.SimpleRule(s2, Symbols.String([s1]))

        super(Algae, self).__init__(s1, [s1, s2], [r1, r2])
