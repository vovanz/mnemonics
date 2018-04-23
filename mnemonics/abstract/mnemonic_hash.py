from random import Random

from ._iterable_to_string import IterableToString


class AbstractMnemonicHash(IterableToString):
    wordlist = None

    def __init__(self, seed, length=4):
        self._seed = seed
        self._length = length
        self._random = Random(seed)
        self._mnemonic_list = [self._random.choice(self.wordlist) for _ in range(length)]

    def __iter__(self):
        return iter(self._mnemonic_list)

    def __repr__(self):
        return '{}({}, length={})'.format(self.__class__.__name__, repr(self._seed), repr(self._length))
