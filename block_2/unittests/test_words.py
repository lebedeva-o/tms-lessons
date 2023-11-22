import datetime
import unittest
import requests

from unittest.mock import patch
from words import join_words


def mocked_get(*args, **kwargs):
    return "badger-racoon"


class TestJoinWords(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("A test beings")

    @classmethod
    def tearDownClass(cls):
        print("A test ends")

    def setUp(self):
        print("A test suite begins")

    def tearDown(self):
        print("A test suite ends")

    def test_join_words_simple(self):
        print("1")
        result = join_words("hello", "Olga")
        self.assertEqual(result, "hello-Olga")

    def test_join_words_empty(self):
        print("2")
        result = join_words(" ", "")
        self.assertEqual(result, " -")

    def test_join_words_symbols(self):
        print("3")
        result = join_words("!@", "#")
        self.assertEqual(result, "!@-#")

    def test_join_words_hyphen(self):
        print("4")
        result = join_words("- ", " -")
        self.assertEqual(result, "- - -")

    def test_join_words_numbers(self):
        print("5")
        result = join_words("42", "24")
        self.assertEqual(result, "42-24")

    @unittest.skip("skip for task")
    def test_join_words_for_skip(self):
        print("skip")
        result = join_words("python", "is a language")
        self.assertEqual(result, "python is a snake")

    @unittest.skipIf(datetime.datetime.now().weekday() in [0, 2, 4],
                     "Skip on M, W, F")
    def test_join_words_skipIF(self):
        result = join_words("Skip", "test")
        self.assertEqual(result, "Skip-test")

    @unittest.expectedFailure
    def test_join_words_failure(self):
        print("expectedFailure")
        result = join_words("python", "is a language")
        self.assertEqual(result, "python is a snake")

    @patch("requests.get", side_effect=mocked_get)
    def test_mock(self, mock):
        print("Test mock")
        response = requests.get("https://www.google.com/search?q=badger")
        self.assertEqual(response, "badger-racoon")

    # @patch("requests.get", side_effect=mocked_get)
    # def test_mock_404(self, mock):
    #     print("Test mock")
    #     response = requests.get("https://www.google.com/search?q=badger")
    #     self.assertEqual(response, 404)
