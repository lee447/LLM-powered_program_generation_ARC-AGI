def solve(grid):
    h = len(grid)
    w = len(grid[0])
    grey = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==5]
    row_counts = {}
    col_counts = {}
    for r,c in grey:
        row_counts[r] = row_counts.get(r,0)+1
        col_counts[c] = col_counts.get(c,0)+1
    bar_rows = [r for r,cnt in row_counts.items() if cnt>1]
    bar_cols = [c for c,cnt in col_counts.items() if cnt>1]
    out = [row[:] for row in grid]
    def bfs(sr,sc):
        col = grid[sr][sc]
        vis = {(sr,sc)}
        q = [(sr,sc)]
        res = [(sr,sc,grid[sr][sc])]
        while q:
            r,c = q.pop(0)
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc = r+dr,c+dc
                if 0<=nr<h and 0<=nc<w and (nr,nc) not in vis:
                    v = grid[nr][nc]
                    if v!=0 and v!=5:
                        vis.add((nr,nc))
                        q.append((nr,nc))
                        res.append((nr,nc,v))
        return res
    if bar_cols:
        c = bar_cols[0]
        rs = [r for r in range(h) if (r,c) in grey]
        r1,r2 = min(rs),max(rs)
        seed1 = None
        for r in rs:
            if c+1<w and grid[r][c+1] not in (0,5):
                seed1 = (r,c+1); break
        if seed1:
            samp1 = bfs(seed1[0],seed1[1])
            sr1 = min(r for r,c,v in samp1)
            sr2 = max(r for r,c,v in samp1)
            sc1 = min(c for r,c,v in samp1)
            #sc2 = max(c for r,c,v in samp1)
            M = sr2-sr1+1
            for sr,sc,v in samp1:
                dr = sr-sr1
                dc = sc-sc1
                for tr in range(r1+dr, r2+1, M):
                    out[tr][c+1+dc] = v
    if bar_rows:
        r = bar_rows[0]
        cs = [c for c in range(w) if (r,c) in grey]
        c1,c2 = min(cs),max(cs)
        seed2 = None
        for c in cs:
            if r+1<h and grid[r+1][c] not in (0,5):
                seed2 = (r+1,c); break
        if seed2:
            samp2 = bfs(seed2[0],seed2[1])
            sr1 = min(r for r,c,v in samp2)
            #sr2 = max(r for r,c,v in samp2)
            sc1 = min(c for r,c,v in samp2)
            W = max(c for r,c,v in samp2)-sc1+1
            for sr,sc,v in samp2:
                dr = sr-sr1
                dc = sc-sc1
                for tc in range(c1+dc, c2+1, W):
                    out[r+1+dr][tc] = v
    return out