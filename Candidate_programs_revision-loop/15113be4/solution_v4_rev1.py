from typing import List, Tuple
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def find_comps(value_test):
        seen = [[False]*W for _ in range(H)]
        comps = []
        for i in range(H):
            for j in range(W):
                if not seen[i][j] and value_test(grid[i][j]):
                    color = grid[i][j]
                    q = deque([(i,j)])
                    seen[i][j] = True
                    cells = []
                    while q:
                        y,x = q.popleft()
                        cells.append((y,x))
                        for dy,dx in dirs:
                            ny, nx = y+dy, x+dx
                            if 0<=ny<H and 0<=nx<W and not seen[ny][nx] and value_test(grid[ny][nx]):
                                seen[ny][nx] = True
                                q.append((ny,nx))
                    comps.append((cells, color))
        return comps

    def signature(cells: List[Tuple[int,int]]):
        ys = [y for y,_ in cells]
        xs = [x for _,x in cells]
        miny, minx = min(ys), min(xs)
        rel = sorted(((y-miny, x-minx) for y,x in cells))
        return tuple(rel)

    seed_comps = []
    for cells, color in find_comps(lambda v: v not in (0,1,4)):
        seed_comps.append((signature(cells), cells, color))
    mask_comps = []
    for cells, _ in find_comps(lambda v: v == 1):
        mask_comps.append((signature(cells), cells))

    seeds_by_sig = {}
    for sig, cells, color in seed_comps:
        seeds_by_sig.setdefault(sig, []).append((cells, color))
    masks_by_sig = {}
    for sig, cells in mask_comps:
        masks_by_sig.setdefault(sig, []).append(cells)

    for sig in seeds_by_sig:
        if sig in masks_by_sig:
            scs = seeds_by_sig[sig]
            mcs = masks_by_sig[sig]
            n = min(len(scs), len(mcs))
            for k in range(n):
                seed_cells, seed_color = scs[k]
                mask_cells = mcs[k]
                for y,x in seed_cells:
                    grid[y][x] = 1
                for y,x in mask_cells:
                    grid[y][x] = seed_color
    return grid