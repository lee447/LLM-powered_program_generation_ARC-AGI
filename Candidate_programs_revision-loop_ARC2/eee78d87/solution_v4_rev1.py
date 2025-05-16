from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    k = n - 1
    B = [[0,1,1],[0,1,1],[0,0,0]]
    def rot(tile):
        return [ [tile[2-j][i] for j in range(3)] for i in range(3) ]
    out = [[0]*(k*3+1) for _ in range(k*3+1)]
    for i in range(1,n):
        for j in range(1,n):
            base = B
            s = (i+j)%2
            if s==1:
                base = rot(base)
            c = 7 if grid[i][j]==7 else 9
            r0 = (i-1)*3
            c0 = (j-1)*3
            for di in range(3):
                for dj in range(3):
                    if base[di][dj]==1:
                        out[r0+di][c0+dj] = c
    return out