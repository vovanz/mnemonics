import re
from uuid import UUID

from mnemonics.abstract.iterable_to_string import IterableToString
from mnemonics.wordlist import default_wordlist


class ReversibleMnemonic(IterableToString):
    wordlist = default_wordlist
    wordlist_length = len(wordlist)
    wordlist_indexes = {
        word.lower(): index for index, word in enumerate(wordlist)
    }

    @classmethod
    def _parse_mnemonic_string_iter(cls, mnemonic_string):
        mnemonic_string = re.sub('[^a-z]', '', mnemonic_string.lower())

        i = 0
        for j in range(len(mnemonic_string)):
            prefix = mnemonic_string[i:j]
            if prefix in cls.wordlist_indexes:
                yield prefix
                i = j
        yield mnemonic_string[i:]

    def _generate_mnemonic_from_int(self):
        integer = int(self._int)

        while integer > 0:
            selected_word = self.wordlist[integer % self.wordlist_length]
            integer //= self.wordlist_length
            self._mnemonic_list.append(selected_word)

    def _restore_int_from_list(self):
        multiplier = 1
        for word in self._mnemonic_list:
            self._int += self.wordlist_indexes[word] * multiplier
            multiplier *= self.wordlist_length

    def __init__(self, integer=None, mnemonic_string=None, mnemonic_iterable=None):
        if [integer, mnemonic_string, mnemonic_iterable].count(None) != 2:
            raise TypeError(
                'Exactly one of the arguments (integer, mnemonic_string, mnemonic_iter) must be given.'
            )

        if integer is not None:
            self._int = abs(integer)
            self._mnemonic_list = []
            if not isinstance(integer, int):
                raise TypeError('Argument integer must be an instance of int.')
            self._generate_mnemonic_from_int()

        if mnemonic_string is not None:
            mnemonic_iterable = self._parse_mnemonic_string_iter(mnemonic_string)

        if mnemonic_iterable is not None:
            self._mnemonic_list = list(mnemonic_iterable)
            self._int = 0
            self._restore_int_from_list()

    def __int__(self):
        return self._int

    @property
    def integer(self):
        return self._int

    @property
    def uuid(self):
        return UUID(int=self._int)

    def __iter__(self):
        return iter(self._mnemonic_list)

    def __repr__(self):
        return '{}(mnemonic_string={})'.format(self.__class__.__name__, repr(self.lisp_case))

    @classmethod
    def from_integer(cls, integer):
        return cls(integer=integer)

    @classmethod
    def from_iterable(cls, iterable):
        return cls(mnemonic_iterable=iterable)

    @classmethod
    def from_string(cls, string):
        return cls(mnemonic_string=string)

    @classmethod
    def from_uuid(cls, uuid):
        return cls(integer=uuid.int)
