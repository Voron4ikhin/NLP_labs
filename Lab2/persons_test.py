import unittest
from yargy import rule, or_, and_, not_, Parser
from yargy.interpretation import fact
from yargy.predicates import gram
from yargy.relations import gnc_relation




gnc = gnc_relation()
name = ['first', 'middle', 'last']
Name = fact('Name', name)
default = Name(first=None, middle=None, last=None)
FIRST = gram('Name').interpretation(Name.first).match(gnc)
MIDDLE = gram('Patr').interpretation(Name.middle).match(gnc)
LAST = and_(gram('Surn'), not_(gram('Abbr'))).interpretation(Name.last).match(gnc)
FULL_NAME_1 = rule(LAST, FIRST, MIDDLE)
FULL_NAME_2 = rule(FIRST, MIDDLE, LAST)
FIRST_MIDDLE = rule(FIRST, MIDDLE)
MIDDLE_FIRST = rule(MIDDLE, FIRST)
FIRST_LAST = rule(FIRST, LAST)
LAST_FIRST = rule(LAST, FIRST)
ONLY_FIRST = rule(FIRST)
ONLY_MIDDLE = rule(MIDDLE)
ONLY_LAST = rule(LAST)


FINAL_NAME = or_(FULL_NAME_1, FULL_NAME_2, FIRST_MIDDLE, FIRST_LAST, MIDDLE_FIRST, LAST_FIRST, ONLY_LAST, ONLY_FIRST, ONLY_MIDDLE).interpretation(Name)
parser = Parser(FINAL_NAME)
'''text = 'Иванов Петр Васильевич'

for match in parser.findall(text):
    print(match.fact.first)'''


class TestPersons(unittest.TestCase):
    def test_1(self):
        testing_address = 'Иванов Петр Васильевич'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, 'Петр')
        self.assertEqual(res.middle, 'Васильевич')
        self.assertEqual(res.last, 'Иванов')
    def test_2(self):
        testing_address = 'шипицын дмитрий вячеславович'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, 'дмитрий')
        self.assertEqual(res.middle, 'вячеславович')
        self.assertEqual(res.last, 'шипицын')

    def test_3(self):
        testing_address = 'елена владимировна'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, 'елена')
        self.assertEqual(res.middle, 'владимировна')
        self.assertEqual(res.last, None)

    def test_4(self):
        testing_address = 'басалаева юлия михайловна'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, 'юлия')
        self.assertEqual(res.middle, 'михайловна')
        self.assertEqual(res.last, 'басалаева')

    def test_5(self):
        testing_address = 'ну я как раз по фамилии есть смотри мам'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, None)
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, None)

    def test_6(self):
        testing_address = 'глушенков власти на android'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, None)
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, 'глушенков')

    def test_7(self):
        testing_address = 'фамилию сказать что за фамилия терентьева людмила'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, 'людмила')
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, 'терентьева')

    def test_8(self):
        testing_address = 'елена владимировна'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, 'елена')
        self.assertEqual(res.middle, 'владимировна')
        self.assertEqual(res.last, None)

    def test_9(self):
        testing_address = 'анюта'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, 'анюта')
        self.assertEqual(res.middle, None)
        self.assertEqual(res.last, None)

    def test_10(self):
        testing_address = 'р1 артем витальевич'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, 'артем')
        self.assertEqual(res.middle, 'витальевич')
        self.assertEqual(res.last, None)

    def test_11(self):
        testing_address = 'фитнес веретельников олег викторович'
        res = default if parser.find(testing_address) is None else parser.find(testing_address).fact
        self.assertEqual(res.first, 'олег')
        self.assertEqual(res.middle, 'викторович')
        self.assertEqual(res.last, 'веретельников')


if __name__ == '__main__':
    unittest.main()
