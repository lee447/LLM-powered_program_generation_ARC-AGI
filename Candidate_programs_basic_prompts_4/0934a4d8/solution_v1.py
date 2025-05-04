def solve(grid):
    R, C = len(grid), len(grid[0])
    ones = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 8]
    r0 = min(r for r, _ in ones)
    r1 = max(r for r, _ in ones)
    c0 = min(c for _, c in ones)
    c1 = max(c for _, c in ones)
    h, w = r1 - r0 + 1, c1 - c0 + 1
    freq = {}
    order = []
    for i in range(R - h + 1):
        for j in range(C - w + 1):
            block = tuple(tuple(grid[i + di][j + dj] for dj in range(w)) for di in range(h))
            if any(val == 8 for row in block for val in row):
                continue
            if block not in freq:
                freq[block] = 0
                order.append(block)
            freq[block] += 1
    best = max(order, key=lambda b: freq[b])
    return [list(row) for row in best]