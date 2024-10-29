import unittest
from tests_12_3 import RunnerTest, TournamentTest

my_testST = unittest.TestSuite()
my_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
my_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_testST)
