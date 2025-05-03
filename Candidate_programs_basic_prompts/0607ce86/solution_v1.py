from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0]) if n else 0
    processed = [[False]*m for _ in range(n)]
    result = [[0]*m for _ in range(n)]
    while True:
        best = None
        for r in range(n):
            cols = [j for j in range(m) if grid[r][j] != 0 and not processed[r][j]]
            if not cols:
                continue
            c_start = min(cols)
            c_end = max(cols)
            w = c_end - c_start + 1
            h = 1
            while r+h < n and grid[r+h][c_start] != 0 and not processed[r+h][c_start] and grid[r+h][c_end] != 0 and not processed[r+h][c_end]:
                h += 1
            positions = []
            for rr in range(n - h + 1):
                ok = True
                for i in range(h):
                    if grid[rr+i][c_start] == 0 or processed[rr+i][c_start] or grid[rr+i][c_end] == 0 or processed[rr+i][c_end]:
                        ok = False
                        break
                if ok:
                    positions.append(rr)
            if len(positions) < 2:
                continue
            area = w * h
            if best is None or area > best[0]:
                best = (area, r, c_start, c_end, h, positions)
        if best is None:
            break
        _, _, c0, c1, h, poses = best
        for r0 in poses:
            for i in range(h):
                for j in range(c0, c1+1):
                    if grid[r0+i][j] != 0 and not processed[r0+i][j]:
                        result[r0+i][j] = grid[r0+i][j]
                        processed[r0+i][j] = True
    return result