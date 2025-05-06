def solve(grid):
    from collections import defaultdict, Counter
    R, C = len(grid), len(grid[0])
    positions = {}
    for i in range(R):
        for j in range(C):
            v = grid[i][j]
            if v not in positions: positions[v] = [i, i, j, j, 0]
            p = positions[v]
            p[0] = min(p[0], i); p[1] = max(p[1], i)
            p[2] = min(p[2], j); p[3] = max(p[3], j)
            p[4] += 1
    marker = None
    max_area = -1
    for v, (r0, r1, c0, c1, cnt) in positions.items():
        h = r1 - r0 + 1; w = c1 - c0 + 1
        if h * w == cnt and h > 1 and w > 1 and h * w > max_area:
            max_area = h * w
            marker = (v, r0, r1, c0, c1)
    v, r0, r1, c0, c1 = marker
    h, w = r1 - r0 + 1, c1 - c0 + 1
    counts = Counter()
    blocks = {}
    for i in range(R - h + 1):
        for j in range(C - w + 1):
            bad = False
            key = []
            for di in range(h):
                row = grid[i+di][j:j+w]
                if v in row:
                    bad = True
                    break
                key.append(tuple(row))
            if bad: continue
            key = tuple(key)
            counts[key] += 1
            blocks[key] = key
    pattern = counts.most_common(1)[0][0]
    return [list(row) for row in pattern]