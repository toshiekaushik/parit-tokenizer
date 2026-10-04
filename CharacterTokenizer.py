from Tokenizer import Tokenizer

class CharacterTokenizer(Tokenizer):
    """Represent a string as a sequeunce of Unicode code points."""
    def encode(self, string: str) -> list[int]:
        return list(map(ord, string))

    def decode(self, indices: list[int]) -> str:
        return "".join(map(chr, indices))
