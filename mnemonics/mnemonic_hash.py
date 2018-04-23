from .abstract.mnemonic_hash import AbstractMnemonicHash
from .wordlist import default_wordlist


class MnemonicHash(AbstractMnemonicHash):
    wordlist = default_wordlist
