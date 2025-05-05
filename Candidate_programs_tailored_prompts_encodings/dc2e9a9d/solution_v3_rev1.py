from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 3 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==3:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                if len(comp)>1:
                    clusters.append(comp)
    def bbox(comp):
        rs = [r for r,c in comp]; cs = [c for r,c in comp]
        return min(rs), max(rs), min(cs), max(cs)
    def make_mask(comp, r0, c0):
        return [(r-r0, c-c0) for r,c in comp]
    for comp in clusters:
        r0,r1,c0,c1 = bbox(comp)
        mask = make_mask(comp, r0, c0)
        height, width = r1-r0+1, c1-c0+1
        shift = None
        hp = width+1; vp = height+1
        right = w-1-c1; left = c0; down = h-1-r1; up = r0
        # decide orientation
        if width>=height:
            # try horizontal
            if right>=hp:
                shift = (0, hp)
            elif left>=hp:
                shift = (0, -hp)
            elif down>=vp:
                shift = (vp, 0)
            elif up>=vp:
                shift = (-vp, 0)
        else:
            if down>=vp:
                shift = (vp, 0)
            elif up>=vp:
                shift = (-vp, 0)
            elif right>=hp:
                shift = (0, hp)
            elif left>=hp:
                shift = (0, -hp)
        if not shift:
            continue
        dr,dc = shift
        color = 1 if dc!=0 else 8
        for dr0,dc0 in mask:
            rr, cc = r0+dr0+dr, c0+dc0+dc
            if 0<=rr<h and 0<=cc<w and grid[rr][cc]==0:
                grid[rr][cc] = color
    return grid