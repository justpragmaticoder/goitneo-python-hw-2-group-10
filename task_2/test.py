from re import S
import unittest
from datetime import datetime, timedelta
from collections import defaultdict

from classes import *


class Test(unittest.TestCase):
    def test_record_add_phone_happy_flow(self):
        john_record = Record("John")
        john_record.add_phone("1234567890")

        self.assertEqual(john_record.phones[0].get_value(), "1234567890")

    def test_record_add_phone_empty_phone(self):
        john_record = Record("John")
        john_record.add_phone("")

        self.assertEqual(len(john_record.phones), 0)

    def test_record_edit_phone_happy_flow(self):
        john_record = Record("John")
        john_record.add_phone("1234567890")
        john_record.edit_phone("1234567890", "0987654321")

        self.assertEqual(john_record.phones[0].get_value(), "0987654321")

    def test_record_edit_phone_empty_args(self):
        john_record = Record("John")
        john_record.add_phone("1234567890")
        john_record.edit_phone("", "")

        self.assertEqual(john_record.phones[0].get_value(), "1234567890")

    def test_record_find_phone(self):
        john_record = Record("John")
        john_record.add_phone("1234567890")
        happy_flow_search = john_record.find_phone("1234567890")
        wrong_phone_search = john_record.find_phone("")

        self.assertEqual(happy_flow_search.value, "1234567890")
        self.assertEqual(wrong_phone_search, None)

    def test_address_book_add_record(self):
        record_name = "John"
        book = AddressBook()
        john_record = Record(record_name)

        john_record.add_phone("1234567890")
        book.add_record(john_record)
        book.add_record({})

        self.assertEqual(
            len(book.data.values()),
            1,
        )
        self.assertEqual(
            book.data.get(record_name).get_name().get_value(),
            record_name,
        )

    def test_address_book_find_record(self):
        record_name = "Vasyl"
        book = AddressBook()
        vasyl_record = Record(record_name)

        vasyl_record.add_phone("1234567890")
        book.add_record(vasyl_record)

        search_result = book.find(record_name)
        self.assertEqual(
            len(book.data.values()),
            1,
        )
        self.assertEqual(
            search_result.get_name().get_value(),
            record_name,
        )

    def test_address_book_delete_record(self):
        vasyl_record_name = "Vasyl"
        ivan_record_name = "Ivan"
        book = AddressBook()
        vasyl_record = Record(vasyl_record_name)
        ivan_record = Record(ivan_record_name)

        vasyl_record.add_phone("1234567890")
        book.add_record(vasyl_record)
        book.add_record(ivan_record)
        book.delete(vasyl_record_name)

        search_result = book.find(ivan_record_name)
        self.assertEqual(
            len(book.data.values()),
            1,
        )
        self.assertEqual(
            search_result.get_name().get_value(),
            ivan_record_name,
        )
