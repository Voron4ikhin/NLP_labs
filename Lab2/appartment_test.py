import unittest
from yargy import rule, or_, and_, Parser
from yargy.predicates import gte, lte
from yargy.interpretation import fact
from yargy.predicates import dictionary, in_caseless

from someinfo import *


apartment = ['numberApparts']
Apartment = fact('Building', apartment)
default = Apartment(numberApparts=None)

NUMBER = rule(and_(gte(1), lte(100000))).interpretation(Apartment.numberApparts)
APARTMENT_TYPE = dictionary(apartment_type)

APARTMENT_NUMBER = rule(APARTMENT_TYPE, NUMBER)
NUMBER_APARTMENT = rule(NUMBER, APARTMENT_TYPE)

FINAL_APARTMENT = or_(APARTMENT_NUMBER, NUMBER_APARTMENT).interpretation(Apartment)
parser = Parser(FINAL_APARTMENT)
text = '''город липецк улица катукова 2 а квартира 223'''
for match in parser.findall(text):
    print(match.fact)


class TestAppartment(unittest.TestCase):
    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        match = (None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(res, None)

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        match = (None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(res, None)

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        match = (None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(res, None)

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        match = (None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(res, None)

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        match = (None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(res, '310')

    def test_6(self):
        testing_address = 'Кусковская 19 корпус 1'
        match = (None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(res, None)

    def test_7(self):
        testing_address = 'марша захарова 12 маршала захарова дом 12'
        match = (None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(res, None)

    def test_8(self):
        testing_address = 'null'
        match = (None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()