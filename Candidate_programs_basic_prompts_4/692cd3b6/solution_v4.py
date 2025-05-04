from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    fives = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    holes = []
    for r, c in fives:
        for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            rr, cc = r+dr, c+dc
            if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
                holes.append((rr, cc))
                break
    (r1, c1), (r2, c2) = holes
    er, ec = r2, c1
    for rr in range(min(r1, er), max(r1, er)+1):
        if grid[rr][c1] == 0:
            grid[rr][c1] = 4
    for cc in range(min(c2, ec), max(c2, ec)+1):
        if grid[r2][cc] == 0:
            grid[r2][cc] = 4
    return grid