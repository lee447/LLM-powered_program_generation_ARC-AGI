import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    # locate the 4×4 main block
    for br in range(h - 3):
        for bc in range(w - 3):
            block = {grid[r][c] for r in range(br, br+4) for c in range(bc, bc+4)}
            if 0 not in block and len(block) == 2:
                r0, c0 = br, bc
                main_colors = list(block)
                break
        else:
            continue
        break
    A, B = main_colors
    # find the "anchor" color adjacent to that block
    anchor = None
    for r in range(r0, r0+4):
        for c in range(c0, c0+4):
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                rr, cc = r+dr, c+dc
                if 0 <= rr < h and 0 <= cc < w:
                    v = grid[rr][cc]
                    if v != 0 and v not in main_colors:
                        anchor = v
                        break
            if anchor is not None:
                break
        if anchor is not None:
            break
    # collect the other colors in the 8×8 region
    mini = []
    for r in range(r0, r0+8):
        for c in range(c0, c0+8):
            v = grid[r][c]
            if v != 0 and v not in main_colors and v != anchor and v not in mini:
                mini.append(v)
    # top‐right: replicate main block with A→anchor, B→mini[0]
    for dr in range(4):
        for dc in range(4):
            v = grid[r0+dr][c0+dc]
            out[r0+dr][c0+4+dc] = anchor if v == A else (mini[0] if mini else 0)
    # bottom‐left: stripes by rows using mini[1],mini[2]
    if len(mini) > 2:
        c1, c2 = mini[1], mini[2]
        for dr in range(4):
            color = c1 if dr % 2 == 0 else c2
            for dc in range(4):
                out[r0+4+dr][c0+dc] = color
    # bottom‐right: stripes by columns using mini[-1],mini[-2]
    if len(mini) > 3:
        c1, c2 = mini[-1], mini[-2]
        for dr in range(4):
            for dc in range(4):
                out[r0+4+dr][c0+4+dc] = c1 if dc % 2 == 0 else c2
    return out