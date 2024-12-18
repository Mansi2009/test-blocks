import unittest
from block import __main__

class TestBlock(unittest.TestCase):

    def test_main_success(self):
        result = __main__()
        self.assertEqual(result, {"bin": "B1"})

    def test_main_invalid_input(self):
        with self.assertRaises(ValueError):
            __main__(value="0.40")  # Invalid input type (string)

if __name__ == "__main__":
    unittest.main()
