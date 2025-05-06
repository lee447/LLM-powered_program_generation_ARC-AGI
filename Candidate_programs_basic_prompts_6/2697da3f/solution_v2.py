from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    min_r = rows; max_r = -1; min_c = cols; max_c = -1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
                if j < min_c: min_c = j
                if j > max_c: max_c = j
    block = [row[min_c:max_c+1] for row in grid[min_r:max_r+1]]
    h0 = len(block); w0 = len(block[0])
    short, long = (h0, w0) if h0 <= w0 else (w0, h0)
    N = 2*long + short
    cs = long; ce = long + short
    out = [[0]*N for _ in range(N)]
    def rot_cw(m):
        r, c = len(m), len(m[0])
        return [[m[r-1-j][i] for j in range(r)] for i in range(c)]
    def rot_180(m):
        r, c = len(m), len(m[0])
        return [[m[r-1-i][c-1-j] for j in range(c)] for i in range(r)]
    def rot_ccw(m):
        r, c = len(m), len(m[0])
        return [[m[j][c-1-i] for j in range(r)] for i in range(c)]
    b = block
    if h0 <= w0:
        for i in range(h0):
            for j in range(w0):
                out[cs + i][j] = b[i][j]
        r1 = rot_cw(b)
        for i in range(w0):
            for j in range(h0):
                out[i][cs + j] = r1[i][j]
        r2 = rot_180(b)
        for i in range(h0):
            for j in range(w0):
                out[cs + i][ce + j] = r2[i][j]
        r3 = rot_ccw(b)
        for i in range(w0):
            for j in range(h0):
                out[ce + i][cs + j] = r3[i][j]
    else:
        r1 = rot_cw(b)
        for i in range(short):
            for j in range(long):
                out[cs + i][j] = r1[i][j]
        r2 = rot_180(r1)
        for i in range(long):
            for j in range(short):
                out[i][cs + j] = r2[i][j]
        r3 = rot_ccw(b)
        for i in range(short):
            for j in range(long):
                out[cs + i][ce + j] = b[j][short-1-i]
        r4 = rot_180(b)
        for i in range(long):
            for j in range(short):
                out[ce + i][cs + j] = r4[j][i]
    return out