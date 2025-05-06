def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque
    # find platform row
    best_row = max(range(h), key=lambda r: sum(1 for x in grid[r] if x != 0))
    # find background color
    row_vals = [c for c in grid[best_row] if c != 0]
    if row_vals:
        bg = max(set(row_vals), key=row_vals.count)
    else:
        bg = 0
    # find background region via BFS
    br = [[False]*w for _ in range(h)]
    dq = deque()
    for c in range(w):
        if grid[best_row][c] == bg:
            br[best_row][c] = True
            dq.append((best_row, c))
    while dq:
        y, x = dq.popleft()
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny, nx = y+dy, x+dx
            if 0 <= ny < h and 0 <= nx < w and not br[ny][nx] and grid[ny][nx] == bg:
                br[ny][nx] = True
                dq.append((ny, nx))
    # new grid: keep only bg region
    out = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if br[y][x]:
                out[y][x] = bg
    # anchor row
    anchor = best_row - 1
    # find hole segments on anchor
    holes = [c for c in range(w) if out[anchor][c] == 0]
    segs = []
    i = 0
    while i < len(holes):
        j = i
        while j+1 < len(holes) and holes[j+1] == holes[j] + 1:
            j += 1
        segs.append([holes[i], holes[j]])
        i = j+1
    # sort segments by length desc
    segs.sort(key=lambda s: s[1]-s[0], reverse=True)
    # find other regions
    visited = [[False]*w for _ in range(h)]
    regions = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0 and not br[y][x] and not visited[y][x]:
                col = grid[y][x]
                q = deque([(y,x)])
                visited[y][x] = True
                cells = []
                ymin = y; ymax = y; xmin = x; xmax = x
                while q:
                    yy, xx = q.popleft()
                    cells.append((yy,xx))
                    ymin = min(ymin, yy); ymax = max(ymax, yy)
                    xmin = min(xmin, xx); xmax = max(xmax, xx)
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==col and not br[ny][nx]:
                            visited[ny][nx] = True
                            q.append((ny,nx))
                regions.append({
                    'cells': cells, 'col': col,
                    'ymin': ymin, 'ymax': ymax, 'xmin': xmin, 'xmax': xmax,
                    'assigned': False
                })
    # sort regions by size desc
    regions.sort(key=lambda r: len(r['cells']), reverse=True)
    # assign segments
    for reg in regions:
        height = reg['ymax'] - reg['ymin'] + 1
        width = reg['xmax'] - reg['xmin'] + 1
        for i, s in enumerate(segs):
            seg_len = s[1] - s[0] + 1
            # try no rotate
            if width <= seg_len:
                reg['assigned'] = True
                reg['rotate'] = False
                reg['seg'] = s
                segs.pop(i)
                break
            # try rotate
            if height <= seg_len:
                reg['assigned'] = True
                reg['rotate'] = True
                reg['seg'] = s
                segs.pop(i)
                break
    # place regions
    for reg in regions:
        col = reg['col']
        ymin, ymax, xmin, xmax = reg['ymin'], reg['ymax'], reg['xmin'], reg['xmax']
        height = ymax - ymin + 1
        width = xmax - xmin + 1
        if reg['assigned']:
            s0, s1 = reg['seg']
            seg_start = s0
            if not reg['rotate']:
                for (y, x) in reg['cells']:
                    ydown = ymax - y
                    ny = anchor - ydown
                    nx = seg_start + (x - xmin)
                    out[ny][nx] = col
            else:
                new_h = width
                for (y, x) in reg['cells']:
                    dy = y - ymin; dx = x - xmin
                    new_dy = dx
                    new_dx = height - 1 - dy
                    down = new_h - 1 - new_dy
                    ny = anchor - down
                    nx = seg_start + new_dx
                    out[ny][nx] = col
        else:
            for (y, x) in reg['cells']:
                out[y][x] = col
    return out