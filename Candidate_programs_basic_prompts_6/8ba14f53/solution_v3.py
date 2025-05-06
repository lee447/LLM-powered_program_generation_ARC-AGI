from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    cols_by_color = {}
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v != 0:
                if v not in cols_by_color:
                    cols_by_color[v] = [r, r, c, c]
                else:
                    mnr, mxr, mnc, mxc = cols_by_color[v]
                    cols_by_color[v] = [min(mnr, r), max(mxr, r), min(mnc, c), max(mxc, c)]
    colors = sorted(cols_by_color.items(), key=lambda x: x[1][2])
    hole_counts = []
    for color, (mnr, mxr, mnc, mxc) in colors:
        h, w = mxr - mnr + 1, mxc - mnc + 1
        visited = [[False]*w for _ in range(h)]
        stack = []
        for i in range(h):
            for j in (0, w-1):
                rr, cc = mnr + i, mnc + j
                if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 0 and not visited[i][j]:
                    visited[i][j] = True
                    stack.append((i, j))
        for j in range(w):
            for i in (0, h-1):
                rr, cc = mnr + i, mnc + j
                if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 0 and not visited[i][j]:
                    visited[i][j] = True
                    stack.append((i, j))
        while stack:
            i, j = stack.pop()
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i+di, j+dj
                if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj]:
                    rr, cc = mnr+ni, mnc+nj
                    if grid[rr][cc] == 0:
                        visited[ni][nj] = True
                        stack.append((ni, nj))
        cnt = 0
        for i in range(h):
            for j in range(w):
                if grid[mnr+i][mnc+j] == 0 and not visited[i][j]:
                    cnt += 1
        hole_counts.append((color, cnt))
    out_h = rows - 1
    out_w = cols // 3
    out = [[0]*out_w for _ in range(out_h)]
    prev = 0
    for color, cnt in hole_counts:
        start = ((prev + out_w - 1)//out_w)*out_w
        for k in range(cnt):
            idx = start + k
            if idx >= out_h * out_w:
                break
            r, c = divmod(idx, out_w)
            out[r][c] = color
        prev += cnt
    return out