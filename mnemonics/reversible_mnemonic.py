from .abstract import AbstractReversibleMnemonic
from .wordlist import default_wordlist


class ReversibleMnemonic(AbstractReversibleMnemonic):
    wordlist = default_wordlist
