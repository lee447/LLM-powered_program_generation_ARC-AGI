from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    pts = [(i,j) for i in range(H) for j in range(W) if grid[i][j] != 0]
    cs = {grid[i][j] for i,j in pts}
    cs.discard(0)
    c = cs.pop()
    used = {grid[i][j] for i in range(H) for j in range(W)}
    newc = next(x for x in range(1,10) if x != c and x not in used)
    rows = [i for i,j in pts]; cols = [j for i,j in pts]
    rmin, rmax, cmin, cmax = min(rows), max(rows), min(cols), max(cols)
    h, w = rmax-rmin+1, cmax-cmin+1
    mask = [[1 if grid[rmin+i][cmin+j]==c else 0 for j in range(w)] for i in range(h)]
    cg_r, cg_c = (H-1)/2, (W-1)/2
    sc_r, sc_c = (rmin+rmax)/2, (cmin+cmax)/2
    vr, vc = sc_r-cg_r, sc_c-cg_c
    def rotate_vec(vr,vc):
        return -vc, vr
    def rotate_mask(m):
        mh, mw = len(m), len(m[0])
        return [[m[mh-1-j][i] for j in range(mw)] for i in range(mw)]
    res = [[0]*W for _ in range(H)]
    vrs = []
    vcs = []
    mks = []
    dims = []
    cur_vr, cur_vc = vr, vc
    cur_m = mask
    cur_h, cur_w = h, w
    for k in range(4):
        vrs.append(cur_vr); vcs.append(cur_vc)
        mks.append(cur_m); dims.append((len(cur_m), len(cur_m[0])))
        cur_vr, cur_vc = rotate_vec(cur_vr, cur_vc)
        cur_m = rotate_mask(cur_m)
    for k in range(4):
        vk_r, vk_c = vrs[k], vcs[k]
        mh, mw = dims[k]
        for sign in (1,-1):
            pr = cg_r + sign*vk_r
            pc = cg_c + sign*vk_c
            top = int(pr - (mh-1)/2)
            left= int(pc - (mw-1)/2)
            col = c if k%2==0 else newc
            mk = mks[k]
            for i in range(mh):
                for j in range(mw):
                    if mk[i][j]:
                        rr, cc = top+i, left+j
                        if 0 <= rr < H and 0 <= cc < W:
                            res[rr][cc] = col
    return res