from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    top, bot = grid
    cols = [i for i,v in enumerate(bot) if v==2]
    n = len(cols)
    m = n-1
    out = [[0]*m for _ in range(n)]
    x = m//2
    out[0][x] = 3
    for k in range(n-1):
        j = cols[k]
        out[k+1][x] = 2
        if top[j]==2 and x+1<m:
            out[k+1][x+1] = 2
            x += 1
        elif top[j]==0 and x-1>=0:
            out[k+1][x-1] = 2
            x -= 1
    return out