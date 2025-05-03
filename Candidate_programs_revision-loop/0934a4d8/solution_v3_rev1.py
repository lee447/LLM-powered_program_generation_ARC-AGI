import math

def solve(grid):
    h, w = len(grid), len(grid[0])
    eights = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    rs = [r for r, c in eights]; cs = [c for r, c in eights]
    r0, c0 = min(rs), min(cs)
    shape = [(r - r0, c - c0) for r, c in eights]
    rc = (sum(r for r, c in shape) / len(shape),
          sum(c for r, c in shape) / len(shape))
    copies = []
    for r in range(h):
        for c in range(w):
            if all(0 <= r + dr < h and 0 <= c + dc < w for dr, dc in shape):
                val = grid[r + shape[0][0]][c + shape[0][1]]
                if val != 8 and all(grid[r + dr][c + dc] == val for dr, dc in shape):
                    copies.append(((r, c), val))
    def ang(p):
        r, c = p
        cr, cc = r + rc[0], c + rc[1]
        ar = cr - (r0 + rc[0]); ac = cc - (c0 + rc[1])
        return (-math.atan2(ar, ac)) % (2 * math.pi)
    copies.sort(key=lambda x: ang(x[0]))
    r_base, c_base = copies[0][0]
    max_r = max(r for r, c in shape)
    max_c = max(c for r, c in shape)
    out = [[0] * (max_c + 1) for _ in range(max_r + 1)]
    for dr, dc in shape:
        out[dr][dc] = grid[r_base + dr][c_base + dc]
    return out