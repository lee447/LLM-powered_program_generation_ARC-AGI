from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sep_rows = [r for r in range(h) if all(c == 0 for c in grid[r])]
    bands = []
    for i in range(len(sep_rows) - 1):
        a, b = sep_rows[i], sep_rows[i+1]
        if b > a + 1:
            bands.append((a + 1, b - 1))
    sep_cols = [c for c in range(w) if all(grid[r][c] == 0 for r in range(h))]
    cols = []
    for i in range(len(sep_cols) - 1):
        a, b = sep_cols[i], sep_cols[i+1]
        if b > a + 1:
            cols.append((a + 1, b - 1))
    blocks = []
    for bi, (r0, r1) in enumerate(bands):
        for ci, (c0, c1) in enumerate(cols):
            # find block color
            found = None
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    if grid[r][c] != 0:
                        found = grid[r][c]
                        break
                if found is not None:
                    break
            if found is None:
                continue
            color = found
            # interior coords
            ir0, ir1 = r0 + 1, r1 - 1
            ic0, ic1 = c0 + 1, c1 - 1
            # detect orientation
            hor = any(all(grid[r][c] == color for c in range(ic0, ic1+1)) for r in range(ir0, ir1+1))
            ver = any(all(grid[r][c] == color for r in range(ir0, ir1+1)) for c in range(ic0, ic1+1))
            blocks.append({
                'color': color,
                'band': bi,
                'r0': r0, 'r1': r1,
                'c0': c0, 'c1': c1,
                'hor': hor, 'ver': ver
            })
    by_color = {}
    for b in blocks:
        by_color.setdefault(b['color'], []).append(b)
    out = [row[:] for row in grid]
    for color, blist in by_color.items():
        if len(blist) < 2:
            continue
        blist.sort(key=lambda x: x['band'])
        init = blist[0]
        for b in blist[1:]:
            ir0, ir1 = b['r0']+1, b['r1']-1
            ic0, ic1 = b['c0']+1, b['c1']-1
            mid_r = ir0 + (ir1 - ir0) // 2
            mid_c = ic0 + (ic1 - ic0) // 2
            if init['hor'] and not b['hor']:
                for c in range(ic0, ic1+1):
                    out[mid_r][c] = color
            if init['ver'] and not b['ver']:
                for r in range(ir0, ir1+1):
                    out[r][mid_c] = color
    return out