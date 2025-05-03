def solve(grid):
    h, w = len(grid), len(grid[0])
    frames = []
    for i in range(h):
        for j in range(w):
            if i+3<h and j+3<w:
                ok = True
                for x in range(4):
                    if grid[i][j+x]!=1 or grid[i+3][j+x]!=1 or grid[i+x][j]!=1 or grid[i+x][j+3]!=1:
                        ok = False; break
                if ok:
                    interior = (grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j+1],grid[i+2][j+2])
                    frames.append(((i,j),interior))
    # find template frame: the one whose interior tuple is unique
    counts = {}
    for _,ints in frames:
        counts[ints] = counts.get(ints,0)+1
    tpl = next(ints for _,ints in frames if counts[ints]==1)
    tpl_frame = next(pos for pos,ints in frames if ints==tpl)
    # sort frames into 3x3 by position
    rows = sorted(set(p[0] for p,_ in frames))
    cols = sorted(set(p[1] for p,_ in frames))
    rows.sort(); cols.sort()
    def rot2(mat):
        return (mat[2],mat[0],mat[3],mat[1])
    def rot_k(mat,k):
        for _ in range(k): mat = rot2(mat)
        return mat
    tr = rows.index(tpl_frame[0])
    tc = cols.index(tpl_frame[1])
    out = [row[:] for row in grid]
    for (i,j),_ in frames:
        r = rows.index(i); c = cols.index(j)
        k = ((c-tc)-(r-tr))%4
        m = rot_k(tpl,k)
        out[i+1][j+1] = m[0]
        out[i+1][j+2] = m[1]
        out[i+2][j+1] = m[2]
        out[i+2][j+2] = m[3]
    return out