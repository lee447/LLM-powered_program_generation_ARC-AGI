from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    out = [[0]*w for _ in range(h)]
    for bi in range(0, h, 3):
        for bj in range(0, w, 3):
            b = [[grid[bi+i][bj+j] == 5 for j in range(3)] for i in range(3)]
            s = sum(b[i][j] for i in range(3) for j in range(3))
            if s == 1 and b[1][1]:
                c = 4
            elif s == 3 and b[0][2] and b[1][1] and b[2][0]:
                c = 9
            elif s == 3 and b[0][0] and b[0][1] and b[0][2]:
                c = 6
            elif s == 3 and b[2][0] and b[2][1] and b[2][2]:
                c = 1
            elif s == 8:
                c = 3
            else:
                c = 0
            for i in range(3):
                for j in range(3):
                    out[bi+i][bj+j] = c
    return out