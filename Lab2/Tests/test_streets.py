import unittest

from NER.engine.AddressNERHypothesis import AddressNERHypothesis
from NER.engine.NERModel import NERModel


class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = NERModel()

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( ('комсомольский', 'проспект'), res.street)

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( ('катукова', 'улица'), res.street)

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('рабочая', 'улица'), res.street)

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('доватора', None), res.street)

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('бехтеева', None), res.street)

    def test_6(self):
        testing_address = 'улица меркулова дом 24'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('меркулова', 'улица'), res.street)

    def test_7(self):
        testing_address = 'октябрьская 48 частный дом город сургут'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('октябрьская', None), res.street)

    def test_8(self):
        testing_address = 'сколько улица 30 лет победы 50 46'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('30 лет победы', 'улица'), res.street)

    def test_9(self):
        testing_address = 'тюменский тракт 10'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('тюменский', 'тракт'), res.street)

    def test_10(self):
        testing_address = 'сургут югорская 30/2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('югорская', None), res.street)

    def test_11(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual((None, None), res.street)

    def test_12(self):
        testing_address = 'старый оскол микрорайон олимпийский дом 23 квартира 105'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('олимпийский', 'микрорайон'), res.street)

    def test_13(self):
        testing_address = 'город сургут улица фармана салманова 4'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( ('фармана салманова', 'улица'), res.street)

    def test_14(self):
        testing_address = 'ты сургут улица 30 лет победы'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( ('30 лет победы', 'улица'), res.street)

    def test_15(self):
        testing_address = 'проезд мунарева 2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('мунарева', 'проезд'), res.street)

    def test_16(self):
        testing_address = 'домашний адрес где я живу'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual((None, None), res.street)

    def test_17(self):
        testing_address = 'артема 32 квартира 8'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( ('артема', None), res.street)

    def test_18(self):
        testing_address = 'знаете знаете у меня дорогая девочка у меня уже все есть и менять из из одного переходить на другой я не хочу поэтому какой город квартира какой ничего я вам сообщать не хочу поэтому до свидания я ничего не'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( (None, None), res.street)

    def test_19(self):
        testing_address = 'новогиреевская 34'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( ('новогиреевская', None), res.street)

    def test_20(self):
        testing_address = 'мое 3 парковая'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('парковая', None), res.street)

    def test_21(self):
        testing_address = 'москва мусы джалиля 38 корпус 2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('мусы джалиля', None), res.street)

    def test_22(self):
        testing_address = 'надо 50% город нальчик горького 1257'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('горького', None), res.street)

    def test_23(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('каширское', 'шоссе'), res.street)

    def test_24(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('зеленые', 'аллеи'), res.street)

    def test_25(self):
        testing_address = 'дмитрия ульянова 17 корпус 1 москва'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('дмитрия ульянова', None), res.street)

    def test_26(self):
        testing_address = 'null'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual((None, None), res.street)

    def test_27(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('алтуфьевское', None), res.street)

    def test_28(self):
        testing_address = 'марша захарова 12 маршала захарова дом 12'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('маршала захарова', None), res.street)

    def test_29(self):
        testing_address = 'а зачем'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual((None, None), res.street)

    def test_30(self):
        testing_address = 'Кавказский 16'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('Кавказский', None), res.street)

    def test_31(self):
        testing_address = 'Старый Гай 1 корпус 2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('Старый Гай'.lower(), None), (res.street[0].lower(), None))

    def test_32(self):
        testing_address = 'зелинского улица зелинского дом 2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('зелинского', 'улица'), res.street)


if __name__ == '__main__':
    unittest.main()
