import numpy as np

def solve(grid):
    grid = np.array(grid)
    H, W = grid.shape
    grey = 5
    # find grey rows
    grey_rows = [i for i in range(H) if np.any(grid[i] == grey)]
    # find header row: first row above grey rows where all non-grey non-zero CCs are size 1
    from collections import deque
    def cc_sizes(row):
        vis = np.zeros(W, bool)
        sizes = []
        for j in range(W):
            if not vis[j] and grid[row,j] != 0 and grid[row,j] != grey:
                c = grid[row,j]
                cnt = 0
                q = deque([(row,j)])
                while q:
                    i0,j0 = q.popleft()
                    if 0 <= i0 < H and 0 <= j0 < W and not vis[j0] and grid[i0,j0]==c and i0==row:
                        vis[j0] = True
                        cnt += 1
                        q += [(row,j0-1),(row,j0+1)]
                sizes.append(cnt)
        return sizes
    first_g = min(grey_rows)
    header_row = None
    for i in range(first_g):
        sz = cc_sizes(i)
        if sz and max(sz)==1:
            header_row = i
            break
    # find shape1 rows: contiguous rows after header_row with any non-grey non-zero
    r = header_row+1
    shape1 = []
    while r < H and np.any((grid[r]!=0)&(grid[r]!=grey)):
        shape1.append(r)
        r += 1
    # find pillars columns
    gmask = np.any(grid==grey,axis=0)
    cols = np.where(gmask)[0]
    pillars = []
    j=0
    while j<len(cols):
        a=cols[j]
        if j+1<len(cols) and cols[j+1]==a+1:
            pillars.append((a,a+1)); j+=2
        else:
            j+=1
    n = len(pillars)
    # region data rows = rows immediately after each grey row with any non-grey non-zero
    data = []
    for g in grey_rows:
        i = g+1
        if i<H and np.any((grid[i]!=0)&(grid[i]!=grey)):
            data.append(i)
    # choose last two
    data = data[-2:]
    # bands: [shape1] if shape1 else [], then data
    bands = []
    if shape1:
        bands.append(shape1)
    for r in data:
        bands.append([r])
    B = len(bands)
    out_h = B*2 + (B-1)
    out_w = n*2 + (n-1)
    out = [[0]*out_w for _ in range(out_h)]
    for bi,rows in enumerate(bands):
        y0 = bi*3
        single = len(rows)==1
        for b,(c0,c1) in enumerate(pillars):
            x0 = b*3
            if not single:
                # header region: use header color
                # get header color at header_row in that column-range
                j0,j1 = c0,c1
                # header col-range = either exactly j0 or between pillars:
                # use value at header_row nearest to midpoint
                seg = grid[header_row,max(0,j0- (c0>0)):min(W,j1+2)]
                nonz = np.where((seg!=0)&(seg!=grey))[0]
                if nonz.size:
                    hc = int(seg[nonz[0]])
                else:
                    continue
                pts = [(i,j) for i in rows for j in range(j0,j1+2) if j<W and grid[i,j]!=0 and grid[i,j]!=grey]
                if not pts: continue
                is_ = [p[0] for p in pts]
                js = [p[1] for p in pts]
                i0,i1 = min(is_),max(is_)
                j0p,j1p = min(js),max(js)
                ph,iw = i1-i0+1, j1p-j0p+1
                mask = [[0]*iw for _ in range(ph)]
                for i,j in pts:
                    mask[i-i0][j-j0p]=1
                for i in range(ph):
                    for j in range(iw):
                        if mask[i][j]:
                            out[y0+i][x0+j] = hc
            else:
                i = rows[0]
                col = None
                if grid[i,c0]!=0 and grid[i,c0]!=grey: col=c0
                if grid[i,c1]!=0 and grid[i,c1]!=grey: col=c1
                if col is None: continue
                color = int(grid[i,col])
                # draw fallback horizontal L
                if col==c0:
                    # L
                    out[y0+0][x0+0]=color; out[y0+0][x0+1]=color
                    out[y0+1][x0+0]=color
                else:
                    # R
                    out[y0+0][x0+0]=color; out[y0+0][x0+1]=color
                    out[y0+1][x0+1]=color
    return out