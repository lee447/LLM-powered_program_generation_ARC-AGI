from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    shapes = {}
    for i in range(m):
        for j in range(n):
            v = grid[i][j]
            if v != 0:
                shapes.setdefault(v, []).append((i, j))
    info = []
    for color, pts in shapes.items():
        minr = min(r for r, _ in pts)
        maxr = max(r for r, _ in pts)
        minc = min(c for _, c in pts)
        maxc = max(c for _, c in pts)
        holes = 0
        for r in range(minr+1, maxr):
            for c in range(minc+1, maxc):
                if grid[r][c] == 0:
                    holes += 1
        if holes > 0:
            info.append((minc, color, holes))
    info.sort(key=lambda x: x[0])
    out = [[0]*3 for _ in range(3)]
    row = 0
    for _, color, holes in info:
        col = 0
        placed = 0
        while placed < holes and row < 3:
            out[row][col] = color
            placed += 1
            col += 1
            if col == 3 and placed < holes:
                row += 1
                col = 0
        row += 1
    return out