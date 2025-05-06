from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    bs = h
    n = w // bs
    res = [[] for _ in range(h)]
    for b in range(n):
        j0 = b * bs
        B = [row[j0:j0+bs] for row in grid]
        s5 = sum(1 for i in range(bs) for j in range(bs) if B[i][j] == 5)
        if s5 == bs*bs - 1 and B[bs//2][bs//2] == 0:
            c = 3
        elif s5 == bs and B[1][1] == 5 and B[0][bs-1] == 5 and B[bs-1][0] == 5:
            c = 9
        elif s5 == 1 and B[1][1] == 5:
            c = 4
        elif B[0] == [5]*bs and all(all(x==0 for x in B[i]) for i in range(1,bs)):
            c = 6
        elif B[0] == [5]*bs and B[bs-1] == [5]*bs and all(x==0 for x in B[1]):
            c = 6
        elif B[bs-1] == [5]*bs and all(all(x==0 for x in B[i]) for i in range(bs-1)):
            c = 1
        else:
            c = 0
        for i in range(h):
            res[i].extend([c]*bs)
    return res