from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    b = grid[0][0]
    m = (n-1)*3 + 1
    out = [[0]*m for _ in range(m)]
    B = [[0,0,0],[0,1,1],[0,1,1]]
    def rot(t):
        return [[t[3-1-j][i] for j in range(3)] for i in range(3)]
    B2 = rot(B)
    for i in range(n-1):
        for j in range(n-1):
            c = 9 if grid[i][j] != b else 0
            if c:
                base = B if (i+j)%2==0 else B2
                r0, c0 = i*3, j*3
                for di in range(3):
                    for dj in range(3):
                        if base[di][dj]:
                            out[r0+di][c0+dj] = c
    for i in range(m):
        if i%3==0:
            for j in range(m):
                out[i][j] = b
                out[j][i] = b
    return out