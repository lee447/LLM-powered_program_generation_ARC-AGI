def solve(grid):
    R, C = len(grid), len(grid[0])
    fives = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 5]
    def has_neighbor(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if (dr or dc) and 0 <= r+dr < R and 0 <= c+dc < C:
                    v = grid[r+dr][c+dc]
                    if v != 0 and v != 5:
                        return True
        return False
    if has_neighbor(*fives[0]):
        src_r, src_c = fives[0]
        tgt_r, tgt_c = fives[1]
    else:
        src_r, src_c = fives[1]
        tgt_r, tgt_c = fives[0]
    result = [row[:] for row in grid]
    for r in range(R):
        for c in range(C):
            v = grid[r][c]
            if v != 0 and v != 5:
                dr, dc = r - src_r, c - src_c
                tr, tc = tgt_r + dr, tgt_c + dc
                if 0 <= tr < R and 0 <= tc < C:
                    result[tr][tc] = v
    return result