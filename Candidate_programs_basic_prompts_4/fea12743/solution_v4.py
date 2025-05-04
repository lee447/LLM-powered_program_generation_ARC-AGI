def solve(grid):
    R, C = len(grid), len(grid[0])
    rows = [i for i in range(R) if all(grid[i][j] == 0 for j in range(C))]
    cols = [j for j in range(C) if all(grid[i][j] == 0 for i in range(R))]
    stripes = []
    for a, b in zip(rows, rows[1:]):
        if b - a > 1:
            stripes.append((a + 1, b))
    blocks = []
    for a, b in zip(cols, cols[1:]):
        if b - a > 1:
            blocks.append((a + 1, b))
    positions = []
    for si, (r0, r1) in enumerate(stripes):
        for bj, (c0, c1) in enumerate(blocks):
            pts = [(i, j) for i in range(r0, r1) for j in range(c0, c1) if grid[i][j] == 2]
            if pts:
                positions.append((si, bj, pts))
    adj = {idx: set() for idx in range(len(positions))}
    for i, (si, bj, _) in enumerate(positions):
        for j, (sj, bk, _) in enumerate(positions):
            if i < j:
                if si == sj and abs(bj - bk) == 1: adj[i].add(j); adj[j].add(i)
                if bj == bk and abs(si - sj) == 1: adj[i].add(j); adj[j].add(i)
    used = {grid[i][j] for i in range(R) for j in range(C)}
    palette = [2] + [c for c in range(1,10) if c != 2 and c not in used] + [c for c in range(1,10) if c not in (2,)]
    color = {}
    for idx in sorted(adj, key=lambda x:(positions[x][0],positions[x][1])):
        banned = {color[nbr] for nbr in adj[idx] if nbr in color}
        for c in palette:
            if c not in banned:
                color[idx] = c
                break
    out = [row[:] for row in grid]
    for idx, (_, _, pts) in enumerate(positions):
        c = color[idx]
        for i, j in pts:
            out[i][j] = c
    return out