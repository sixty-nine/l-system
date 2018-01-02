from .. import Grammar, Symbols, Rules

class TwinDragon(Grammar.SimpleGrammar):
    """
    https://en.wikipedia.org/wiki/Dragon_curve#Twindragon
    """

    def __init__(self):
        super(TwinDragon, self).__init__('X+YF', ['X=X+YF', 'Y=FX-Y'])