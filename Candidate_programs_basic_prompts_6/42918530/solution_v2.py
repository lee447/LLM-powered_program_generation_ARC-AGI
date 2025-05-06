from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    row_seps = [-1]
    for y in range(h):
        if all(grid[y][x] == 0 for x in range(w)):
            row_seps.append(y)
    row_seps.append(h)
    col_seps = [-1]
    for x in range(w):
        if all(grid[y][x] == 0 for y in range(h)):
            col_seps.append(x)
    col_seps.append(w)
    out = [row[:] for row in grid]
    for bi in range(len(row_seps)-1):
        y0 = row_seps[bi] + 1
        y1 = row_seps[bi+1] - 1
        if y0 > y1: continue
        for bj in range(len(col_seps)-1):
            x0 = col_seps[bj] + 1
            x1 = col_seps[bj+1] - 1
            if x0 > x1: continue
            c = grid[y0][x0]
            if c == 0: continue
            # detect broken border
            need_border = False
            for x in range(x0, x1+1):
                if grid[y0][x] == 0 or grid[y1][x] == 0:
                    need_border = True
            for y in range(y0, y1+1):
                if grid[y][x0] == 0 or grid[y][x1] == 0:
                    need_border = True
            if need_border:
                for x in range(x0, x1+1):
                    out[y0][x] = c
                    out[y1][x] = c
                for y in range(y0, y1+1):
                    out[y][x0] = c
                    out[y][x1] = c
                continue
            # detect blank interior
            blank_int = True
            for y in range(y0+1, y1):
                for x in range(x0+1, x1):
                    if grid[y][x] != 0:
                        blank_int = False
                        break
                if not blank_int:
                    break
            if blank_int:
                cy = (y0 + y1) // 2
                cx = (x0 + x1) // 2
                for y in range(y0+1, y1):
                    for x in range(x0+1, x1):
                        if y == cy or x == cx:
                            out[y][x] = c
                continue
    return out