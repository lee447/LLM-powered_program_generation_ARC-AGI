from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                cells = []
                rmin = rmax = i
                cmin = cmax = j
                while stack:
                    x, y = stack.pop()
                    cells.append((x, y))
                    if x < rmin: rmin = x
                    if x > rmax: rmax = x
                    if y < cmin: cmin = y
                    if y > cmax: cmax = y
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                comps.append((cells, len(cells), rmin, rmax, cmin, cmax))
    _, _, rmin, rmax, cmin, cmax = max(comps, key=lambda x: x[1])
    def outside(i, j):
        return not (rmin <= i <= rmax and cmin <= j <= cmax)
    mapping = {}
    for i in range(h):
        for j in range(w-1):
            a, b = grid[i][j], grid[i][j+1]
            if a and b and a != b and outside(i, j) and outside(i, j+1):
                mapping[b] = a
    out = []
    for i in range(rmin, rmax+1):
        row = []
        for j in range(cmin, cmax+1):
            v = grid[i][j]
            row.append(mapping.get(v, v))
        out.append(row)
    return out