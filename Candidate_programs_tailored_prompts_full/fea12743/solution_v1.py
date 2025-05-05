def solve(grid):
    H = len(grid)
    W = len(grid[0])
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
                stack = [(r,c)]
                comp = []
                visited[r][c] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == 2:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                clusters.append(comp)
    band_clusters = [[] for _ in bands]
    for comp in clusters:
        minr = min(x for x,y in comp)
        for i,(a,b) in enumerate(bands):
            if a <= minr <= b:
                band_clusters[i].append(comp)
                break
    mapping = { (0,'right'):8, (1,'left'):8, (1,'right'):3, (2,'right'):3 }
    out = [row[:] for row in grid]
    for bi, comps in enumerate(band_clusters):
        comps.sort(key=lambda comp: min(y for x,y in comp))
        for si, comp in enumerate(comps):
            side = 'left' if si == 0 else 'right'
            col = mapping.get((bi, side))
            if col is not None:
                for x,y in comp:
                    out[x][y] = col
    return out