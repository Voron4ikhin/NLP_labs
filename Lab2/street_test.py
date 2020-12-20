import unittest
from yargy import rule, or_, Parser
from yargy.interpretation import fact
from yargy.predicates import  dictionary
from yargy.pipelines import morph_pipeline

from someinfo import *

street = ['nameStreet', 'typeStreet']
Street = fact('Street', street)
default = Street(nameStreet=None, typeStreet=None)

STREET_NAME = dictionary(streets_name).interpretation(Street.nameStreet)
STREET_NAME_COMPLEX = morph_pipeline(streets_name).interpretation(Street.nameStreet)
STREET_TYPE = dictionary(streets_type).interpretation(Street.typeStreet)
ONLY_STREET = rule(STREET_NAME)
ONLY_STREET_COMPLEX = rule(STREET_NAME_COMPLEX)
NAME_TYPE = rule(STREET_NAME, STREET_TYPE)
TYPE_NAME = rule(STREET_TYPE, STREET_NAME)
NAME_TYPE_COMPLEX = rule(STREET_NAME_COMPLEX, STREET_TYPE)
TYPE_NAME_COMPLEX = rule(STREET_TYPE, STREET_NAME_COMPLEX)
FINAL_STREET_NAME = or_(ONLY_STREET, ONLY_STREET_COMPLEX, NAME_TYPE, TYPE_NAME, NAME_TYPE_COMPLEX, TYPE_NAME_COMPLEX).interpretation(Street)
parser = Parser(FINAL_STREET_NAME)


text = '''артема 32 квартира 8'''
for match in parser.findall(text):
    print(match.fact)


class TestStreet(unittest.TestCase):
    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None, match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('комсомольский', 'проспект'), res)

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('катукова', 'улица'), res)

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('рабочая', 'улица'), res)

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('доватора', None), res)

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('бехтеева', None), res)

    def test_6(self):
        testing_address = 'улица меркулова дом 24'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('меркулова', 'улица'), res)

    def test_7(self):
        testing_address = 'октябрьская 48 частный дом город сургут'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('октябрьская', None), res)

    def test_8(self):
        testing_address = 'сколько улица 30 лет победы 50 46'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('30 лет победы', 'улица'), res)

    def test_9(self):
        testing_address = 'тюменский тракт 10'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('тюменский', 'тракт'), res)

    def test_10(self):
        testing_address = 'сургут югорская 30/2'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('югорская', None), res)

    def test_11(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual((None, None), res)

    def test_12(self):
        testing_address = 'старый оскол микрорайон олимпийский дом 23 квартира 105'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('олимпийский', 'микрорайон'), res)

    def test_13(self):
        testing_address = 'город сургут улица фармана салманова 4'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual( ('фармана салманова', 'улица'), res)

    def test_14(self):
        testing_address = 'ты сургут улица 30 лет победы'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual( ('30 лет победы', 'улица'), res)

    def test_15(self):
        testing_address = 'проезд мунарева 2'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('мунарева', 'проезд'), res)

    def test_16(self):
        testing_address = 'домашний адрес где я живу'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual((None, None), res)

    def test_17(self):
        testing_address = 'артема 32 квартира 8'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('артема', None), res)

    def test_18(self):
        testing_address = 'знаете знаете у меня дорогая девочка у меня уже все есть и менять из из одного переходить на другой я не хочу поэтому какой город квартира какой ничего я вам сообщать не хочу поэтому до свидания я ничего не'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual( (None, None), res)

    def test_19(self):
        testing_address = 'новогиреевская 34'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual( ('новогиреевская', None), res)

    def test_20(self):
        testing_address = 'мое 3 парковая'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('парковая', None), res)

    def test_21(self):
        testing_address = 'москва мусы джалиля 38 корпус 2'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('мусы джалиля', None), res)

    def test_22(self):
        testing_address = 'надо 50% город нальчик горького 1257'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('горького', None), res)

    def test_23(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('каширское', 'шоссе'), res)

    def test_24(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('зеленые', 'аллеи'), res)

    def test_25(self):
        testing_address = 'дмитрия ульянова 17 корпус 1 москва'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('дмитрия ульянова', None), res)

    def test_26(self):
        testing_address = 'null'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual((None, None), res)

    def test_27(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('алтуфьевское', None), res)

    def test_28(self):
        testing_address = 'марша захарова 12 маршала захарова дом 12'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('маршала захарова', None), res)

    def test_29(self):
        testing_address = 'а зачем'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual((None, None), res)

    def test_30(self):
        testing_address = 'Кавказский 16'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('Кавказский', None), res)

    def test_31(self):
        testing_address = 'Старый Гай 1 корпус 2'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('Старый Гай'.lower(), None), (res[0].lower(), None))

    def test_32(self):
        testing_address = 'зелинского улица зелинского дом 2'
        match = (None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None)
        self.assertEqual(('зелинского', 'улица'), res)


if __name__ == '__main__':
    unittest.main()