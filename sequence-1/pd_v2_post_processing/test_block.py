import unittest
from block import __main__

class TestBlock(unittest.TestCase):

    def test_main_success(self):
        result = __main__(probability=0.40)
        self.assertEqual(result, {"grade": "B1"})

    def test_main_invalid_input(self):
        with self.assertRaises(ValueError):
            __main__(probability="0.40")

if __name__ == "__main__":
    unittest.main()
