from unittest import TestCase

from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    #user story #1
    def test_get_phrase(self):
       translator = PigLatinTranslator("Hello world")
       phrase = translator.get_phrase()
       self.assertEqual(phrase, "Hello world")

    #user story #2
    def test_translate_empty_phrase(self):
        translator = PigLatinTranslator('')
        phrase = translator.translate()
        self.assertEqual(phrase, "nil")

    #user story #3
    def test_translate_phrase_starting_with_vowel_and_ending_with_y(self):
        translator = PigLatinTranslator("any")
        translation = translator.translate()
        self.assertEqual(translation, "anynay")

