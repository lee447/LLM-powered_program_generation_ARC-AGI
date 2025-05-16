from collections import Counter

def solve(grid):
    R, C = len(grid), len(grid[0])
    r0, r1, c0, c1 = R, -1, C, -1
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 8:
                r0 = min(r0, i)
                r1 = max(r1, i)
                c0 = min(c0, j)
                c1 = max(c1, j)
    hmask = r1 - r0 + 1
    wmask = c1 - c0 + 1
    heights = {hmask}
    widths = {wmask}
    if r0 > 0 and all(grid[r0-1][j] != 8 for j in range(c0, c1+1)):
        heights.add(hmask + 1)
    if r1 + 1 < R and all(grid[r1+1][j] != 8 for j in range(c0, c1+1)):
        heights.add(hmask + 1)
    if c0 > 0 and all(grid[i][c0-1] != 8 for i in range(r0, r1+1)):
        widths.add(wmask + 1)
    if c1 + 1 < C and all(grid[i][c1+1] != 8 for i in range(r0, r1+1)):
        widths.add(wmask + 1)
    counter = Counter()
    for h in heights:
        for w in widths:
            for i in range(R - h + 1):
                for j in range(C - w + 1):
                    ok = True
                    for di in range(h):
                        for dj in range(w):
                            if grid[i+di][j+dj] == 8:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        blk = tuple(tuple(grid[i+di][j+dj] for dj in range(w)) for di in range(h))
                        counter[blk] += 1
    pattern = max(counter.items(), key=lambda x: x[1])[0]
    return [list(row) for row in pattern]