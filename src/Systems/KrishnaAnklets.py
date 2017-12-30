from .. import Grammar, Symbols, Rules

class KrishnaAnklets(Grammar.SimpleGrammar):
    """
    http://paulbourke.net/fractals/krishna/
    """

    def __init__(self):
        super(KrishnaAnklets, self).__init__('X--X', ['X=XFX--XFX'])
