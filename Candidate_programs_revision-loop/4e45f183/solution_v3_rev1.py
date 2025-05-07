def solve(grid):
    n = len(grid)
    bs = (n - 4) // 3
    step = bs + 1
    colors = sorted({v for row in grid for v in row if v})
    c1, c2 = colors
    def block_counts(bi, bj):
        top, left = 1 + bi*step, 1 + bj*step
        cnt = {c1:0, c2:0}
        for i in range(bs):
            for j in range(bs):
                v = grid[top+i][left+j]
                if v in cnt: cnt[v] += 1
        return cnt
    cntc = block_counts(1,1)
    plus_shape = c1 if cntc[c1] > cntc[c2] else c2
    plus_back = c2 if plus_shape is c1 else c1
    cnt00 = block_counts(0,0)
    L_shape1 = c1 if cnt00[c1] == 3 else c2
    L_shape2 = c2 if L_shape1 is c1 else c1
    out = [[0]*n for _ in range(n)]
    mid = bs//2
    for bi in range(3):
        for bj in range(3):
            top, left = 1 + bi*step, 1 + bj*step
            if bi==1 or bj==1:
                for i in range(bs):
                    for j in range(bs):
                        out[top+i][left+j] = plus_back
                for k in range(bs):
                    out[top+mid][left+k] = plus_shape
                    out[top+k][left+mid] = plus_shape
            else:
                shape = L_shape1 if (bi,bj) in ((0,0),(2,2)) else L_shape2
                for i in range(bs):
                    for j in range(bs):
                        out[top+i][left+j] = plus_back
                if bi==0 and bj==0:
                    pts = [(0,0),(0,1),(1,0)]
                elif bi==0 and bj==2:
                    pts = [(0,bs-1),(0,bs-2),(1,bs-1)]
                elif bi==2 and bj==0:
                    pts = [(bs-1,0),(bs-1,1),(bs-2,0)]
                else:
                    pts = [(bs-1,bs-1),(bs-1,bs-2),(bs-2,bs-1)]
                for dx,dy in pts:
                    out[top+dx][left+dy] = shape
    return out