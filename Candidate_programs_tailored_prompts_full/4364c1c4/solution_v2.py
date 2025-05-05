from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    background = grid[0][0]
    orig = [row[:] for row in grid]
    res = [row[:] for row in grid]
    r = 0
    while r < H:
        if grid[r][0] == background:
            r += 1
            continue
        color = grid[r][0]
        start = r
        while r < H and grid[r][0] == color:
            r += 1
        end = r - 1
        # bottom row defines full width
        cols_full = [c for c in range(W) if grid[end][c] == color]
        left = min(cols_full)
        width = max(cols_full) - left + 1
        indent = end - 1 if end - 1 >= start else None
        if indent is not None:
            gaps = [c for c in range(left, left + width) if grid[indent][c] == background]
            if len(gaps) == 2:
                g0, g1 = gaps
                gap_w = g1 - g0 + 1
                off = g0 - left
                new_off = width - gap_w - off
                ng0 = left + new_off
                ng1 = ng0 + gap_w - 1
                for c in gaps:
                    orig[indent][c] = color
                for c in range(ng0, ng1 + 1):
                    orig[indent][c] = background
        # clear in res and write shifted pattern
        pattern = {}
        for rr in range(start, end + 1):
            pattern[rr] = orig[rr][left:left+width]
            for c in range(left, left + width):
                res[rr][c] = background
        for rr in range(start, end + 1):
            for i, v in enumerate(pattern[rr]):
                res[rr][i] = v
    return res