import unittest

from NER.engine.AddressNERHypothesis import AddressNERHypothesis
from NER.engine.NERModel import NERModel


class TestHome(unittest.TestCase):
    def setUp(self):
        self.NERInstance = NERModel()

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('50', None, None))

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('36 a', None, None))

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('31а', None, None))

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('18', None, None))

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('9', None, None))

    def test_6(self):
        testing_address = 'артема 32 квартира 8'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('32', None, None))

    def test_7(self):
        testing_address = 'город липецк полиграфическая дом 4'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('4', None, None))

    def test_8(self):
        testing_address = 'сколько стоит нет arkadata у нас есть москва каширское шоссе 55 корпус 1'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('55', '1', None))

    def test_9(self):
        testing_address = 'люберцы октябрьский проспект 10 корпус 1'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('10', '1', None))

    def test_10(self):
        testing_address = 'бульвар миттова 24'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('24', None, None))

    def test_11(self):
        testing_address = 'стол вы знаете москва алтуфьевское 78'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.building, ('78', None, None))


if __name__ == '__main__':
    unittest.main()
