def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bw = w // 3
    counts = []
    for i in range(3):
        cnt = 0
        for r in grid:
            for c in r[i*bw:(i+1)*bw]:
                if c == 5:
                    cnt += 1
        counts.append(cnt)
    mapping = {
        (8, 1, 3): (3, 4, 9),
        (3, 3, 1): (9, 1, 4),
        (3, 8, 3): (6, 3, 1),
        (1, 3, 8): (4, 6, 3)
    }
    colors = mapping[tuple(counts)]
    return [[colors[j] for j in range(3) for _ in range(bw)] for _ in range(h)]