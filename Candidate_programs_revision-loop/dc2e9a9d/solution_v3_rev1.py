from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 3 and not visited[i][j]:
                stack = [(i,j)]
                coords = []
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    coords.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 3 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,c in coords]
                cs = [c for r,c in coords]
                shapes.append((min(rs), max(rs), min(cs), max(cs), coords))
    res = [row[:] for row in grid]
    def can_place_h(shape):
        minr,maxr,minc,maxc,coords = shape
        sw = maxc-minc+1
        cc0 = maxc+2
        if cc0+sw-1 >= w: return False
        for r,c in coords:
            if grid[r][cc0+(c-minc)] != 0: return False
        return True
    def can_place_v(shape):
        minr,maxr,minc,maxc,coords = shape
        sh = maxr-minr+1
        # down
        rr0 = maxr+2
        if rr0+sh-1 < h:
            ok = True
            for r,c in coords:
                if grid[rr0+(r-minr)][c] != 0: ok = False; break
            if ok: return ("down", rr0)
        # up
        rr1 = minr-2
        rs0 = rr1-(sh-1)
        if rs0 >= 0:
            ok = True
            for r,c in coords:
                if grid[rs0+(r-minr)][c] != 0: ok = False; break
            if ok: return ("up", rs0)
        return (None, None)
    chosen_h = None
    chosen_v = None
    dir_v = None
    off_v = None
    for sh in shapes:
        if not can_place_h(sh): continue
        for sv in shapes:
            if sv is sh: continue
            d, off = can_place_v(sv)
            if d:
                chosen_h = sh
                chosen_v = sv
                dir_v = d
                off_v = off
                break
        if chosen_h: break
    if chosen_h:
        minr,maxr,minc,maxc,coords = chosen_h
        sw = maxc-minc+1
        cc0 = maxc+2
        for r,c in coords:
            res[r][cc0+(c-minc)] = 1
    if chosen_v:
        minr,maxr,minc,maxc,coords = chosen_v
        sh = maxr-minr+1
        if dir_v == "down":
            rr0 = maxr+2
        else:
            rr0 = off_v
        for r,c in coords:
            res[(rr0+(r-minr))][c] = 8
    return res