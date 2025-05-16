def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = None
    freq = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq.items(), key=lambda x: x[1])[0]
    def find_rects():
        seen = set()
        rects = []
        for i in range(h):
            for j in range(w):
                c = grid[i][j]
                if c!=bg and (i,j) not in seen:
                    # detect rectangle of color c
                    # find extent right
                    j0 = j
                    while j0+1<w and grid[i][j0+1]==c:
                        j0+=1
                    # find extent down
                    i0 = i
                    while i0+1<h and all(grid[i0+1][x]==c for x in range(j, j0+1)):
                        i0+=1
                    # record border cells
                    for ii in range(i, i0+1):
                        for jj in range(j, j0+1):
                            if (ii==i or ii==i0 or jj==j or jj==j0) and grid[ii][jj]==c:
                                seen.add((ii,jj))
                    rects.append((i,i0,j,j0,c))
        return rects
    out = [row[:] for row in grid]
    for top,bottom,left,right,c in find_rects():
        ih = bottom-top-1
        iw = right-left-1
        if ih>0 and iw>0 and ih%2==1:
            mid = top + 1 + ih//2
            for x in range(left+1, right):
                if (x - (left+1)) % 2 == 0 and out[mid][x]==bg:
                    out[mid][x] = c
    return out