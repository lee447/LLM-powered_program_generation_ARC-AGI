from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    min_r, max_r, min_c, max_c = h, -1, w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 8:
                min_r = min(min_r, r); max_r = max(max_r, r)
                min_c = min(min_c, c); max_c = max(max_c, c)
    H, W = max_r - min_r + 1, max_c - min_c + 1
    counts = {}
    for r in range(h - H + 1):
        for c in range(w - W + 1):
            block = []
            ok = True
            for i in range(H):
                row = grid[r + i][c:c + W]
                if 8 in row:
                    ok = False
                    break
                block.append(tuple(row))
            if not ok:
                continue
            key = tuple(block)
            counts[key] = counts.get(key, 0) + 1
    best = max(counts.items(), key=lambda x: x[1])[0]
    return [list(row) for row in best]