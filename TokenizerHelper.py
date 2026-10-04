
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
