def solve(puzzle):
    words = puzzle.split()
    letters = set(''.join(words))
    n = len(letters)
    char_to_int = dict(zip(letters, range(10)))
        
    for permutation in range(10**n):
        char_to_int.update(zip(letters, map(int, str(permutation).zfill(n))))
        if sum(int(word) for word in words[-1]) == int(words[-1]):
            return char_to_int
    return None