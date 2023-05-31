import unittest

from package.basicjsonserializer import JSONSerializer
from package.basicxmlserializer import XMLSerializer


class PrimitiveTypes(unittest.TestCase):
    json_serializer = JSONSerializer()
    xml_serializer = XMLSerializer()

    def test_json_dumps(self):
        self.assertEqual(self.json_serializer.dumps("900"), '"900"')
        self.assertEqual(self.json_serializer.dumps(900), "900")
        self.assertEqual(self.json_serializer.dumps(900.0), "900.0")
        self.assertEqual(self.json_serializer.dumps(9j + 12), "(12+9j)")
        self.assertEqual(self.json_serializer.dumps("test"), '"test"')
        self.assertEqual(self.json_serializer.dumps(False), "false")
        self.assertEqual(self.json_serializer.dumps(""), '""')

    def test_json_loads(self):
        self.assertEqual(self.json_serializer.loads('"900"'), "900")
        self.assertEqual(self.json_serializer.loads("900"), 900)
        self.assertEqual(self.json_serializer.loads("900.0"), 900.0)
        self.assertEqual(self.json_serializer.loads("(12+9j)"), 12 + 9j)
        self.assertEqual(self.json_serializer.loads("false"), False)
        self.assertEqual(self.json_serializer.loads('"test"'), "test")
        self.assertEqual(self.json_serializer.loads('""'), "")
        self.assertEqual(self.json_serializer.loads(""), None)

    def test_json_xml_dumps_and_loads(self):
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps("900")), "900")
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps("900")), "900")

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(900)), 900)
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps(900)), 900)

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(900.0)), 900.0)
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps(900.0)), 900.0)

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(9 + 12j)), 9 + 12j)
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps(9 + 12j)), 9 + 12j)

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps("test")), "test")
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps("test")), "test")

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(False)), False)
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps(False)), False)

    def test_dump_and_load(self):
        with (open("filefrom.txt", "w+") as f, open("filefrom.txt", "r") as t):
            self.json_serializer.dump("900", f)
            f.seek(0)
            self.assertEqual(self.json_serializer.load(t), '900')

        with (open("filefrom.txt", "w+") as f, open("filefrom.txt", "r") as t):
            self.json_serializer.dump(900, f)
            f.seek(0)
            self.assertEqual(self.json_serializer.load(t), 900)

        with (open("filefrom.txt", "w+") as f, open("filefrom.txt", "r") as t):
            self.json_serializer.dump(900.0, f)
            f.seek(0)
            self.assertEqual(self.json_serializer.load(t), 900.0)

        with (open("filefrom.txt", "w+") as f, open("filefrom.txt", "r") as t):
            self.json_serializer.dump(9 + 12j, f)
            f.seek(0)
            self.assertEqual(self.json_serializer.load(t), 12j + 9)

        with (open("filefrom.txt", "w+") as f, open("filefrom.txt", "r") as t):
            self.json_serializer.dump(True, f)
            f.seek(0)
            self.assertEqual(self.json_serializer.load(t), True)

        with (open("filefrom.txt", "w+") as f, open("filefrom.txt", "r") as t):
            self.json_serializer.dump("test", f)
            f.seek(0)
            self.assertEqual(self.json_serializer.load(t), "test")


if __name__ == '__main__':
    unittest.main()
