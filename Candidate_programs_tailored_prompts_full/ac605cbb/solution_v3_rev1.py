from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    anchors = [(r, c, grid[r][c]) for r in range(H) for c in range(W) if grid[r][c] != 0]
    out = [[0]*W for _ in range(H)]
    occupied = [[False]*W for _ in range(H)]
    for r, c, v in anchors:
        out[r][c] = v
        occupied[r][c] = True
    center_r, center_c = H/2, W/2
    for r, c, v in anchors:
        placed = False
        hd_list = [1, -1] if c < center_c else [-1, 1]
        vd_list = [-1, 1] if r < center_r else [1, -1]
        orders = [(0,1), (1,0)] if r < center_r else [(1,0), (0,1)]
        for hor_first, ver_first in orders:
            if placed:
                break
            for hd in hd_list:
                if placed:
                    break
                for vd in vd_list:
                    if placed:
                        break
                    maxh = (W-1-c) if hd>0 else c
                    maxv = (H-1-r) if vd>0 else r
                    if maxh <= 0 or maxv <= 0:
                        continue
                    for hlen in range(1, maxh+1):
                        if placed:
                            break
                        for vlen in range(1, maxv+1):
                            if placed:
                                break
                            if hor_first == 0:
                                path1 = [(r, c+hd*i) for i in range(1, hlen+1)]
                                corner = (r, c+hd*hlen)
                                path2 = [(corner[0]+vd*i, corner[1]) for i in range(1, vlen+1)]
                            else:
                                path1 = [(r+vd*i, c) for i in range(1, vlen+1)]
                                corner = (r+vd*vlen, c)
                                path2 = [(corner[0], corner[1]+hd*i) for i in range(1, hlen+1)]
                            end = path2[-1]
                            if any(not(0<=x<H and 0<=y<W) or occupied[x][y] for x,y in path1+path2):
                                continue
                            for x,y in path1+path2:
                                out[x][y] = 5
                                occupied[x][y] = True
                            out[end[0]][end[1]] = v
                            occupied[end[0]][end[1]] = True
                            placed = True
        if not placed:
            # try straight horizontal first if horizontal space >= vertical, else vertical first
            dist_h = min(c, W-1-c)
            dist_v = min(r, H-1-r)
            if dist_h >= dist_v:
                # horizontal
                for hd in hd_list:
                    maxh = (W-1-c) if hd>0 else c
                    for hlen in range(1, maxh+1):
                        cells = [(r, c+hd*i) for i in range(1, hlen+1)]
                        if any(occupied[x][y] for x,y in cells):
                            break
                        end = (r, c+hd*hlen)
                        for x,y in cells:
                            out[x][y] = 5
                            occupied[x][y] = True
                        out[end[0]][end[1]] = v
                        occupied[end[0]][end[1]] = True
                        placed = True
                        break
                if placed:
                    continue
                # vertical
                for vd in vd_list:
                    maxv = (H-1-r) if vd>0 else r
                    for vlen in range(1, maxv+1):
                        cells = [(r+vd*i, c) for i in range(1, vlen+1)]
                        if any(occupied[x][y] for x,y in cells):
                            break
                        end = (r+vd*vlen, c)
                        for x,y in cells:
                            out[x][y] = 5
                            occupied[x][y] = True
                        out[end[0]][end[1]] = v
                        occupied[end[0]][end[1]] = True
                        placed = True
                        break
            else:
                # vertical first
                for vd in vd_list:
                    maxv = (H-1-r) if vd>0 else r
                    for vlen in range(1, maxv+1):
                        cells = [(r+vd*i, c) for i in range(1, vlen+1)]
                        if any(occupied[x][y] for x,y in cells):
                            break
                        end = (r+vd*vlen, c)
                        for x,y in cells:
                            out[x][y] = 5
                            occupied[x][y] = True
                        out[end[0]][end[1]] = v
                        occupied[end[0]][end[1]] = True
                        placed = True
                        break
                    if placed:
                        break
                if placed:
                    continue
                # horizontal
                for hd in hd_list:
                    maxh = (W-1-c) if hd>0 else c
                    for hlen in range(1, maxh+1):
                        cells = [(r, c+hd*i) for i in range(1, hlen+1)]
                        if any(occupied[x][y] for x,y in cells):
                            break
                        end = (r, c+hd*hlen)
                        for x,y in cells:
                            out[x][y] = 5
                            occupied[x][y] = True
                        out[end[0]][end[1]] = v
                        occupied[end[0]][end[1]] = True
                        placed = True
                        break
    return out