from uuid import UUID

from mnemonics.reversible_mnemonic import ReversibleMnemonic


class MnemonicUUID(UUID):
    def __init__(self, *args, **kwargs):
        if 'uuid' in kwargs:
            kwargs['int'] = kwargs['uuid'].int
            kwargs['version'] = kwargs['uuid'].version
            del kwargs['uuid']
        super().__init__(*args, **kwargs)
        self.mnemonic = ReversibleMnemonic()
