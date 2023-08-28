# dog_test.py
import io
import sys
import unittest
from dog import Dog

class TestDog(unittest.TestCase):
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        dog_instance = Dog()
        dog_instance.name = ""
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(), "Name must be string between 1 and 25 characters.")

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        dog_instance = Dog()
        dog_instance.name = 123
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(), "Name must be string between 1 and 25 characters.")

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        dog_instance = Dog()
        dog_instance.name = "What do dogs do on their day off? Can't lie around - that's their job."
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(), "Name must be string between 1 and 25 characters.")

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        dog_instance = Dog()
        dog_instance.name = "Fido"
        self.assertEqual(dog_instance.name, "Fido")

    def test_breed_not_in_list(self):
        '''prints "Breed must be in list of approved breeds." if not in breed list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        dog_instance = Dog()
        dog_instance.breed = "Human"
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(), "Breed must be in list of approved breeds.")

    def test_breed_in_list(self):
        '''saves breed if in breed list.'''
        dog_instance = Dog()
        dog_instance.breed = "Pug"
        self.assertEqual(dog_instance.breed, "Pug")

if __name__ == '__main__':
    unittest.main()
