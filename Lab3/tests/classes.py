import unittest

from package.basicjsonserializer import JSONSerializer


class Dumpling:
    dumplings = 24

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def get_dumplings(cls):
        return cls.dumplings

    @staticmethod
    def sheeesh():
        return "eat raw beef"

    def simple_method(self):
        print("wowzers")

    def __len__(self):
        return self.dumplings


class DumplingEater(Dumpling):
    noteaten = 122

    def __init__(self, name):
        self.name = "SNAKEATER"

    @classmethod
    def total_dumplings(cls):
        return cls.noteaten


class Test(unittest.TestCase):
    json = JSONSerializer()

    def test_1(self):
        self.assertEqual(
            self.json.loads(self.json.dumps(Dumpling("Dobry"))).brand,
            Dumpling("Dobry").brand
        )
        self.assertEqual(
            self.json.loads(self.json.dumps(Dumpling)).sheeesh(),
            Dumpling.sheeesh()
        )

    def test_2(self):
        self.assertEqual(
            self.json.loads(self.json.dumps(Dumpling("slave"))).__len__(),
            Dumpling("slave").__len__()
        )
        self.assertEqual(
            self.json.loads(self.json.dumps(Dumpling("slave"))).simple_method(),
            Dumpling("slave").simple_method()
        )
        self.assertEqual(
            self.json.loads(self.json.dumps(Dumpling("slave"))).get_dumplings(),
            Dumpling("slave").get_dumplings()
        )

    def test_3(self):
        self.assertEqual(
            self.json.loads(self.json.dumps(DumplingEater("slave"))).total_dumplings(),
            DumplingEater("slava").total_dumplings()
        )


if __name__ == '__main__':
    unittest.main()
