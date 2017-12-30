from .. import Grammar, Symbols, Rules

class Rings(Grammar.SimpleGrammar):
    """
    http://paulbourke.net/fractals/rings/
    """

    def __init__(self):
        super(Rings, self).__init__('F+F+F+F', ['F=FF+F+F+F+F+F-F'])
