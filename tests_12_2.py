import runner2
import unittest


class TournamentTest(unittest.TestCase):
        # setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты
    # всех тестов.

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    #setUp - метод, где создаются 3 объекта:
    #Бегун по имени Усэйн, со скоростью 10.
    #Бегун по имени Андрей, со скоростью 9.
    #Бегун по имени Ник, со скоростью 3.

    def setUp(self):
        self.r1 = runner2.Runner('Усэйн', 10)
        self.r2 = runner2.Runner('Андрей', 9)
        self.r3 = runner2.Runner('Ник', 3)

    # tearDownClass - метод, где выводятся all_results по очереди в столбец

    def tearDown(self):
        for key, value in all_results.items():
            all_results[key] = value.name
        print(all_results)

    # Метод тестирования забегов, в котором создаётся объект Tournament на дистанцию 90.
    # У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results.
    # В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
    # (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.

    def test_tournament_1(self):
        t1 = runner2.Tournament(90, self.r1, self.r3).start()
        all_results.update(t1)
        self.assertTrue(all_results.get(len(all_results)) == 'Ник')

    def test_tournament_2(self):
        t2 = runner2.Tournament(90,  self.r2, self.r3).start()
        all_results.update(t2)
        self.assertTrue(all_results.get(len(all_results)) == 'Ник')

    def test_tournament_3(self):
        t3 = runner2.Tournament(90, self.r1, self.r2, self.r3).start()
        all_results.update(t3)
        self.assertTrue(all_results.get(len(all_results)) == 'Ник')

if __name__ == "__main__":
    unittest.main()
