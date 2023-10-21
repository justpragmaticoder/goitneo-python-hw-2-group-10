import unittest
from datetime import datetime, timedelta
from collections import defaultdict

from bot import *


class Test(unittest.TestCase):
    def test_add_contact_happy_flow(self):
        contacts = {}
        result = add_contact(["John", 12341231], contacts)

        self.assertEqual(contacts, {"John": 12341231})
        self.assertEqual(result, "Contact added.")

    def test_add_contact_wrong_args(self):
        contacts = {}
        result = add_contact([], contacts)

        self.assertEqual(contacts, {})
        self.assertEqual(result, "Give me name and phone please.")

    def test_change_contact_happy_flow(self):
        contacts = {"John": 12341231}
        result = change_contact(["John", 99999999], contacts)

        self.assertEqual(contacts, {"John": 99999999})
        self.assertEqual(result, "Contact updated.")

    def test_change_contact_not_found(self):
        contacts = {"Joshua": 12341231}
        result = change_contact([], contacts)

        self.assertEqual(contacts, {"Joshua": 12341231})
        self.assertEqual(result, "Give me name and phone please.")

    def test_change_contact_wrong_args(self):
        contacts = {"Joshua": 12341231}
        result = change_contact(["John", 99999999], contacts)

        self.assertEqual(result, "Contact was not found.")

    def test_show_phone_happy_flow(self):
        contacts = {"Joshua": 12341231}
        result = show_phone(["Joshua"], contacts)

        self.assertEqual(result, 12341231)

    def test_show_phone_not_found(self):
        contacts = {"Joshua": 12341231}
        result = show_phone(["John"], contacts)

        self.assertEqual(result, "Contact was not found.")

    def test_show_phone_wrond_args(self):
        contacts = {"Joshua": 12341231}
        result = show_phone([], contacts)

        self.assertEqual(contacts, {"Joshua": 12341231})
        self.assertEqual(result, "Enter user name")

    def test_show_all(self):
        contacts = {"Joshua": 12341231, "Steve": 2857371}
        result = show_all(contacts)

        self.assertEqual(result, "Joshua: 12341231\nSteve: 2857371")
