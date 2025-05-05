from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    bands = []
    in_band = False
    for r in range(H):
        if any(grid[r][c] != 0 for c in range(W)):
            if not in_band:
                start = r
                in_band = True
        else:
            if in_band:
                bands.append((start, r - 1))
                in_band = False
    if in_band:
        bands.append((start, H - 1))

    visited = [[False]*W for _ in range(H)]
    clusters = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 2 and not visited[r][c]:
                stack = [(r, c)]
                comp = []
                visited[r][c] = True
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == 2:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                clusters.append(comp)

    band_clusters = [[] for _ in bands]
    for comp in clusters:
        minr = min(x for x,y in comp)
        for i,(a,b) in enumerate(bands):
            if a <= minr <= b:
                band_clusters[i].append(comp)
                break

    out = [row[:] for row in grid]
    last = len(bands) - 1
    mid = len(bands) // 2

    for i, comps in enumerate(band_clusters):
        comps.sort(key=lambda comp: min(y for x,y in comp))
        # detect closed frame (size==10) vs open shape
        sz = len(comps[0])
        is_closed = (sz == 10)
        if is_closed:
            j = (i + 1) % 2
            col = 8 if i < last else 3
            for x,y in comps[j]:
                out[x][y] = col
        else:
            if i < mid:
                # only left
                for x,y in comps[0]:
                    out[x][y] = 8
            elif i == mid:
                # both
                for x,y in comps[0]:
                    out[x][y] = 8
                for x,y in comps[1]:
                    out[x][y] = 3
            else:
                # only right
                for x,y in comps[1]:
                    out[x][y] = 3

    return out