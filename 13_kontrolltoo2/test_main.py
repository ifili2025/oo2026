import unittest
from main import Toiduaine
from main import Toidukomponent
#Kontrolli toiduaine loomist automattestiga

class TestToiduaine(unittest.TestCase):
    def test_loomine(self):
        t = Toiduaine("kartul", 20, 20, 20)
        self.assertEqual(t.nimetus, "kartul")
        self.assertEqual(t.valk, 20)
        self.assertEqual(t.rasv, 20)
        self.assertEqual(t.süsivesikud, 20)
    def test_rasva_kogus(self):
        t = Toiduaine("kartul", 40, 10, 50)
        tk1 = Toidukomponent(t, 100)
        self.assertAlmostEqual(tk1.rasva_kogus(), float(10), places=7)

suite = unittest.TestLoader().loadTestsFromTestCase(TestToiduaine)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Teste: {result.testsRun}')