from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c != 0 and not visited[y][x]:
                pts = []
                stack = [(y, x)]
                visited[y][x] = True
                while stack:
                    cy, cx = stack.pop()
                    pts.append((cy, cx))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == c:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                comps.append((c, pts))
    border_clusters = []
    for c, pts in comps:
        ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
        miny, maxy = min(ys), max(ys)
        minx, maxx = min(xs), max(xs)
        perim = []
        for xx in range(minx, maxx+1):
            perim.append((miny, xx)); perim.append((maxy, xx))
        for yy in range(miny+1, maxy):
            perim.append((yy, minx)); perim.append((yy, maxx))
        if perim:
            cnt = sum(1 for yy, xx in perim if grid[yy][xx] == c)
            if cnt >= len(perim)*0.6:
                border_clusters.append((miny, minx, maxy, maxx, c))
    border_clusters.sort(key=lambda t: (t[0], t[1]))
    out = []
    for miny, minx, maxy, maxx, c in border_clusters:
        iy1, iy2 = miny+1, maxy-1
        ix1, ix2 = minx+1, maxx-1
        if ix1>ix2 or iy1>iy2:
            out.append([c]*4)
            continue
        anomaly = None
        for yy in range(iy1, iy2+1):
            for xx in range(ix1, ix2+1):
                v = grid[yy][xx]
                if v != 0 and v != c:
                    anomaly = v
                    break
            if anomaly is not None:
                break
        intw = ix2 - ix1 + 1
        row = []
        for i in range(4):
            start = ix1 + int(i*intw/4)
            end = ix1 + int((i+1)*intw/4)
            if end <= start:
                end = start + 1
            found = False
            if anomaly is not None:
                for yy in range(iy1, iy2+1):
                    for xx in range(start, end):
                        if grid[yy][xx] == anomaly:
                            found = True
                            break
                    if found:
                        break
            row.append(anomaly if found else c)
        out.append(row)
    return out