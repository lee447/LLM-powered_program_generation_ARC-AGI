from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    bottom = [j for j,v in enumerate(grid[1]) if v==2]
    topset = {j for j,v in enumerate(grid[0]) if v==2}
    m = len(bottom)
    h, w = m, m-1
    out = [[0]*w for _ in range(h)]
    x = w//2
    out[0][x] = 3
    for i in range(m-1):
        b0, b1 = bottom[i], bottom[i+1]
        if grid[0][b0]==2 and grid[0][b1]==2:
            out[i+1][x] = 2
        else:
            out[i+1][x] = 2
            if x+1<w:
                out[i+1][x+1] = 2
                x += 1
    return out