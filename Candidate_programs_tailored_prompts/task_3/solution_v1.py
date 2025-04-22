from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    nzr = [r for r in range(H) if any(grid[r][c] != 0 for c in range(W))]
    def segments(idx):
        segs = []
        start = prev = None
        for i in idx:
            if start is None:
                start = prev = i
            elif i == prev + 1:
                prev = i
            else:
                segs.append(list(range(start, prev + 1)))
                start = prev = i
        if start is not None:
            segs.append(list(range(start, prev + 1)))
        return segs
    row_segs = segments(nzr)
    nzc = [c for c in range(W) if any(grid[r][c] != 0 for r in range(H))]
    col_segs = segments(nzc)
    def sign(x):
        return 0 if x == 0 else (1 if x > 0 else -1)
    for rs in row_segs:
        for cs in col_segs:
            # identify border color
            color = 0
            for c in cs:
                if grid[rs[0]][c] != 0:
                    color = grid[rs[0]][c]
                    break
                if grid[rs[-1]][c] != 0:
                    color = grid[rs[-1]][c]
                    break
            if color == 0:
                for r in rs:
                    if grid[r][cs[0]] != 0:
                        color = grid[r][cs[0]]
                        break
                    if grid[r][cs[-1]] != 0:
                        color = grid[r][cs[-1]]
                        break
            if color == 0:
                continue
            r0, r1 = rs[0], rs[-1]
            c0, c1 = cs[0], cs[-1]
            rc = (r0 + r1) // 2
            cc = (c0 + c1) // 2
            # map border segments inward
            for c in cs:
                for r in (r0, r1):
                    if grid[r][c] == color:
                        dr = sign(rc - r)
                        dc = 0
                        rr, cc2 = r + dr, c + dc
                        if out[rr][cc2] == 0:
                            out[rr][cc2] = color
            for r in rs:
                for c in (c0, c1):
                    if grid[r][c] == color:
                        dr = 0
                        dc = sign(cc - c)
                        rr, cc2 = r + dr, c + dc
                        if out[rr][cc2] == 0:
                            out[rr][cc2] = color
    return out