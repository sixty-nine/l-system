import unittest

import LSystem

class LSystemTestCase(unittest.TestCase):

    def testAlgae(self):

        g = LSystem.Systems.Algae()

        self.assertEqual('A', str(g.string))
        self.assertEqual('AB', str(g.run().string))
        self.assertEqual('ABA', str(g.run().string))
        self.assertEqual('ABAAB', str(g.run().string))
        self.assertEqual('ABAABABA', str(g.run().string))
        self.assertEqual('ABAABABAABAAB', str(g.run().string))
        self.assertEqual('ABAABABAABAABABAABABA', str(g.run().string))
        self.assertEqual('ABAABABAABAABABAABABAABAABABAABAAB', str(g.run().string))

    def testFractalTree(self):
        g = LSystem.Systems.FractalTree()

        self.assertEqual('0', str(g.string))
        self.assertEqual('1[0]0', str(g.run().string))
        self.assertEqual('11[1[0]0]1[0]0', str(g.run().string))
        self.assertEqual('1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0', str(g.run().string))

    def testKoch(self):
        g = LSystem.Systems.Koch()

        self.assertEqual('F', str(g.string))
        self.assertEqual('F+F-F-F+F', str(g.run().string))
        self.assertEqual('F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F', str(g.run().string))
        self.assertEqual('F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F+' +
                         'F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-' +
                         'F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F-' +
                         'F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F+' +
                         'F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F', str(g.run().string))
