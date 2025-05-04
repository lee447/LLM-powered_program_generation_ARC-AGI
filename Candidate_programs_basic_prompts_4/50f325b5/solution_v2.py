def solve(grid):
    N, M = len(grid), len(grid[0])
    orig = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == 8]
    if not orig:
        return grid
    minr = min(r for r, c in orig)
    maxr = max(r for r, c in orig)
    minc = min(c for r, c in orig)
    maxc = max(c for r, c in orig)
    r0 = (minr + maxr) // 2
    c0 = (minc + maxc) // 2
    rel0 = [(r - r0, c - c0) for r, c in orig]
    def rot_ccw(shape):
        return [(-c, r) for r, c in shape]
    variants = [rel0]
    for _ in range(3):
        variants.append(rot_ccw(variants[-1]))
    out = [row[:] for row in grid]
    for shape in variants[1:]:
        placed = False
        for i in range(N):
            if placed:
                break
            for j in range(M):
                ok = True
                for dr, dc in shape:
                    r, c = i + dr, j + dc
                    if r < 0 or r >= N or c < 0 or c >= M or out[r][c] == 8:
                        ok = False
                        break
                if not ok:
                    continue
                for dr, dc in shape:
                    out[i + dr][j + dc] = 8
                placed = True
                break
    return out