from mnemonics.wordlist import default_wordlist


class ReversibleMnemonic:
    wordlist = default_wordlist

    def __init__(self, integer=None, mnemonic=None):
        pass

    @property
    def snake_case(self):
        return ''

    @property
    def screaming_snake_case(self):
        return ''

    @property
    def camel_case(self):
        return self.upper_camel_case

    @property
    def upper_camel_case(self):
        return ''

    @property
    def lower_camel_case(self):
        return ''

    @property
    def lisp_case(self):
        return ''

    def __iter__(self):
        pass
