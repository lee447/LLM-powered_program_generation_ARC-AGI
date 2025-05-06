from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    A = grid
    rot = [row[::-1] for row in A[::-1]]
    flipud = A[::-1]
    fliplr = [row[::-1] for row in A]
    res = []
    for r, fu in zip(rot, flipud):
        res.append(r + fu)
    for fl, row in zip(fliplr, A):
        res.append(fl + row)
    return res