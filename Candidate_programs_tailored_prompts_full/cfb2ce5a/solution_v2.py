def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    # find main 4x4 block
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
    # find anchor: nonzero not in block, adjacent (manh=1) to any block cell
    anchor = None
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v not in main_colors:
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    rr, cc = r+dr, c+dc
                    if 0 <= rr < h and 0 <= cc < w and (rr in range(r0, r0+4) and cc in range(c0, c0+4)):
                        anchor = v
                        break
                if anchor is not None:
                    break
        if anchor is not None:
            break
    # find mini-shape colors: nonzero not in block or anchor, in inner 8x8
    mini = []
    for r in range(r0, r0+8):
        for c in range(c0, c0+8):
            v = grid[r][c]
            if v != 0 and v != anchor and v not in main_colors:
                if v not in mini:
                    mini.append(v)
    # extend top band
    A, B = main_colors
    for dr in range(4):
        for dc in range(4):
            orig = grid[r0+dr][c0+dc]
            if orig == A:
                out[r0+dr][c0+dc+4] = anchor
            else:
                out[r0+dr][c0+dc+4] = mini[0] if mini else 0
    # fill bottom-left block stripes by rows
    if mini:
        col = mini[0]
        col2 = mini[1] if len(mini) > 1 else mini[0]
        for dr in range(4):
            color = col if dr % 2 == 0 else col2
            for dc in range(4):
                out[r0+4+dr][c0+dc] = color
    # fill bottom-right block stripes by columns
    if len(mini) > 1:
        for dr in range(4):
            for dc in range(4):
                color = mini[1] if dc % 2 == 0 else mini[0]
                out[r0+4+dr][c0+4+dc] = color
    return out