def solve(grid):
    H = len(grid)
    W = len(grid[0]) if H else 0
    result = [[0]*W for _ in range(H)]
    for c in range(W):
        has_anchor = any(grid[r][c] == 5 for r in range(H))
        if not has_anchor:
            for r in range(H):
                v = grid[r][c]
                if v != 0:
                    result[r][c] = v
        else:
            last = {}
            for r in range(H):
                v = grid[r][c]
                if v != 0 and v != 5:
                    if v not in last or r > last[v]:
                        last[v] = r
            stripes = sorted(last.items(), key=lambda x: x[1])
            start = 0
            for v, end in stripes:
                for r in range(start, end+1):
                    result[r][c] = v
                start = end + 1
            for r in range(start, H):
                result[r][c] = 5
    return result