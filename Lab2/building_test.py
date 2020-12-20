import unittest
from yargy import rule, or_, and_, Parser
from yargy.predicates import gte, lte
from yargy.interpretation import fact
from yargy.predicates import dictionary, in_caseless

from someinfo import *


building = ['numberBuilding', 'numberCorp', 'typeBuilding']
Building = fact('Building', building)
default = Building(numberBuilding=None, numberCorp=None, typeBuilding=None)

LETTER = in_caseless(set('абвгдеёжзийклмнопрстуфхцчшщьыъэюя'))
NUMBER = rule(and_(gte(1), lte(1000)), LETTER.optional())
BUILDING_NUMBER = or_(rule(NUMBER, LETTER), rule(NUMBER)).interpretation(Building.numberBuilding)
STREET_TYPE = dictionary(building_type)
BUILDING_TYPE = dictionary(streets_name)
CORP_TYPE = dictionary(corp_type)
CORP_NUMBER = NUMBER.interpretation(Building.numberCorp)

FULL_BUILDING = rule(BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER)
ONLY_ONE = rule(BUILDING_TYPE, BUILDING_NUMBER)
FULL_STREET = rule(STREET_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER)
ONLY_ONE_STREET = rule(STREET_TYPE, BUILDING_NUMBER)


FINAL_BUILDING = or_(FULL_BUILDING, ONLY_ONE, FULL_STREET, ONLY_ONE_STREET).interpretation(Building)
parser = Parser(FINAL_BUILDING)
text = '''город липецк улица катукова 2 а'''
for match in parser.findall(text):
    print(match.fact)


class TestHome(unittest.TestCase):
    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
        match.numberBuilding if hasattr(match, 'numberBuilding') else None,
        match.numberCorp if hasattr(match, 'numberCorp') else None,
        match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('50', None, None))

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 а'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberBuilding if hasattr(match, 'numberBuilding') else None,
            match.numberCorp if hasattr(match, 'numberCorp') else None,
            match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('36 а', None, None))

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberBuilding if hasattr(match, 'numberBuilding') else None,
            match.numberCorp if hasattr(match, 'numberCorp') else None,
            match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('31а', None, None))

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberBuilding if hasattr(match, 'numberBuilding') else None,
            match.numberCorp if hasattr(match, 'numberCorp') else None,
            match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('18', None, None))

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberBuilding if hasattr(match, 'numberBuilding') else None,
            match.numberCorp if hasattr(match, 'numberCorp') else None,
            match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('9', None, None))

    def test_6(self):
        testing_address = 'артема 32 квартира 8'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberBuilding if hasattr(match, 'numberBuilding') else None,
            match.numberCorp if hasattr(match, 'numberCorp') else None,
            match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('32', None, None))

    def test_7(self):
        testing_address = 'город липецк полиграфическая дом 4'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberBuilding if hasattr(match, 'numberBuilding') else None,
            match.numberCorp if hasattr(match, 'numberCorp') else None,
            match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('4', None, None))

    def test_8(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberBuilding if hasattr(match, 'numberBuilding') else None,
            match.numberCorp if hasattr(match, 'numberCorp') else None,
            match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('55', '1', None))

    def test_9(self):
        testing_address = 'люберцы октябрьский проспект 10 корпус 1'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberBuilding if hasattr(match, 'numberBuilding') else None,
            match.numberCorp if hasattr(match, 'numberCorp') else None,
            match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('10', '1', None))

    def test_10(self):
        testing_address = 'бульвар миттова 24'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberBuilding if hasattr(match, 'numberBuilding') else None,
            match.numberCorp if hasattr(match, 'numberCorp') else None,
            match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('24', None, None))

    def test_11(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        match = (None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (
            match.numberBuilding if hasattr(match, 'numberBuilding') else None,
            match.numberCorp if hasattr(match, 'numberCorp') else None,
            match.typeBuilding if hasattr(match, 'typeBuilding') else None)
        self.assertEqual(res, ('78', None, None))


if __name__ == '__main__':
    unittest.main()



