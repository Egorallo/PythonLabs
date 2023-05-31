import unittest

from package.basicjsonserializer import JSONSerializer
from package.basicxmlserializer import XMLSerializer


class JSONDataStructuresCase(unittest.TestCase):
    json_serializer: JSONSerializer = JSONSerializer()
    xml_serializer: XMLSerializer = XMLSerializer()

    def test_empty(self):
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps({})), {})
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps({})), {})

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(())), ())
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps(())), ())

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps([])), [])
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps([])), [])

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(set())), set())
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps(set())), set())

    def test_single_value(self):
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps({"900": 900})), {"900": 900})
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps({"900": 900})), {"900": 900})

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(([2, 900]))), ([2, 900]))
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps(([2, 900]))), ([2, 900]))

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps([900])), [900])
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps([900])), [900])

        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps({90, 900})), {90, 900})
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps({90, 900})), {90, 900})

    def test_nested(self):
        test = {
            1: 2,
            3: ["test", [], True],
            2: {
                6: {1, 2, 3},
                8: {
                    9: "GG",
                   "hell nah": (12, 21)
                },
            }
        }
        self.assertEqual(self.json_serializer.loads(self.json_serializer.dumps(test)), test)
        self.assertEqual(self.xml_serializer.loads(self.xml_serializer.dumps(test)), test)


if __name__ == '__main__':
    unittest.main()












