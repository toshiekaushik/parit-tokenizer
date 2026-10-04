from BPE import BPETokenizerParams
from Tokenizer import Tokenizer
from TokenizerHelper import merge

class BPETokenizer(Tokenizer):
    """BPE tokenizer given a set of merges and vocabulary"""
    def __init__(self, params: BPETokenizerParams):
        self.params = params

    def encode(self, string: str) -> list[int]:
        indices = list(map(int, string.encode("utf-8")))

        # Slow implementation
        for pair, new_index in self.params.merges.items():
            indices = merge(indices, pair, new_index)

        return indices

    def decode(self, indices: list[int]) -> str:
        bytes_list = list(map(self.params.vocab.get, indices))
        string = b"".join(bytes_list).decode("utf-8")
        return string