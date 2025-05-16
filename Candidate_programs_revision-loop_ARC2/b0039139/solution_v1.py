def solve(grid):
    h = len(grid)
    w = len(grid[0])
    stripe_rows = [i for i in range(h) if all(grid[i][j] == 1 for j in range(w))]
    stripe_cols = [j for j in range(w) if all(grid[i][j] == 1 for i in range(h))]
    if stripe_rows:
        orientation = 'horizontal'
        bounds = [-1] + stripe_rows + [h]
        segs = []
        for a, b in zip(bounds, bounds[1:]):
            if a+1 <= b-1:
                segs.append(grid[a+1:b])
        s1 = segs[0]
        s3 = segs[2]
        s4 = segs[3]
        H3 = len(s3)
        H4 = len(s4)
        sh = len(s1)
        sw = len(s1[0])
        # find M in s1
        minr = sh; maxr = -1; minc = sw; maxc = -1
        for i in range(sh):
            for j in range(sw):
                if s1[i][j] != 0:
                    if i < minr: minr = i
                    if i > maxr: maxr = i
                    if j < minc: minc = j
                    if j > maxc: maxc = j
        M = [row[minc:maxc+1] for row in s1[minr:maxr+1]]
        HP = len(M); WP = len(M[0])
        # colors
        prim = None
        for row in s1:
            for v in row:
                if v != 0:
                    prim = v; break
            if prim is not None: break
        c3 = None
        for row in s3:
            for v in row:
                if v != 0:
                    c3 = v; break
            if c3 is not None: break
        c4 = None
        for row in s4:
            for v in row:
                if v != 0:
                    c4 = v; break
            if c4 is not None: break
        P = [[c3 if M[i][j] == prim else c4 for j in range(WP)] for i in range(HP)]
        if c4 > c3:
            npos = H4 - HP + 1
        else:
            npos = H3 - HP + 1
        Hout = HP * npos + (npos - 1)
        Wout = WP
        out = [[0]*Wout for _ in range(Hout)]
        for k in range(npos):
            base = k*(HP+1)
            for i in range(HP):
                for j in range(WP):
                    out[base+i][j] = P[i][j]
            if k < npos-1:
                for j in range(Wout):
                    out[base+HP][j] = c4
        return out
    else:
        orientation = 'vertical'
        bounds = [-1] + stripe_cols + [w]
        segs = []
        for a, b in zip(bounds, bounds[1:]):
            if a+1 <= b-1:
                segs.append([row[a+1:b] for row in grid])
        s1 = segs[0]
        s3 = segs[2]
        s4 = segs[3]
        SH = len(s1)
        SW = len(s1[0])
        # find M in s1
        minr = SH; maxr = -1; minc = SW; maxc = -1
        for i in range(SH):
            for j in range(SW):
                if s1[i][j] != 0:
                    if i < minr: minr = i
                    if i > maxr: maxr = i
                    if j < minc: minc = j
                    if j > maxc: maxc = j
        M = [row[minc:maxc+1] for row in [r[minc:maxc+1] for r in s1[minr:maxr+1]]]
        # note: above listcomp is wrong, fix slicing
        M = [r[minc:maxc+1] for r in s1[minr:maxr+1]]
        HP = len(M); WP = len(M[0])
        prim = None
        for row in s1:
            for v in row:
                if v != 0:
                    prim = v; break
            if prim is not None: break
        c3 = None
        for row in s3:
            for v in row:
                if v != 0:
                    c3 = v; break
            if c3 is not None: break
        c4 = None
        for row in s4:
            for v in row:
                if v != 0:
                    c4 = v; break
            if c4 is not None: break
        P = [[c3 if M[i][j] == prim else c4 for j in range(WP)] for i in range(HP)]
        W3 = len(s3[0])
        W4 = len(s4[0])
        if c4 > c3:
            npos = W4 - WP + 1
        else:
            npos = W3 - WP + 1
        Hout = HP
        Wout = WP * npos + (npos - 1)
        out = [[0]*Wout for _ in range(Hout)]
        for k in range(npos):
            base = k*(WP+1)
            for i in range(HP):
                for j in range(WP):
                    out[i][base+j] = P[i][j]
            if k < npos-1:
                for i in range(Hout):
                    out[i][base+WP] = c4
        return out