class PigLatinTranslator:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                  'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == '':
            return 'nil'

        #traduzione frase parola per parola
        if ' ' in self.phrase or '-' in self.phrase:
            return self._translate_multi_word()

        #altrimenti traduci solo la singola parola
        return self._translate_single_word(self.phrase)

    def _translate_multi_word(self) -> str:
        result = ''
        word = ''

        for char in self.phrase:
            if char.isalpha():  #controlla se il carattere che scorre è una lettera
                word += char
            else:  # char è spazio o trattino
                if word:
                    result += self._translate_single_word(word)
                    word = ''
                result += char  # manteniamo lo spazio o trattino

        # ultima parola
        if word:
            result += self._translate_single_word(word)

        return result

    def _translate_single_word(self, word: str) -> str:
        if word == '':
            return ''

        first_letter = word[0].lower()
        last_letter = word[-1].lower()

        if first_letter in self.vowels and last_letter == 'y':
            return word + 'nay'

        if first_letter in self.consonants:
            num_consonants = self.return_initial_consonants_word(word)
            consonants = word[:num_consonants]
            rest = word[num_consonants:]
            return rest + consonants + 'ay'

        if last_letter in self.vowels:
            return word + 'yay'

        return word + 'ay'

    def return_initial_consonants_word(self, word: str) -> int:
        consonants = 0
        for letter in word.lower():
            if letter in self.consonants:
                consonants += 1
            elif letter in self.vowels:
                break
        return consonants
