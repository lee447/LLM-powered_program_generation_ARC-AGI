def solve(grid):
    N = len({c for row in grid for c in row})
    new_rows = [row * N for row in grid]
    result = []
    for _ in range(N):
        for r in new_rows:
            result.append(r.copy())
    return result