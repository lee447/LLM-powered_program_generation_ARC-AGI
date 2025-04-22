def solve(grid):
    h, w = len(grid), len(grid[0])
    row_seps = [i for i in range(h) if all(grid[i][j] == 0 for j in range(w))]
    col_seps = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    row_seps.sort()
    col_seps.sort()
    row_int = [(row_seps[i]+1, row_seps[i+1]-1) for i in range(len(row_seps)-1) if row_seps[i+1] - row_seps[i] > 1]
    col_int = [(col_seps[i]+1, col_seps[i+1]-1) for i in range(len(col_seps)-1) if col_seps[i+1] - col_seps[i] > 1]
    new = [list(r) for r in grid]
    for bi, (r0, r1) in enumerate(row_int):
        for bj, (c0, c1) in enumerate(col_int):
            cs = {(r0, c0), (r0, c0+1), (r0+1, c0),
                  (r0, c1), (r0, c1-1), (r0+1, c1),
                  (r1, c0), (r1, c0+1), (r1-1, c0),
                  (r1, c1), (r1, c1-1), (r1-1, c1)}
            cluster_color = grid[next(iter(cs))[0]][next(iter(cs))[1]]
            fill_color = None
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    if grid[r][c] != 0 and (r, c) not in cs:
                        fill_color = grid[r][c]
                        break
                if fill_color is not None:
                    break
            if (bi + bj) % 2 == 0:
                cluster_color, fill_color = fill_color, cluster_color
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    if grid[r][c] == 0:
                        continue
                    new[r][c] = cluster_color if (r, c) in cs else fill_color
    return new