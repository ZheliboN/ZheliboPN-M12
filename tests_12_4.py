import logging
import unittest
import traceback


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    iz_frozen = False

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r1 = Runner('Борис', -8)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning(f"Неверная скорость для Runner\n{err}")
            logging.warning(traceback.format_exc())

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r2 = Runner(['Пётр'])
            for i in range(-10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning(f"Неверный тип данных для объекта Runner\n{err}")
            logging.warning(traceback.format_exc())

    @unittest.skipIf(iz_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r3 = Runner('Alex')
        r4 = Runner('Olga')
        for i in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
if __name__ == "__main__":
    unittest.main()
