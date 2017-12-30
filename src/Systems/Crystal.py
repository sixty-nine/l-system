from .. import Grammar, Symbols, Rules

class Crystal(Grammar.Grammar):
    """
    http://paulbourke.net/fractals/crystal/
    """

    def __init__(self):

        f = Symbols.Constant('F')
        plus = Symbols.Constant('+')

        r1 = Rules.SimpleRule(f, Symbols.String([f, f, plus, f, plus, plus, f, plus, f]))

        super(Crystal, self).__init__(Symbols.String([f, plus, f, plus, f, plus, f, plus]), [f, plus], [r1])
