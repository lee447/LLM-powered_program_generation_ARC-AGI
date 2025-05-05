from collections import Counter

def solve(grid):
    H = len(grid)
    W = len(grid[0])
    row_anchors = [i for i in range(H) if all(grid[i][j] == 0 for j in range(W))]
    col_anchors = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    out = [row[:] for row in grid]
    def rot(b):
        n = len(b)
        return [[b[j][n-1-i] for j in range(n)] for i in range(n)]
    def rotate(b, k):
        for _ in range(k % 4):
            b = rot(b)
        return b
    for bi in range(len(row_anchors)-1):
        r0 = row_anchors[bi] + 1
        r1 = row_anchors[bi+1]
        size = r1 - r0
        for bj in range(len(col_anchors)-1):
            c0 = col_anchors[bj] + 1
            c1 = col_anchors[bj+1]
            block = [[grid[r0+dr][c0+dc] for dc in range(size)] for dr in range(size)]
            cnt = Counter(v for row in block for v in row if v != 0)
            if len(cnt) < 2:
                continue
            a, b = cnt.most_common()
            border_color = a[0]
            fill_color = b[0]
            if any(block[0][c] == fill_color for c in range(size)):
                orient = 0
            elif any(block[r][size-1] == fill_color for r in range(size)):
                orient = 1
            elif any(block[size-1][c] == fill_color for c in range(size)):
                orient = 2
            else:
                orient = 3
            rb = rotate(block, orient)
            thr = size
            for c in range(size):
                if rb[0][c] == fill_color:
                    thr = c
                    break
            rb_out = [[border_color if dr+dc < thr else fill_color for dc in range(size)] for dr in range(size)]
            ob = rotate(rb_out, 4-orient)
            for dr in range(size):
                for dc in range(size):
                    out[r0+dr][c0+dc] = ob[dr][dc]
    return out