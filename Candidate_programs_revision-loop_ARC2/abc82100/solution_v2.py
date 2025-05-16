def solve(grid):
    h, w = len(grid), len(grid[0])
    segs = []
    used = [[False]*w for _ in range(h)]
    for i in range(h):
        j = 0
        while j < w:
            if grid[i][j] != 0:
                c = grid[i][j]
                k = j
                while k < w and grid[i][k]==c:
                    k += 1
                if k-j>1:
                    segs.append(("H", i, j, k-j, c))
                    for x in range(j, k):
                        used[i][x]=True
                j = k
            else:
                j+=1
    for j in range(w):
        i = 0
        while i < h:
            if grid[i][j] != 0 and not used[i][j]:
                c = grid[i][j]
                k = i
                while k < h and grid[k][j]==c:
                    k += 1
                if k-i>1:
                    segs.append(("V", j, i, k-i, c))
                i = k
            else:
                i+=1
    segs.sort(key=lambda x: -x[3])
    out = [[0]*w for _ in range(h)]
    hr = vr = 0
    for ori, a, b, L, c in segs:
        if ori=="H":
            if hr<h:
                for x in range(L):
                    out[hr][x] = c
                hr += 1
        else:
            if vr<w:
                for y in range(L):
                    out[y][vr] = c
                vr += 1
    return out