from .. import Grammar, Symbols, Rules

class QuadraticKochIsland(Grammar.SimpleGrammar):
    """
    http://paulbourke.net/fractals/quadratic_koch_island_b/
    """

    def __init__(self):
        super(QuadraticKochIsland, self).__init__('F+F+F+F', ['F=F-FF+FF+F+F-F-FF+F+F-F-FF-FF+F'])
