import unittest
from kata3.kata3_concatenate import concatenate

class TestConcatenate(unittest.TestCase):
    def test_three_valid_word(self):
        input_list = ["yoda", "best", "has"]
        self.assertEqual(concatenate(input_list), "yes")

    def test_single_word(self):
        self.assertEqual(concatenate(["hello"]), "h")

    def test_two_words(self):
        self.assertEqual(concatenate(["abc", "xyz"]), "ay")

    def test_multiple_words(self):
        self.assertEqual(concatenate(["apple", "banana", "cherry", "dates"]), "aaee")

    def test_empty_list(self):
        self.assertEqual(concatenate([]), "")

    def test_longer_words(self):
        self.assertEqual(concatenate(["python", "is", "awesome"]), "pse")


if __name__ == "__main__":
    unittest.main()