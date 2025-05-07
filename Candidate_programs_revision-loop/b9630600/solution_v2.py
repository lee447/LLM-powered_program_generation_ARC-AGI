def solve(grid):
    H = len(grid)
    W = len(grid[0])
    out = [row[:] for row in grid]
    def runs(row):
        segs = []
        in3 = False
        for i,v in enumerate(row):
            if v==3 and not in3:
                start = i
                in3 = True
            if v!=3 and in3:
                segs.append((start,i-1))
                in3 = False
        if in3:
            segs.append((start,W-1))
        return segs
    chunk_starts = []
    for r in range(H):
        if any(v==3 for v in grid[r]):
            if r==0 or all(grid[r-1][c]==0 for c in range(W)):
                if runs(grid[r]):
                    chunk_starts.append(r)
    for r in chunk_starts:
        segs = runs(grid[r])
        if r+1>=H: continue
        if len(segs)>1:
            for i in range(len(segs)-1):
                a = segs[i][1]
                b = segs[i+1][0]
                for c in range(a,b+1):
                    out[r+1][c] = 3
        else:
            a,b = segs[0]
            length = b-a+1
            center = (a+b)//2
            odd = length%2==1
            for c in range(a,b+1):
                if odd and c==center:
                    continue
                out[r+1][c] = 3
    return out