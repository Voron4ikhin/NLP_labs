import unittest

from NER.engine.AddressNERHypothesis import AddressNERHypothesis
from NER.engine.NERModel import NERModel


class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = NERModel()

    def test_one(self):
        testing_address = 'проспект комсомольский 50'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( ('комсомольский', 'проспект'), res.street)
        self.assertEqual(('50', None, None), res.building)


    def test_second(self):
        testing_address = 'город липецк улица катукова 36 a'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('липецк', 'город'), res.city)
        self.assertEqual( ('катукова', 'улица'), res.street)
        self.assertEqual(('36 a', None, None), res.building)


    def test_third(self):
        testing_address = 'сургут улица рабочая дом 31а'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('сургут', None), res.city)
        self.assertEqual(('рабочая', 'улица'), res.street)
        self.assertEqual(('31а', None, None), res.building)


    def test_fouth(self):
        testing_address = 'город липецк доватора 18'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('липецк', 'город'), res.city)
        self.assertEqual( ('доватора', None), res.street)
        self.assertEqual( ('18', None, None), res.building)

    def test_behtereva(self):
        testing_address =  'ну бехтеева 9 квартира 310'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( (None, None), res.city,)
        self.assertEqual(('бехтеева', None),res.street)
        self.assertEqual(('9', None, None),res.building)
        self.assertEqual('310', res.appartment )

    def test_moskovskaya(self):
        testing_address = 'московская 34б'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( (None, None), res.city)
        self.assertEqual( ('московская', None), res.street,)
        self.assertEqual(('34б', None, None), res.building)
        self.assertEqual(None, res.appartment)

    def test_minina(self):
        testing_address =  'улица минина дом 1'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual((None, None), res.city)
        self.assertEqual(('минина', 'улица'), res.street)
        self.assertEqual(('1', None, None), res.building)
        self.assertEqual( None, res.appartment)

    def test_30_let_victory(self):
        testing_address =  'сколько улица 30 лет победы 50 46'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( (None, None), res.city)
        self.assertEqual(('30 лет победы', 'улица'), res.street)
        self.assertEqual( ('50', None, None), res.building)
        self.assertEqual('46', res.appartment)

    def test_tract(self):
        testing_address =  'тюменский тракт 10'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual((None, None), res.city, )
        self.assertEqual(('тюменский', 'тракт'), res.street )
        self.assertEqual(('10', None, None), res.building )
        self.assertEqual( None, res.appartment)

    def test_beregovaya(self):
        testing_address =  'береговая 43 береговая 43 сургут'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('сургут', None), res.city)
        self.assertEqual(('береговая', None), res.street)
        self.assertEqual( ('43', None, None), res.building)
        self.assertEqual(None, res.appartment)

    def test_yuogorskaya(self):
        testing_address =  'сургут югорская 30/2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('сургут', None), res.city)
        self.assertEqual(('югорская', None), res.street)
        self.assertEqual(('30/2', None, None), res.building)
        self.assertEqual( None, res.appartment)

    def test_index(self):
        testing_address = 'индекс 12 мне вот этого не надо'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual((None, None), res.city, )
        self.assertEqual( (None, None), res.street,)
        self.assertEqual( (None, None, None), res.building,)
        self.assertEqual( None, res.appartment,)

    def test_salmanova(self):
        testing_address = 'город сургут улица фармана салманова 4'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('сургут', 'город'), res.city, )
        self.assertEqual(('фармана салманова', 'улица'), res.street, )
        self.assertEqual(('4', None, None), res.building, )
        self.assertEqual( None, res.appartment,)

    def test_vidnoe(self):
        testing_address = 'зеленые аллеи город видное дом 8'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('видное', 'город'), res.city, )
        self.assertEqual( ('зеленые аллеи', None), res.street,)
        self.assertEqual(('8', None, None), res.building, )
        self.assertEqual( None, res.appartment,)

    def test_zelinskogo(self):
        testing_address = 'зелинского улица зелинского дом 2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( (None, None), res.city,)
        self.assertEqual(('зелинского', 'улица'), res.street, )
        self.assertEqual(('2', None, None), res.building, )
        self.assertEqual( None, res.appartment,)

    def test_kuskovaya_corpus(self):
        testing_address = 'Кусковская 19 корпус 1 '
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual((None, None), res.city, )
        self.assertEqual(('Кусковская', None), res.street, )
        self.assertEqual(('19', '1', None), res.building, )
        self.assertEqual(None, res.appartment )

    def test_shosse(self):
        testing_address = 'москва щелковское шоссе 35'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('москва', None), res.city, )
        self.assertEqual(('щелковское', 'шоссе'), res.street, )
        self.assertEqual(('35', None, None), res.building, )
        self.assertEqual(None, res.appartment, )

    def test_park(self):
        testing_address = 'город москва марьинский парк дом 25 корпус 2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( ('москва', 'город'), res.city,)
        self.assertEqual( ('марьинский парк', None), res.street,)
        self.assertEqual(('25', '2', None), res.building, )
        self.assertEqual(None, res.appartment, )

    def test_gai(self):
        testing_address = 'Старый Гай 1 корпус 2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('Старый Гай'.lower(), None), (res.street[0].lower(), None))
        self.assertEqual( ('1', '2', None), res.building)
        self.assertEqual( None, res.appartment,)

    def test_third_post(self):
        testing_address = 'улица 3 почтовое отделение дом 62'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual((None, None), res.city, )
        self.assertEqual(('3 почтовое отделение', 'улица'), res.street, )
        self.assertEqual(('62', None, None), res.building, )
        self.assertEqual(None, res.appartment, )

    def test_july_street(self):
        testing_address = 'нижний новгород улица июльских дней 19'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( ('нижний новгород', None), res.city,)
        self.assertEqual(('июльских дней', 'улица'), res.street, )
        self.assertEqual(('19', None, None), res.building, )
        self.assertEqual(None, res.appartment, )

    def test_val(self):
        testing_address = 'так москва хамовнический вал но я думаю что я еще обсужу со своими домашними то есть вот у нас цифровое телевидение есть но акадо вот вы не спешите я тогда вам наберу но либо в приложения'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual(('москва', None), res.city, )
        self.assertEqual(('хамовнический вал', None), res.street, )
        self.assertEqual((None, None, None), res.building, )
        self.assertEqual(None, res.appartment, )

    def test_semen_bilecky(self):
        testing_address = 'город сургут улица семена билецкого 1'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        self.assertEqual( ('сургут', 'город'), res.city,)
        self.assertEqual(('семена билецкого', 'улица'), res.street, )
        self.assertEqual(('1', None, None), res.building, )
        self.assertEqual( None, res.appartment,)


    def test_critical(self):
        testing_address = 'улица значит антонова овсиенко дом 19/2'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        print(testing_address, res)
        self.assertEqual(('антонова овсиенко', 'улица'), res.street )
        self.assertEqual(('19/2', None, None), res.building, )

    def test_critical0(self):
        testing_address = 'улица генерала армии епишева дом 9'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        print(testing_address, res)
        self.assertEqual(('генерала армии епишева', 'улица'), res.street )
        self.assertEqual(('9', None, None), res.building, )


    def test_critical1(self):
        testing_address = 'улица академика байкова дом 9'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        print(testing_address, res)
        self.assertEqual(('9', None, None), res.building, )
        self.assertEqual(('академика байкова', 'улица'), res.street )

    def test_critical2(self):
        testing_address = 'улица академика байкова дом дом дом 9'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        print(testing_address, res)
        self.assertEqual(('9', None, None), res.building, )
        self.assertEqual(('академика байкова', 'улица'), res.street )

    def test_critical2_3(self):
        testing_address = 'улица подзаборного байкова дом дом дом 9'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        print(testing_address, res)
        self.assertEqual(('9', None, None), res.building, )
        self.assertEqual(('подзаборного байкова', 'улица'), res.street )

    def test_critical2_4(self):
        testing_address = 'улица монтажника байкова дом дом дом 9'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        print(testing_address, res)
        self.assertEqual(('9', None, None), res.building, )
        self.assertEqual(('монтажника байкова', 'улица'), res.street )

    def test_critical3(self):
        testing_address = 'такзначит у меня дом номер 12 а улица джона рида'
        addressNER = AddressNERHypothesis(testing_address)
        res: AddressNERHypothesis = self.NERInstance.predict(addressNER)
        print(testing_address, res)
        self.assertEqual(('джона рида', 'улица'), res.street)
        self.assertEqual(('12', None, None), res.building, )

if __name__ == '__main__':
    unittest.main()