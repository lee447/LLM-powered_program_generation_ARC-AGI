def solve(grid):
    h, w = len(grid), len(grid[0])
    patterns = []
    for row in grid:
        if any(c > 1 for c in row) and all(c != 0 for c in row):
            arr = row[1:-1]
            for L in range(1, len(arr) + 1):
                if all(arr[i] == arr[i % L] for i in range(len(arr))):
                    p = tuple(arr[:L])
                    if p not in patterns:
                        patterns.append(p)
                    break
    out = [row[:] for row in grid]
    for i, row in enumerate(grid):
        if any(c > 1 for c in row):
            p = None
            for cand in patterns:
                if all(row[j] == 0 or row[j] == cand[(j - 1) % len(cand)] for j in range(1, w - 1)):
                    p = cand
                    break
            for j in range(1, w - 1):
                if row[j] == 0:
                    out[i][j] = p[(j - 1) % len(p)]
        else:
            for j in range(1, w - 1):
                if row[j] == 0:
                    out[i][j] = 1
    return out