import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r1 = runner.Runner('my_r1')
        count = 0
        while count < 10:
            r1.walk()
            count +=1
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        r2 = runner.Runner('my_r2')
        count = 0
        while count < 10:
            r2.run()
            count += 1
        self.assertEqual(r2.distance, 100)

    def test_challenge(self):
        r3 = runner.Runner('my_r3')
        r4 = runner.Runner('my_r4')
        count = 0
        while count < 10:
            r3.walk()
            r3.run()
            r4.walk()
            r4.run()
            count += 1
        self.assertNotEqual(r3.distance, 50, 100)
        self.assertNotEqual(r4.distance, 50, 100)
