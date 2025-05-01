from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    min_r, max_r = h, -1
    min_c, max_c = w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 8:
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)
    H = max_r - min_r + 1
    W = max_c - min_c + 1
    for dr in (-1, 1):
        for dc in (-1, 1):
            sr = min_r + dr * H
            sc = min_c + dc * W
            if 0 <= sr <= h - H and 0 <= sc <= w - W:
                block = [row[sc:sc+W] for row in grid[sr:sr+H]]
                if all(val != 8 for row in block for val in row):
                    return block
    return []