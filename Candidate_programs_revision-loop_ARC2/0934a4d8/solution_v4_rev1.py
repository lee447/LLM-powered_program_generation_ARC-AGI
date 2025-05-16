def solve(grid):
    from collections import Counter
    n, m = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    marker = 8
    r0, c0 = n, m
    r1 = c1 = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == marker:
                r0 = min(r0, i); c0 = min(c0, j)
                r1 = max(r1, i); c1 = max(c1, j)
    w = c1 - c0 + 1
    h = r1 - r0 + 1
    above = [row[c0:c1+1] for row in grid[:r0]]
    below = [row[c0:c1+1] for row in grid[r1+1:]]
    left = [row[:c0] for row in grid[r0:r1+1]]
    right = [row[c1+1:] for row in grid[r0:r1+1]]
    def choose(cand):
        if not cand: return False
        dims = (len(cand), len(cand[0]))
        return dims != (h, w)
    for cand in (above, below, left, right):
        if choose(cand):
            return cand
    return []