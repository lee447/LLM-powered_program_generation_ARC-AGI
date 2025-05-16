from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] != bg and not visited[r][c]:
                v = grid[r][c]
                q = deque([(r, c)])
                visited[r][c] = True
                comp = []
                while q:
                    rr, cc = q.popleft()
                    comp.append((rr, cc))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == v:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                rows = [x for x,_ in comp]
                r0 = min(rows)
                if r0 < 5:
                    continue
                row_pts = sorted(c0 for rr, c0 in comp if rr == r0)
                n = len(row_pts)
                if n == 0 or n == 2:
                    continue
                hl = 9 if v != 9 else 1
                nr = r0 - 5
                if any(row_pts[i+1] == row_pts[i] + 1 for i in range(n-1)):
                    curr = [row_pts[0]]
                    runs = []
                    for c0 in row_pts[1:]:
                        if c0 == curr[-1] + 1:
                            curr.append(c0)
                        else:
                            runs.append(curr)
                            curr = [c0]
                    runs.append(curr)
                    if len(runs) > 1:
                        starts = [run[0] for run in runs]
                        spacing = starts[1] - starts[0]
                        for i in range(len(starts)):
                            nc = i * spacing
                            if 0 <= nr < h and 0 <= nc < w:
                                out[nr][nc] = hl
                        continue
                if n == 1:
                    nc = row_pts[0]
                    if 0 <= nr < h and 0 <= nc < w:
                        out[nr][nc] = hl
                else:
                    mid = n // 2
                    for i, c0 in enumerate(row_pts):
                        nc = c0
                        if 0 <= nr < h and 0 <= nc < w:
                            if n % 2 == 1 and i == mid:
                                out[nr][nc] = hl
                            else:
                                out[nr][nc] = v
    return out