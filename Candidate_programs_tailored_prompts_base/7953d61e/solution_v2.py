from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    blocks = grid
    n = len(blocks)
    pi = list(range(n))[::-1]
    top = [(i, pi[i]) for i in range(n)]
    bottom = [(pi[i], i) for i in range(n)]
    pairs = top + bottom
    return [blocks[a] + blocks[b] for a, b in pairs]