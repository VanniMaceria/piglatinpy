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

    #user story #3 - first case
    def test_translate_phrase_starting_with_vowel_and_ending_with_y(self):
        translator = PigLatinTranslator("any")
        translation = translator.translate()
        self.assertEqual(translation, "anynay")

    #user story #3 - second case
    def test_translate_phrase_ending_with_vowel(self):
        translator = PigLatinTranslator('apple')
        translation = translator.translate()
        self.assertEqual(translation, "appleyay")

    #user story #3 - third case
    def test_translate_phrase_ending_with_consonant(self):
        translator = PigLatinTranslator('ask')
        translation = translator.translate()
        self.assertEqual(translation, "askay")

    #user story #4
    def test_translate_phrase_starting_with_consonant(self):
        translator = PigLatinTranslator("hello")
        translation = translator.translate()
        self.assertEqual(translation, "ellohay")

    #user story #4 - altro test per essere sicuro
    def test_translate_phrase_starting_with_consonant_c(self):
        translator = PigLatinTranslator("come")
        translation = translator.translate()
        self.assertEqual(translation, "omecay")

    #user story #5
    def test_translate_phrase_starting_with_more_than_one_consonant(self):
        translator = PigLatinTranslator("known")
        translation = translator.translate()
        self.assertEqual(translation, "ownknay")

    #user story #5 - altro test
    def test_translate_phrase_starting_with_more_than_one_consonant_2(self):
        translator = PigLatinTranslator("knebworth")
        translation = translator.translate()
        self.assertEqual(translation, "ebworthknay")

    #user story #6
    def test_translate_phrase_with_more_than_one_word(self):
        translator = PigLatinTranslator("hello world")
        translation = translator.translate()
        self.assertEqual(translation, "ellohay orldway")

    # user story #6 - test con '-'
    def test_translate_phrase_with_more_than_one_word_with_dash(self):
        translator = PigLatinTranslator("well-being")
        translation = translator.translate()
        self.assertEqual(translation, "ellway-eingbay")


