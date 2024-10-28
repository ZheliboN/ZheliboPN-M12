import unittest
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    iz_frozen = False

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r1 = Runner('Boris')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r2 = Runner('Nikas')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r3 = Runner('Alex')
        r4 = Runner('Olga')
        for i in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)


class TournamentTest(unittest.TestCase):
    iz_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = list()

    @unittest.skipIf(iz_frozen,'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.s_men1 = Runner('Усэйн', 10)
        self.s_men2 = Runner('Андрей', 10)
        self.s_men3 = Runner('Ник', 3)

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        #Усэйн и Ник
        tur01 = Tournament(90, self.s_men1, self.s_men3)
        TournamentTest.all_results.append(tur01.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])] == self.s_men3.name)

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        #Андрей и Ник
        tur02 = Tournament(90, self.s_men2, self.s_men3)
        TournamentTest.all_results.append(tur02.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])] == self.s_men3.name)

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        #Усэйн, Андрей и Ник
        tur03 = Tournament(90, self.s_men1, self.s_men2, self.s_men3)
        TournamentTest.all_results.append(tur03.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])] == self.s_men3.name)

    @classmethod
    def tearDownClass(cls):
        output_dict = {}
        for race in cls.all_results:
            for key, value in race.items():
                output_dict[key] = value.name
            print(output_dict)


if __name__ == "__main__":
    unittest.main()
