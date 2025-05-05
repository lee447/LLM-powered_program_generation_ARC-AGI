from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    frames = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 0 and not visited[i][j]:
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == c:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                rs = [x for x,_ in comp]
                cs = [y for _,y in comp]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                H = r1 - r0 + 1
                W = c1 - c0 + 1
                if len(comp) == 2*(H + W) - 4:
                    frames.append((c, r0, r1, c0, c1))
    m = len(frames)
    if m == 0:
        return []
    rs0 = [f[1] for f in frames]
    rs1 = [f[2] for f in frames]
    cs0 = [f[3] for f in frames]
    cs1 = [f[4] for f in frames]
    row_case = max(rs0) <= min(rs1)
    col_case = max(cs0) <= min(cs1)
    frames.sort(key=lambda f: f[3])
    if not row_case and col_case:
        Hbox = frames[0][2] - frames[0][1] + 1
        Wbox = frames[0][4] - frames[0][3] + 1
        out = [[0]*Wbox for _ in range(Hbox*m)]
        for idx, (c, r0, r1, c0, c1) in enumerate(frames):
            for i in range(Hbox):
                for j in range(Wbox):
                    out[idx*Hbox + i][j] = grid[r0 + i][c0 + j]
    else:
        Hbox = frames[0][2] - frames[0][1] + 1
        Wbox = frames[0][4] - frames[0][3] + 1
        out = [[0]*(Wbox*m) for _ in range(Hbox)]
        for idx, (c, r0, r1, c0, c1) in enumerate(frames):
            for i in range(Hbox):
                for j in range(Wbox):
                    out[i][idx*Wbox + j] = grid[r0 + i][c0 + j]
    return out