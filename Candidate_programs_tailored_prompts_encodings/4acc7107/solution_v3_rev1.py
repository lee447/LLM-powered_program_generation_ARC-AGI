from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    comps = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != 0 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==v:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                comps.setdefault(v, []).append(comp)
    colors = sorted(comps.keys())
    out = [[0]*w for _ in range(h)]
    start_row = h//2
    for side,color in enumerate(colors):
        row = start_row
        for comp in sorted(comps[color], key=lambda c: min(x for x,y in c)):
            size = len(comp)
            r = int(size**0.5)
            if r*r==size:
                sh, sw = r, r
            else:
                sh, sw = 1, size
            col0 = w-sw if side==0 else 0
            for i in range(sh):
                for j in range(sw):
                    out[row+i][col0+j] = color
            row += sh+1
    return out