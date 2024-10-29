import unittest
import runner
import runner2


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r1 = runner.Runner('my_r1')
        count = 0
        while count < 10:
            r1.walk()
            count += 1
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r2 = runner.Runner('my_r2')
        count = 0
        while count < 10:
            r2.run()
            count += 1
        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

class TournamentTest(unittest.TestCase):
    is_frozen = True
    # setUpClass - метод, где создаётся атрибут класса all_results - словарь в который будут сохраняться результаты
    # всех тестов.

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    # setUp - метод, где создаются 3 объекта:
    # Бегун по имени Усэйн, со скоростью 10.
    # Бегун по имени Андрей, со скоростью 9.
    # Бегун по имени Ник, со скоростью 3.

    def setUp(self):
        self.r1 = runner2.Runner('Усэйн', 10)
        self.r2 = runner2.Runner('Андрей', 9)
        self.r3 = runner2.Runner('Ник', 3)

    # tearDownClass - метод, где выводятся all_results по очереди в столбец

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def tearDown(self):
        for key, value in all_results.items():
            all_results[key] = value.name
        print(all_results)

    # Метод тестирования забегов, в котором создаётся объект Tournament на дистанцию 90.
    # У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results.
    # В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
    # (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        t1 = runner2.Tournament(90, self.r1, self.r3).start()
        all_results.update(t1)
        self.assertTrue(all_results.get(len(all_results)) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        t2 = runner2.Tournament(90, self.r2, self.r3).start()
        all_results.update(t2)
        self.assertTrue(all_results.get(len(all_results)) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        t3 = runner2.Tournament(90, self.r1, self.r2, self.r3).start()
        all_results.update(t3)
        self.assertTrue(all_results.get(len(all_results)) == 'Ник')

if __name__ == '__main__':
    unittest.main()
