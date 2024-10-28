import unittest
import tests_12_3

testRT = unittest.TestSuite()
testRT.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testRT.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(testRT)
