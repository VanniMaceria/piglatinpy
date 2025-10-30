from src.error import PigLatinError


class PigLatinTranslator:

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self.phrase = phrase
        self.vowels = {'a', 'e', 'i', 'o', 'u'}
        self.consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                      'y', 'z']

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self.phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self.phrase == '':
            return 'nil'

        first_letter = self.phrase[0]
        last_letter = self.phrase[-1]

        if first_letter in self.vowels and last_letter == 'y':
            return self.phrase + 'nay'

        if first_letter in self.consonants:
            substring = self.phrase[1:] #prendi la sottostringa dal carattere 1 in poi
            return substring + first_letter + 'ay'

        if last_letter in self.vowels:
            return self.phrase + 'yay'

        if last_letter not in self.vowels:
            return self.phrase + 'ay'

        return self.phrase



