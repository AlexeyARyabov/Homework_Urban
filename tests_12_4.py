import unittest
import rt_with_exceptions
import logging


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s : %(levelname)s : %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r1 = rt_with_exceptions.Runner('my_r1', -5)
            logging.info('"test_walk" выполнен успешно')
            count = 0
            while count < 10:
                r1.walk()
                count += 1
            self.assertEqual(r1.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r2 = rt_with_exceptions.Runner(24)
            logging.info('"test_run" выполнен успешно')
            count = 0
            while count < 10:
                r2.run()
                count += 1
            self.assertEqual(r2.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r3 = rt_with_exceptions.Runner('my_r3')
        r4 = rt_with_exceptions.Runner('my_r4')
        count = 0
        while count < 10:
            r3.walk()
            r3.run()
            r4.walk()
            r4.run()
            count += 1
        self.assertNotEqual(r3.distance, 50, 100)
        self.assertNotEqual(r4.distance, 50, 100)

if __name__ == '__main__':
    unittest.main()


