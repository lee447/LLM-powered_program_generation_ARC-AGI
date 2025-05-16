from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    regions = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 1:
                if v not in regions:
                    regions[v] = [r, r, c, c]
                else:
                    regions[v][0] = min(regions[v][0], r)
                    regions[v][1] = max(regions[v][1], r)
                    regions[v][2] = min(regions[v][2], c)
                    regions[v][3] = max(regions[v][3], c)
    def extract(r0, r1, c0, c1):
        return [row[c0:c1+1] for row in grid[r0:r1+1]]
    def rot90(pat):
        h, w = len(pat), len(pat[0])
        return [[pat[h-1-j][i] for j in range(h)] for i in range(w)]
    patterns = {}
    heights = {}
    bots = {}
    for v, (r0, r1, c0, c1) in regions.items():
        p = extract(r0, r1, c0, c1)
        h, w = len(p), len(p[0])
        if h > w:
            p = rot90(p)
            h, w = len(p), len(p[0])
        patterns[v] = p
        heights[v] = h
        bots[v] = regions[v][1]
    base = max(heights.values())
    max_bot = max(bots.values())
    top = max_bot - base + 1
    out = [[1]*W for _ in range(H)]
    xpos = 0
    for v in sorted(patterns, key=lambda v: -regions[v][0]):
        pat = patterns[v]
        h, w = len(pat), len(pat[0])
        y0 = base - h
        for i in range(h):
            for j in range(w):
                if pat[i][j] != 1:
                    r = top + y0 + i
                    c = xpos + j
                    if 0 <= r < H and 0 <= c < W:
                        out[r][c] = pat[i][j]
        xpos += w
    return out