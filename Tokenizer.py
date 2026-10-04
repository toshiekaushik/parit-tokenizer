from abc import ABC

class Tokenizer(ABC):
    """ABSTRACT INTERFACE FOR A TOKENIZER"""
    def encode(self, string: str) -> list[int]:
        raise NotImplementedError

    def decode(self, indices: list[int]) -> str:
        raise NotImplementedError
