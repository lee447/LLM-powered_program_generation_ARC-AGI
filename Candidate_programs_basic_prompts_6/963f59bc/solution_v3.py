from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    cnt = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0:
                cnt[v] = cnt.get(v, 0) + 1
    pattern_color = max((col for col in cnt if col != 0), key=lambda x: cnt[x])
    markers = [(r, c, grid[r][c]) for r in range(H) for c in range(W)
               if grid[r][c] != 0 and grid[r][c] != pattern_color]
    # bounding box of pattern
    rows = [r for r in range(H) for c in range(W) if grid[r][c] == pattern_color]
    cols = [c for r in range(H) for c in range(W) if grid[r][c] == pattern_color]
    top, bottom = min(rows), max(rows)
    left, right = min(cols), max(cols)
    h = bottom - top + 1
    w = right - left + 1
    # extract pattern
    pattern = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[top+i][left+j] == pattern_color:
                pattern[i][j] = 1
    # precompute transforms
    rev_h = [[pattern[i][w-1-j] for j in range(w)] for i in range(h)]
    rev_v = [[pattern[h-1-i][j] for j in range(w)] for i in range(h)]
    out = [row[:] for row in grid]
    for r, c, col in markers:
        if top <= r <= bottom and c > right:
            # side right
            ai = r - top
            # find anchor_j in pattern row ai
            for aj in range(w):
                if pattern[ai][aj]:
                    anchor_j = aj
                    break
            new_anchor_j = w - 1 - anchor_j
            bt, bl = top, c - new_anchor_j
            for i in range(h):
                for j in range(w):
                    if rev_h[i][j]:
                        out[bt+i][bl+j] = col
        elif left <= c <= right and r > bottom:
            # side down
            bt = bottom + 3
            bl = left
            for i in range(h):
                for j in range(w):
                    if rev_v[i][j]:
                        out[bt+i][bl+j] = col
    return out