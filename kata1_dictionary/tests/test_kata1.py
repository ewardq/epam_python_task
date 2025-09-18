import unittest
from contextlib import redirect_stdout
from io import StringIO
from kata1.kata1_dictionary import Dictionary, main

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.d = Dictionary()

    def test_add_and_lookup_entry(self):
        self.d.newentry("Apple", "A fruit that grows on trees")
        self.assertEqual(self.d.look("Apple"), "A fruit that grows on trees")

    def test_lookup_nonexistent_entry(self):
        self.assertEqual(self.d.look("Banana"), "Can't find entry for Banana")

    def test_key_already_present(self):
        self.d.newentry("Apple", "A fruit that grows on trees")
        self.d.newentry("Apple", "A red fruit")
        self.assertEqual(self.d.look("Apple"), "A red fruit")

    def test_add_same_value_different_keys(self):
        self.d.newentry("Orange", "A citrus fruit")
        self.d.newentry("Tangerine", "A citrus fruit")
        self.d.newentry("Grapefruit", "A citrus fruit")
        self.assertEqual(self.d.look("Orange"), "A citrus fruit")
        self.assertEqual(self.d.look("Tangerine"), "A citrus fruit")
        self.assertEqual(self.d.look("Grapefruit"), "A citrus fruit")

    def test_main_function(self):
        # Create a StringIO object to capture stdout
        with StringIO() as buffer, redirect_stdout(buffer):
            # Call the function that prints to stdout
            main()
            # Get the captured output
            output = buffer.getvalue()
            
        # Assert the captured output matches the expected value
        self.assertEqual(output, "A fruit that grows on trees\nCan't find entry for Banana\n")

if __name__ == "__main__":
    unittest.main()