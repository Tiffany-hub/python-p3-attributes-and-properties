# person_test.py
import io
import sys
import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def test_is_class(self):
        '''is a class with the name "Person".'''
        person_instance = Person(name='Guido', job='Sales')
        self.assertIsInstance(person_instance, Person)

    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person_instance = Person(name="", job="Sales")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(), "Name must be string between 1 and 25 characters.")

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person_instance = Person(name=123, job="Sales")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(), "Name must be string between 1 and 25 characters.")

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person_instance = Person(name="What do Persons do on their day off? Can't lie around - that's their job.", job="Sales")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(), "Name must be string between 1 and 25 characters.")

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        person_instance = Person(name="Guido", job="Sales")
        self.assertEqual(person_instance.name, "Guido")

    def test_valid_name_title_case(self):
        '''converts name to title case and saves if between 1 and 25 characters'''
        person_instance = Person(name="guido van rossum", job="Sales")
        self.assertEqual(person_instance.name, "Guido Van Rossum")

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person_instance = Person(job="Benevolent dictator for life")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue().strip(), "Job must be in list of approved jobs.")

    def test_job_in_list(self):
        '''saves job if in job list.'''
        person_instance = Person(job="ITC")
        self.assertEqual(person_instance.job, "ITC")

if __name__ == '__main__':
    unittest.main()
