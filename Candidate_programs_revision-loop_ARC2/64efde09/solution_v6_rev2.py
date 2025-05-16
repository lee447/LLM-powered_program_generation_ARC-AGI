from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = {}
    for row in grid:
        for c in row:
            cnt[c] = cnt.get(c, 0) + 1
    bg = max(cnt, key=cnt.get)
    row_bg = [all(grid[i][j] == bg for j in range(w)) for i in range(h)]
    row_segs = []
    i = 0
    while i < h:
        if not row_bg[i]:
            start = i
            while i < h and not row_bg[i]:
                i += 1
            row_segs.append((start, i))
        else:
            i += 1
    col_bg = [all(grid[i][j] == bg for i in range(h)) for j in range(w)]
    col_segs = []
    j = 0
    while j < w:
        if not col_bg[j]:
            start = j
            while j < w and not col_bg[j]:
                j += 1
            col_segs.append((start, j))
        else:
            j += 1
    def rotate(shape):
        return tuple(tuple(shape[len(shape)-1-r][c] for r in range(len(shape))) for c in range(len(shape[0])))
    shape_classes = []
    instances = {}
    R, C = len(row_segs), len(col_segs)
    for ri in range(R):
        r0, r1 = row_segs[ri]
        for ci in range(C):
            c0, c1 = col_segs[ci]
            block = [grid[r0 + ii][c0:c1] for ii in range(r1 - r0)]
            pts = [(ii, jj) for ii in range(r1 - r0) for jj in range(c1 - c0) if block[ii][jj] != bg]
            if not pts:
                continue
            mi = min(ii for ii, jj in pts)
            Ma = max(ii for ii, jj in pts)
            mj = min(jj for ii, jj in pts)
            Mb = max(jj for ii, jj in pts)
            shape = tuple(tuple(block[ii][jj] for jj in range(mj, Mb + 1)) for ii in range(mi, Ma + 1))
            found = False
            for cid, canon in enumerate(shape_classes):
                tmp = canon
                for rot in range(4):
                    if tmp == shape:
                        instances[(ri, ci)] = (cid, rot, canon)
                        found = True
                        break
                    tmp = rotate(tmp)
                if found:
                    break
            if not found:
                shape_classes.append(shape)
                instances[(ri, ci)] = (len(shape_classes) - 1, 0, shape)
    out = [row[:] for row in grid]
    for ri in range(R):
        for ci in range(C):
            if (ri, ci) in instances:
                continue
            used_r = {instances[(ri, cj)][0] for cj in range(C) if (ri, cj) in instances}
            used_c = {instances[(ri2, ci)][0] for ri2 in range(R) if (ri2, ci) in instances}
            avail = set(range(len(shape_classes))) - used_r - used_c
            if len(avail) != 1:
                continue
            cid = avail.pop()
            canon = shape_classes[cid]
            r0, r1 = row_segs[ri]
            c0, c1 = col_segs[ci]
            bh, bw = r1 - r0, c1 - c0
            for rot in range(4):
                tmp = canon
                for _ in range(rot):
                    tmp = rotate(tmp)
                rh, rw = len(tmp), len(tmp[0])
                if rh <= bh and rw <= bw:
                    off_i = (bh - rh) // 2
                    off_j = (bw - rw) // 2
                    for ii in range(rh):
                        for jj in range(rw):
                            out[r0 + off_i + ii][c0 + off_j + jj] = tmp[ii][jj]
                    break
    return out