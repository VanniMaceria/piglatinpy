from unittest import TestCase

from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
       translator = PigLatinTranslator("Hello world")
       phrase = translator.get_phrase()
       self.assertEqual(phrase, "Hello world")
