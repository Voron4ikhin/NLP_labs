import unittest
from yargy import rule, or_, and_, Parser
from yargy.predicates import gte, lte
from yargy.interpretation import fact
from yargy.predicates import dictionary, in_caseless
from yargy.pipelines import morph_pipeline

from someinfo import *



#address
address = ['nameCity', 'typeCity', 'nameStreet', 'typeStreet', 'numberBuilding', 'numberCorp', 'typeBuilding', 'numberApparts']
Address = fact('Address', address)
default = Address(nameCity=None, typeCity=None,nameStreet=None,typeStreet=None, numberBuilding=None, numberCorp=None, typeBuilding=None, numberApparts=None)

CITY_NAME = dictionary(cities_names).interpretation(Address.nameCity)
CITY_NAME_COMPLEX = morph_pipeline(cities_names).interpretation(Address.nameCity)
CITY_TYPE = dictionary(cities_types).interpretation(Address.typeCity)
STREET_NAME = dictionary(streets_name).interpretation(Address.nameStreet)
STREET_NAME_COMPLEX = morph_pipeline(streets_name).interpretation(Address.nameStreet)
STREET_TYPE = dictionary(streets_type).interpretation(Address.typeStreet)
LETTER = in_caseless(set('абвгдеёжзийклмнопрстуфхцчшщьыъэюя'))
NUMBER = rule(and_(gte(1), lte(1000)), LETTER.optional())
BUILDING_NUMBER = or_(rule(NUMBER, LETTER), rule(NUMBER)).interpretation(Address.numberBuilding)
STREET_TYPE2 = dictionary(building_type)
BUILDING_TYPE = dictionary(streets_name)
CORP_TYPE = dictionary(corp_type)
CORP_NUMBER = NUMBER.interpretation(Address.numberCorp)
NUMBER = rule(and_(gte(1), lte(100000))).interpretation(Address.numberApparts)
APARTMENT_TYPE = dictionary(apartment_type)

