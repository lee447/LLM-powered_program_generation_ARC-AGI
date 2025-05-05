from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for r in range(h):
        for c in range(w):
            if not visited[r][c] and grid[r][c] != bg:
                color = grid[r][c]
                stack = [(r, c)]
                comp = []
                visited[r][c] = True
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            if dx == 0 and dy == 0:
                                continue
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < h and 0 <= ny < w:
                                if not visited[nx][ny] and grid[nx][ny] == color:
                                    visited[nx][ny] = True
                                    stack.append((nx, ny))
                comps.append((color, comp))
    if not comps:
        return grid
    skip_color, skip_comp = max(comps, key=lambda x: len(x[1]))
    out = [row[:] for row in grid]
    for color, comp in comps:
        if comp is skip_comp:
            continue
        rs = [r for r, _ in comp]
        cs = [c for _, c in comp]
        rmin, rmax = min(rs), max(rs)
        cmin, cmax = min(cs), max(cs)
        for i in range(rmin, rmax+1):
            for j in range(cmin, cmax+1):
                out[i][j] = color
    return out