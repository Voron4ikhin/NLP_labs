import unittest
from yargy import rule, or_, and_, not_, Parser
from yargy.interpretation import fact
from yargy.predicates import caseless, normalized, dictionary
from yargy.predicates import gram
from yargy.relations import gnc_relation
from yargy.pipelines import morph_pipeline

from someinfo import *


city = ['nameCity', 'typeCity']
City = fact('City', city)
default = City(nameCity=None, typeCity=None)

CITY_NAME = dictionary(cities_names).interpretation(City.nameCity)
CITY_NAME_COMPLEX = morph_pipeline(cities_names).interpretation(City.nameCity)
CITY_TYPE = dictionary(cities_types).interpretation(City.typeCity)
ONLY_CITY = rule(CITY_NAME)
ONLY_CITY_COMPLEX = rule(CITY_NAME_COMPLEX)
NAME_TYPE = rule(CITY_NAME, CITY_TYPE)
TYPE_NAME = rule(CITY_TYPE, CITY_NAME)
NAME_TYPE_COMPLEX = rule(CITY_NAME_COMPLEX, CITY_TYPE)
TYPE_NAME_COMPLEX = rule(CITY_TYPE, CITY_NAME_COMPLEX)
FINAL_CITY_NAME = or_(ONLY_CITY, ONLY_CITY_COMPLEX, NAME_TYPE, TYPE_NAME, NAME_TYPE_COMPLEX, TYPE_NAME_COMPLEX).interpretation(City)
parser = Parser(FINAL_CITY_NAME)
text = '''город нижний новгород'''
for match in parser.findall(text):
    print(match.fact)


class TestCity(unittest.TestCase):
    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, (None, None))

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, ('липецк', 'город'))

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, ('сургут', None))

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, ('липецк', 'город'))

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, (None, None))

    def test_6(self):
        testing_address = 'сургут югорская 30/2'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, ('сургут', None))

    def test_7(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, (None, None))

    def test_8(self):
        testing_address = 'ты сургут улица 30 лет победы'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, ('сургут', None))

    def test_9(self):
        testing_address = 'надо 50% город нальчик горького 1257'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, ('нальчик', 'город'))

    def test_10(self):
        testing_address = 'null'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, (None, None))

    def test_11(self):
        testing_address = '60 мегабит я'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, (None, None))

    def test_12(self):
        testing_address = 'сургут крылова 53/4'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, ('сургут', None))

    def test_13(self):
        testing_address = 'так москва хамовнический вал но я думаю что я еще обсужу со своими домашними то есть вот у нас цифровое телевидение есть но акадо вот вы не спешите я тогда вам наберу но либо в приложения'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, ('москва', None))

    def test_14(self):
        testing_address = 'мое 3 парковая'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, (None, None))

    def test_15(self):
        testing_address = 'Пришвина 17'
        match = (None, None)  if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, (None, None))

    def test_16(self):
        testing_address = 'Старый Гай 1 корпус 2'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None, match.typeCity if hasattr(match, 'typeCity') else None)
        self.assertEqual(res, (None, None))


if __name__ == '__main__':
    unittest.main()