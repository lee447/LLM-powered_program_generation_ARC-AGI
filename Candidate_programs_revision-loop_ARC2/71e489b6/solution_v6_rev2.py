from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False] * w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                comps.append(comp)
    if not comps:
        return [row[:] for row in grid]
    largest_index = 0
    max_len = len(comps[0])
    for idx, comp in enumerate(comps):
        if len(comp) > max_len:
            max_len = len(comp)
            largest_index = idx
    out = [row[:] for row in grid]
    for idx, comp in enumerate(comps):
        if idx == largest_index:
            continue
        for x, y in comp:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx or dy:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 0:
                            out[nx][ny] = 7
    return out