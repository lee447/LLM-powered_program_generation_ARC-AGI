from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    shape = [(i,j) for i in range(h) for j in range(w) if grid[i][j]==3]
    pink = [(i,j) for i in range(h) for j in range(w) if grid[i][j]==6]
    if not shape or not pink:
        return [row[:] for row in grid]
    ys = [i for i,_ in shape]
    xs = [j for _,j in shape]
    min_y, max_y = min(ys), max(ys)
    min_x, max_x = min(xs), max(xs)
    lefts  = [j for _,j in pink if j<min_x]
    rights = [j for _,j in pink if j>max_x]
    tops   = [i for i,_ in pink if i<min_y]
    bots   = [i for i,_ in pink if i>max_y]
    new_min_x = min_x if not lefts else min(lefts)+1
    new_max_x = max_x if not rights else max(rights)-1
    new_min_y = min_y if not tops else min(tops)+1
    new_max_y = max_y if not bots else max(bots)-1
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if out[i][j]==3:
                out[i][j]=0
    for j in range(new_min_x, new_max_x+1):
        out[new_min_y][j]=3
        out[new_max_y][j]=3
    for i in range(new_min_y, new_max_y+1):
        out[i][new_min_x]=3
        out[i][new_max_x]=3
    return out