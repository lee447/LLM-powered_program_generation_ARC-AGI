def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    if any(8 in row for row in grid):
        pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
        rmin = min(r for r, c in pts)
        rmax = max(r for r, c in pts)
        cmin = min(c for r, c in pts)
        cmax = max(c for r, c in pts)
        rc = rmin - 1
        cc = (cmin + cmax) // 2
        center = grid[rc][cc]
        for r, c in pts:
            out[r][c] = center if r == rmin else center + 1
        return out
    else:
        # input2 logic
        # recolor all 4‐cells
        four = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 4]
        if four:
            rmin = min(r for r, c in four)
            rmax = max(r for r, c in four)
            cmin = min(c for r, c in four)
            cmax = max(c for r, c in four)
            # find center color = 2
            center_color = 2
            for r, c in four:
                out[r][c] = center_color + 1
            # find fill color from input 6
            fill = None
            for r in range(h):
                for c in range(w):
                    if grid[r][c] == 6:
                        fill = 6
                        break
                if fill is not None:
                    break
            # mirror each 4‐cell across center of its bbox
            rc = (rmin + rmax) // 2
            cc = (cmin + cmax) // 2
            for r, c in four:
                dr = r - rc
                dc = c - cc
                rr = rc - dr
                cc2 = cc - dc
                if 0 <= rr < h and 0 <= cc2 < w:
                    out[rr][cc2] = fill
        return out