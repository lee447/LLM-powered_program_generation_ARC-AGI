from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    nrows = len(grid)
    ncols = len(grid[0])
    width = 3
    zones = ncols // width
    perim = 2*(width + nrows) - 4
    color_map = {"single":4, "diag":9, "ring":3, "top_bar":6, "bot_bar":1}
    out = [[0]*ncols for _ in range(nrows)]
    for z in range(zones):
        coords = []
        for r in range(nrows):
            for c in range(z*width, z*width+width):
                if grid[r][c] == 5:
                    coords.append((r, c - z*width))
        lc = len(coords)
        if lc == 1:
            shape = "single"
        elif lc == perim and all(r in (0, nrows-1) or c in (0, width-1) for r, c in coords):
            shape = "ring"
        elif lc == nrows and len({r for r, _ in coords}) == 1:
            r0 = coords[0][0]
            shape = "top_bar" if r0 == 0 else "bot_bar"
        else:
            shape = "diag"
        fill = color_map[shape]
        for r in range(nrows):
            for c in range(z*width, z*width+width):
                out[r][c] = fill
    return out