import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = list()

    def setUp(self):
        self.s_men1 = Runner('Усэйн', 10)
        self.s_men2 = Runner('Андрей', 10)
        self.s_men3 = Runner('Ник', 3)

    def test_tur01(self):
        #Усэйн и Ник
        tur01 = Tournament(90, self.s_men1, self.s_men3)
        TournamentTest.all_results.append(tur01.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])] == self.s_men3.name)

    def test_tur02(self):
        #Андрей и Ник
        tur02 = Tournament(90, self.s_men2, self.s_men3)
        TournamentTest.all_results.append(tur02.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])] == self.s_men3.name)

    def test_tur03(self):
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
