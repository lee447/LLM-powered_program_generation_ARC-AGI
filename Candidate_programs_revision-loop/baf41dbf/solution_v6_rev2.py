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
    new_min_x = min(lefts)+1 if lefts else min_x
    new_max_x = max(rights)-1 if rights else max_x
    new_min_y = min(tops)+1 if tops else min_y
    new_max_y = max(bots)-1 if bots else max_y
    if lefts and rights:
        width = new_max_x - new_min_x + 1
        new_max_y = new_min_y + width - 1
    if tops and bots:
        height = new_max_y - new_min_y + 1
        new_max_x = new_min_x + height - 1
    new_min_x = max(0, new_min_x)
    new_min_y = max(0, new_min_y)
    new_max_x = min(w-1, new_max_x)
    new_max_y = min(h-1, new_max_y)
    vert = [j for j in range(min_x+1, max_x) if all(grid[i][j]==3 for i in range(min_y, max_y+1))]
    horz = [i for i in range(min_y+1, max_y) if all(grid[i][j]==3 for j in range(min_x, max_x+1))]
    out = [row[:] for row in grid]
    for i,j in shape:
        out[i][j] = 0
    for j in range(new_min_x, new_max_x+1):
        out[new_min_y][j] = 3
        out[new_max_y][j] = 3
    for i in range(new_min_y, new_max_y+1):
        out[i][new_min_x] = 3
        out[i][new_max_x] = 3
    for j in vert:
        for i in range(new_min_y, new_max_y+1):
            out[i][j] = 3
    for i in horz:
        for j in range(new_min_x, new_max_x+1):
            out[i][j] = 3
    return out