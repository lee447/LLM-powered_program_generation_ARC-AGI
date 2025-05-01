def solve(grid):
    h, w = len(grid), len(grid[0])
    block_w = w // 3
    counts = [0, 0, 0]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5:
                counts[j // block_w] += 1
    idx = sorted(range(3), key=lambda x: counts[x])
    cols = [0] * 3
    cols[idx[0]] = 1
    cols[idx[1]] = 4
    cols[idx[2]] = 9
    return [[cols[j // block_w] for j in range(w)] for _ in range(h)]