from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    stripe = next(j for j in range(cols) if all(grid[i][j] == 4 for i in range(rows)))
    left_color = None
    for i in range(rows):
        for j in range(stripe):
            if grid[i][j] != 0:
                left_color = grid[i][j]
                break
        if left_color is not None:
            break
    right_color = None
    for i in range(rows):
        for j in range(stripe + 1, cols):
            if grid[i][j] != 0:
                right_color = grid[i][j]
                break
        if right_color is not None:
            break
    others = [j for j in range(cols) if j != stripe]
    bw = len(others) // 4
    res = []
    for i in range(rows):
        row = []
        for b in range(4):
            seg = others[b*bw:(b+1)*bw]
            c = left_color if seg[0] < stripe else right_color
            row.append(2 if any(grid[i][j] == c for j in seg) else 0)
        res.append(row)
    return res