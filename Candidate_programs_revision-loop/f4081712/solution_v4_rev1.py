from collections import defaultdict

def solve(grid):
    R, C = len(grid), len(grid[0])
    uniq = sorted({v for row in grid for v in row})
    candidates = []
    for color in uniq:
        coords = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == color]
        if len(coords) > 1:
            rs = [r for r, _ in coords]; cs = [c for _, c in coords]
            r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
            area = (r1 - r0 + 1) * (c1 - c0 + 1)
            if area == len(coords):
                candidates.append((area, color, r0, r1, c0, c1))
    area, mask_color, br0, br1, bc0, bc1 = min(candidates, key=lambda x: x[0])
    h, w = br1 - br0 + 1, bc1 - bc0 + 1
    counts = defaultdict(int)
    for r in range(R - h + 1):
        for c in range(C - w + 1):
            if r <= br1 and r + h - 1 >= br0 and c <= bc1 and c + w - 1 >= bc0:
                continue
            good = True
            for i in range(h):
                for j in range(w):
                    if grid[r + i][c + j] == mask_color:
                        good = False
                        break
                if not good:
                    break
            if not good:
                continue
            pat = tuple(tuple(grid[r + i][c + j] for j in range(w)) for i in range(h))
            counts[pat] += 1
    best = max(counts, key=counts.get)
    return [list(row) for row in best]