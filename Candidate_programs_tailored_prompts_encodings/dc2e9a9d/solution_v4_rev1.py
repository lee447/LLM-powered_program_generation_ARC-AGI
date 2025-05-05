from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    frames = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 3 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and grid[nr][nc] == 3:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                frames.append((r0,r1,c0,c1))
    frames.sort(key=lambda f: f[0])
    out = [row[:] for row in grid]
    def can_horiz(f):
        r0,r1,c0,c1 = f
        H = r1-r0+1; W = c1-c0+1
        nc0 = c1+2; nc1 = nc0+W-1
        if nc1 >= w: return False
        for i in range(r0, r1+1):
            for j in range(nc0, nc1+1):
                if grid[i][j] != 0: return False
        return True
    def draw_horiz(f):
        r0,r1,c0,c1 = f
        H = r1-r0+1; W = c1-c0+1
        nc0 = c1+2; nc1 = nc0+W-1
        for i in range(r0, r1+1):
            for j in (nc0, nc1):
                out[i][j] = 1
        for j in range(nc0, nc1+1):
            for i in (r0, r1):
                out[i][j] = 1
    def can_vert_up(f):
        r0,r1,c0,c1 = f
        H = r1-r0+1; W = c1-c0+1
        nr1 = r0-2; nr0 = nr1 - H + 1
        if nr0 < 0: return False
        for i in range(nr0, nr1+1):
            for j in range(c0, c1+1):
                if grid[i][j] != 0: return False
        return True
    def can_vert_down(f):
        r0,r1,c0,c1 = f
        H = r1-r0+1; W = c1-c0+1
        nr0 = r1+2; nr1 = nr0 + H - 1
        if nr1 >= h: return False
        for i in range(nr0, nr1+1):
            for j in range(c0, c1+1):
                if grid[i][j] != 0: return False
        return True
    def draw_vert_up(f):
        r0,r1,c0,c1 = f
        H = r1-r0+1; W = c1-c0+1
        nr1 = r0-2; nr0 = nr1 - H + 1
        for j in range(c0, c1+1):
            for i in (nr0, nr1):
                out[i][j] = 8
        for i in range(nr0, nr1+1):
            out[i][c0] = 8
            out[i][c1] = 8
    def draw_vert_down(f):
        r0,r1,c0,c1 = f
        H = r1-r0+1; W = c1-c0+1
        nr0 = r1+2; nr1 = nr0 + H - 1
        for j in range(c0, c1+1):
            for i in (nr0, nr1):
                out[i][j] = 8
        for i in range(nr0, nr1+1):
            out[i][c0] = 8
            out[i][c1] = 8
    # identify bottommost
    if not frames:
        return out
    bottom = max(frames, key=lambda f: f[0])
    # horizontal: among frames except bottom, by c0
    hor_frame = None
    cand = [f for f in frames if f is not bottom]
    cand.sort(key=lambda f: f[2])
    for f in cand:
        if can_horiz(f):
            hor_frame = f
            draw_horiz(f)
            break
    # vertical: select extremes
    if len(frames) == 2:
        vert = [bottom]
    else:
        vert = [frames[0], frames[-1]]
    if hor_frame in vert:
        vert = [f for f in vert if f is not hor_frame]
    for f in vert:
        if can_vert_up(f):
            draw_vert_up(f)
        elif can_vert_down(f):
            draw_vert_down(f)
    return out