#FINAL STRING
CITY_STREET_BUILDING_APARTMENT_1 = rule(CITY_NAME, STREET_NAME, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_2 = rule(CITY_NAME_COMPLEX, STREET_NAME, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_3 = rule(CITY_NAME, STREET_NAME_COMPLEX, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_4 = rule(CITY_NAME_COMPLEX, STREET_NAME_COMPLEX, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_5 = rule(CITY_TYPE, CITY_NAME, STREET_NAME, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_6 = rule(CITY_TYPE, CITY_NAME_COMPLEX, STREET_NAME, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_7 = rule(CITY_TYPE, CITY_NAME, STREET_NAME_COMPLEX, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_8 = rule(CITY_TYPE, CITY_NAME_COMPLEX, STREET_NAME_COMPLEX, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_9 = rule(CITY_NAME, CITY_TYPE, STREET_NAME, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_10 = rule(CITY_NAME_COMPLEX, CITY_TYPE, STREET_NAME, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_11 = rule(CITY_NAME, CITY_TYPE, STREET_NAME_COMPLEX, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)
CITY_STREET_BUILDING_APARTMENT_12 = rule(CITY_NAME_COMPLEX, CITY_TYPE, STREET_NAME_COMPLEX, BUILDING_TYPE, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER, APARTMENT_TYPE, NUMBER)

STREET_BUILDING_1 = rule(STREET_TYPE, STREET_NAME, BUILDING_NUMBER)
CITY_STREET_BUILDING_1 = rule(CITY_TYPE, CITY_NAME, STREET_TYPE, STREET_NAME, BUILDING_NUMBER)
CITY_STREET_BUILDING_2 = rule(CITY_NAME, STREET_TYPE, STREET_NAME, STREET_TYPE2, BUILDING_NUMBER)
CITY_STREET_BUILDING_3 = rule(CITY_TYPE, CITY_NAME, STREET_NAME, BUILDING_NUMBER)
STREET_BUILDING_APARTMENT_1 = rule(STREET_NAME, BUILDING_NUMBER, APARTMENT_TYPE, NUMBER)
STREET_BUILDING_2 = rule(STREET_NAME, BUILDING_NUMBER)
STREET_BUILDING_3 = rule(STREET_TYPE, STREET_NAME, STREET_TYPE2, BUILDING_NUMBER)
STREET_BUILDING_APARTMENT_2 = rule(STREET_TYPE, STREET_NAME_COMPLEX, BUILDING_NUMBER, NUMBER)
STREET_BUILDING_4 = rule(STREET_NAME_COMPLEX, BUILDING_NUMBER)
CITY_STREET_BUILDING_4 = rule(STREET_NAME, BUILDING_NUMBER, CITY_NAME)
CITY_STREET_BUILDING_5 = rule(CITY_TYPE, CITY_NAME, STREET_TYPE, STREET_NAME_COMPLEX, BUILDING_NUMBER)
CITY_STREET_BUILDING_6 = rule(STREET_NAME_COMPLEX, CITY_TYPE, CITY_NAME, STREET_TYPE2, BUILDING_NUMBER)
STREET_BUILDING_5 = rule(STREET_NAME, STREET_TYPE, STREET_TYPE2, BUILDING_NUMBER)
STREET_BUILDING_6 = rule(STREET_NAME, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER)
CITY_STREET_BUILDING_7 = rule(CITY_NAME, STREET_NAME, STREET_TYPE, BUILDING_NUMBER)
CITY_STREET_BUILDING_8 = rule(CITY_TYPE, CITY_NAME, STREET_NAME_COMPLEX, STREET_TYPE2, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER)
STREET_BUILDING_7 = rule(STREET_NAME_COMPLEX, BUILDING_NUMBER, CORP_TYPE, CORP_NUMBER)
STREET_BUILDING_8 = rule(STREET_TYPE, STREET_NAME_COMPLEX, STREET_TYPE2, BUILDING_NUMBER)
CITY_STREET_BUILDING_9 = rule(CITY_NAME_COMPLEX, STREET_TYPE, STREET_NAME_COMPLEX, BUILDING_NUMBER)
CITY_STREET = rule(CITY_NAME, STREET_NAME_COMPLEX)
CITY_STREET_BUILDING_10 = rule(CITY_TYPE, CITY_NAME, STREET_TYPE, STREET_NAME_COMPLEX, BUILDING_NUMBER)
STREET_BUILDING_9 = rule(STREET_TYPE, STREET_NAME_COMPLEX, STREET_TYPE2, BUILDING_NUMBER)
STREET_BUILDING_10= rule(STREET_TYPE2, BUILDING_NUMBER, STREET_TYPE, STREET_NAME_COMPLEX)
CITY_STREET_BUILDING_11 = rule(STREET_NAME, BUILDING_NUMBER, CITY_NAME)
STREET_BUILDING_11 = rule(STREET_NAME, STREET_TYPE, BUILDING_NUMBER)

FINAL_STRING = or_(STREET_BUILDING_1, STREET_BUILDING_2, STREET_BUILDING_3, STREET_BUILDING_4, STREET_BUILDING_5,
                   STREET_BUILDING_6, STREET_BUILDING_7, STREET_BUILDING_8, STREET_BUILDING_9, STREET_BUILDING_10,
                   CITY_STREET_BUILDING_1, CITY_STREET_BUILDING_2, CITY_STREET_BUILDING_3,
                   CITY_STREET_BUILDING_4, CITY_STREET_BUILDING_5, CITY_STREET_BUILDING_6,
                   CITY_STREET_BUILDING_7, CITY_STREET_BUILDING_8, CITY_STREET_BUILDING_9,
                   CITY_STREET_BUILDING_10,CITY_STREET_BUILDING_11, STREET_BUILDING_APARTMENT_1,
                   STREET_BUILDING_APARTMENT_2, CITY_STREET, STREET_BUILDING_11).interpretation(Address)


parser = Parser(FINAL_STRING)

text = '''проспект комсомольский 50'''
for match in parser.findall(text):
    print(match.fact)

class TestStreet(unittest.TestCase):
    def test_one(self):
        testing_address = 'проспект комсомольский 50'
        match = (None, None, None, None, None, None, None, None) if parser.find(testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, 'комсомольский', 'проспект', '50', None, None, None), res)


    def test_second(self):
        testing_address = 'город липецк улица катукова 36 а'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('липецк', 'город', 'катукова', 'улица', '36 а', None, None, None), res)


    def test_third(self):
        testing_address = 'сургут улица рабочая дом 31а'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('сургут', None, 'рабочая', 'улица', '31а', None, None, None), res)


    def test_fouth(self):
        testing_address = 'город липецк доватора 18'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('липецк', 'город', 'доватора', None, '18', None, None, None), res)

    def test_behtereva(self):
        testing_address =  'ну бехтеева 9 квартира 310'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, 'бехтеева', None, '9', None, None, '310'), res)

    def test_moskovskaya(self):
        testing_address = 'московская 34б'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, 'московская', None, '34б', None, None, None), res)

    def test_minina(self):
        testing_address =  'улица минина дом 1'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, 'минина', 'улица', '1', None, None, None), res)

    def test_30_let_victory(self):
        testing_address =  'сколько улица 30 лет победы 50 46'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, '30 лет победы', 'улица', '50', None, None, '46'), res)

    def test_tract(self):
        testing_address =  'тюменский тракт 10'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, 'тюменский', 'тракт', '10', None, None, None), res)

    def test_beregovaya(self):
        testing_address =  'береговая 43 береговая 43 сургут'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('сургут', None, 'береговая', None, '43', None, None, None), res)

    def test_yuogorskaya(self):
        testing_address =  'сургут югорская 30/2'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('сургут', None, 'югорская', None, '30/2', None, None, None), res)

    def test_index(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, None, None, None, None, None, None), res)

    def test_salmanova(self):
        testing_address = 'город сургут улица фармана салманова 4'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('сургут', 'город', 'фармана салманова', 'улица', '4', None, None, None), res)

    def test_vidnoe(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('видное', 'город', 'зеленые аллеи', None,'8', None, None, None), res)

    def test_zelinskogo(self):
        testing_address = 'зелинского улица зелинского дом 2'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, 'зелинского', 'улица', '2', None, None, None), res)

    def test_kuskovaya_corpus(self):
        testing_address = 'Кусковская 19 корпус 1 '
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, 'Кусковская', None, '19', '1', None, None), res)

    def test_shosse(self):
        testing_address = 'москва щелковское шоссе 35'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('москва', None, 'щелковское', 'шоссе', '35', None, None, None), res)

    def test_park(self):
        testing_address = 'город москва марьинский парк дом 25 корпус 2'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('москва', 'город', 'марьинский парк', None, '25', '2', None, None), res)

    def test_gai(self):
        testing_address = 'Старый Гай 1 корпус 2'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, 'Старый Гай', None, '1', '2', None, None), res)

    def test_third_post(self):
        testing_address = 'улица 3 почтовое отделение дом 62'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, '3 почтовое отделение', 'улица', '62', None, None, None), res)

    def test_july_street(self):
        testing_address = 'нижний новгород улица июльских дней 19'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('нижний новгород', None, 'июльских дней', 'улица', '19', None, None, None), res)

    def test_val(self):
        testing_address = 'так москва хамовнический вал но я думаю что я еще обсужу со своими домашними то есть вот у нас цифровое телевидение есть но акадо вот вы не спешите я тогда вам наберу но либо в приложения'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('москва', None, 'хамовнический вал', None, None, None, None, None), res)

    def test_semen_bilecky(self):
        testing_address = 'город сургут улица семена билецкого 1'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('сургут', 'город', 'семена билецкого', 'улица', '1', None, None, None), res)


    def test_critical(self):
        testing_address = 'улица значит антонова овсиенко дом 19/2'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        print(testing_address, res)
        self.assertEqual((None, None, 'антонова овсиенко', 'улица', '19/2', None, None, None), res)

    def test_critical0(self):
        testing_address = 'улица генерала армии епишева дом 9'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        print(testing_address, res)
        self.assertEqual((None, None, 'генерала армии епишева', 'улица', '9', None, None, None), res)


    def test_critical1(self):
        testing_address = 'улица академика байкова дом 9'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        print(testing_address, res)
        self.assertEqual((None, None, 'академика байкова', 'улица', '9', None, None, None), res)

    def test_critical2(self):
        testing_address = 'улица академика байкова дом дом дом 9'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        print(testing_address, res)
        self.assertEqual((None, None, 'академика байкова', 'улица', '9', None, None, None), res)

    def test_critical2_3(self):
        testing_address = 'улица подзаборного байкова дом дом дом 9'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        print(testing_address, res)
        self.assertEqual((None, None, 'подзаборного байкова', 'улица', '9', None, None, None), res)

    def test_critical2_4(self):
        testing_address = 'улица монтажника байкова дом дом дом 9'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, 'монтажника байкова', 'улица', '9', None, None, None), res)

    def test_critical3(self):
        testing_address = 'такзначит у меня дом номер 12 а улица джона рида'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        print(testing_address, res)
        self.assertEqual((None, None, 'джона рида', 'улица', '12', None, None, None), res)

    def test_shkolnaya(self):
        testing_address = 'санкт-петербург школьная 20'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('санкт-петербург', None, 'школьная', None, '20', None, None, None), res)

    def test_full_gagarina(self):
        testing_address = 'санкт-петербург юрия гагарина 22 к 2'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('санкт-петербург', None, 'юрия гагарина', None,'22', '2', None, None), res)

    def test_short_gagarina(self):
        testing_address = 'питер гагарина 22 к2'
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('питер', None, 'гагарина', None, '22', '2', None, None), res)

    def test_untolovsky(self):
        testing_address = "санкт-петербург;юнтоловский 43 корпус 1"
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('санкт-петербург', None, 'юнтоловский', None, '43', '1', None, None), res)


    def test_untolovsky_str(self):
        testing_address = "санкт-петербург юнтоловский 43 строение 1"
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual(('санкт-петербург', None, 'юнтоловский', None, '43', None, '1', None), res)

    def test_untolovsky_str(self):
        testing_address = "юнтоловский 43 ст 1"
        match = (None, None, None, None, None, None, None, None) if parser.find(
            testing_address) is None else parser.find(testing_address).fact
        res = (match.nameCity if hasattr(match, 'nameCity') else None,
               match.typeCity if hasattr(match, 'typeCity') else None,
               match.nameStreet if hasattr(match, 'nameStreet') else None,
               match.typeStreet if hasattr(match, 'typeStreet') else None,
               match.numberBuilding if hasattr(match, 'numberBuilding') else None,
               match.numberCorp if hasattr(match, 'numberCorp') else None,
               match.typeBuilding if hasattr(match, 'typeBuilding') else None,
               match.numberApparts if hasattr(match, 'numberApparts') else None)
        self.assertEqual((None, None, 'юнтоловский', None, '43',  None, '1', None), res)


if __name__ == '__main__':
    unittest.main()