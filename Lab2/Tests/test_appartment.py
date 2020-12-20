import unittest

from NER.engine.AddressNERHypothesis import AddressNERHypothesis
from NER.engine.NERModel import NERModel


class TestAppartment(unittest.TestCase):
    def setUp(self):
        self.NERInstance = NERModel()

    def test_1(self):
        testing_address = 'проспект комсомольский 50'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.appartment, None)

    def test_2(self):
        testing_address = 'город липецк улица катукова 36 a'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.appartment, None)

    def test_3(self):
        testing_address = 'сургут улица рабочая дом 31а'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.appartment, None)

    def test_4(self):
        testing_address = 'город липецк доватора 18'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.appartment, None)

    def test_5(self):
        testing_address = 'ну бехтеева 9 квартира 310'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.appartment, '310')

    def test_6(self):
        testing_address = 'Кусковская 19 корпус 1'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.appartment, None)

    def test_7(self):
        testing_address = 'марша захарова 12 маршала захарова дом 12'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.appartment, None)

    def test_8(self):
        testing_address = 'null'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(res.appartment, None)


if __name__ == '__main__':
    unittest.main()
