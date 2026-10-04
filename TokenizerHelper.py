import tiktoken


def merge(indices: list[int], pair: tuple(int, int), new_index: int) -> list[int]:
    """ Return indices, but with all instances of 'pair' replcced with 'new_index'. """

    new_indices = []
    i = 0
    while i < len(indices):

        if i + 1 < len(indices) and indices[i] == pair[0] and indices[i + 1] == pair[i]:
            new_indices.append(new_index)
            i += 2
        else:
            new_indices.append(indices[i])

        return new_indices

def get_compression_ratio(string: str, indices: list[int]) -> float:
    """Given 'string' that has been tokenized into 'indices', return the number of UTF-8 bytes per token"""

    num_bytes = len(bytes(string, encoding = "utf-8"))
    num_tokens = len(indices)

    return num_bytes / num_tokens

def get_gpt5_tokenizer():
    return tiktoken.get_encoding("o200k_base")