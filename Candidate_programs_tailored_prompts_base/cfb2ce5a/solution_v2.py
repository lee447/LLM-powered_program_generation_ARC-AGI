def solve(grid):
    h, w = len(grid), len(grid[0])
    def find_border():
        for i in range(h):
            for j in range(w):
                if grid[i][j]!=0:
                    return i,j
    br, bc = find_border()
    # detect upper‐left mosaic
    two = set()
    for i in range(br+1, h):
        for j in range(bc+1, w):
            if grid[i][j] and len(two)<2 and (i-br<=5 and j-bc<=5):
                two.add(grid[i][j])
    two = list(two)
    # find mosaic size
    mh=0; mw=0
    for i in range(br+1, h):
        row = [grid[i][j] for j in range(bc+1, w)]
        if all(c in two or c==0 for c in row):
            mh+=1
        else:
            break
    for j in range(bc+1, w):
        col = [grid[i][j] for i in range(br+1, br+1+mh)]
        if all(c in two or c==0 for c in col):
            mw+=1
        else:
            break
    # find two seeds outside mosaic in upper half
    seeds=[]
    for i in range(br+1, br+1+mh):
        for j in range(bc+1+mw, w-1):
            if grid[i][j]!=0:
                seeds.append((i-br-1, j-bc-1, grid[i][j]))
    if len(seeds)>2: seeds=seeds[:2]
    # build block by BFS
    bh, bw = mh, mh
    block = [[0]*bw for _ in range(bh)]
    from collections import deque
    dist = [[None]*bw for _ in range(bh)]
    owner = [[None]*bw for _ in range(bh)]
    Q = deque()
    for r,c,v in seeds:
        if 0<=r<bh and 0<=c<bw:
            dist[r][c]=0; owner[r][c]=v; Q.append((r,c,v))
    while Q:
        r,c,v=Q.popleft()
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr,cc=r+dr,c+dc
            if 0<=rr<bh and 0<=cc<bw:
                nd = dist[r][c]+1
                if dist[rr][cc] is None or nd<dist[rr][cc] or (nd==dist[rr][cc] and v<owner[rr][cc]):
                    dist[rr][cc]=nd; owner[rr][cc]=v
                    Q.append((rr,cc,v))
    for i in range(bh):
        for j in range(bw):
            block[i][j]=owner[i][j] or 0
    # collect lower seeds
    lower = {}
    for i in range(br+1+mh, h-1):
        for j in range(bc+1, w-1):
            c = grid[i][j]
            if c and c not in two:
                lower.setdefault(c, []).append((i,j))
    # rebuild lower in bottom-left
    out = [[0]*w for _ in range(h)]
    # copy border
    for i in range(h):
        for j in range(w):
            if i==0 or j==0 or i==h-1 or j==w-1:
                out[i][j]=0
    # copy mosaic
    for i in range(mh):
        for j in range(mw):
            out[br+1+i][bc+1+j] = grid[br+1+i][bc+1+j]
    # paste block
    for i in range(bh):
        for j in range(bw):
            out[br+1+i][bc+1+mw+j] = block[i][j]
    # place lower clusters
    left = br+1+mh
    keys=sorted(lower)
    col = bc+1
    for k in keys:
        pts = lower[k]
        cnt = len(pts)
        side = int(cnt**0.5+0.999)
        for idx,(i,j) in enumerate(pts):
            r = left + idx//side
            c = col + idx%side
            if r<h-1 and c<w-1:
                out[r][c]=k
        col += side
    return out