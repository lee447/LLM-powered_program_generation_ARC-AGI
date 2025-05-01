def solve(grid):
    h, w = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    colored = [(i,j,orig[i][j]) for i in range(h) for j in range(w) if orig[i][j]>1]
    for i,j,v in colored:
        counts = []
        for di,dj in dirs:
            ci, cj, cnt = i, j, 0
            while True:
                ni, nj = ci+di, cj+dj
                if 0<=ni<h and 0<=nj<w and orig[ni][nj]==1:
                    cnt += 1
                    ci, cj = ni, nj
                else:
                    break
            counts.append(cnt)
        maxc = max(counts)
        for (di,dj),cnt in zip(dirs, counts):
            if cnt==maxc and cnt>0:
                ni, nj = i+di, j+dj
                grid[ni][nj] = v
    return grid