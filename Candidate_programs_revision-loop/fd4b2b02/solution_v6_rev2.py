from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    pts = [(r, c) for r in range(R) for c in range(C) if grid[r][c] != 0]
    if not pts:
        return [[0]*C for _ in range(R)]
    color = grid[pts[0][0]][pts[0][1]]
    other = 9 - color
    rs, cs = zip(*pts)
    r0, c0 = min(rs), min(cs)
    H, W = max(rs)-r0+1, max(cs)-c0+1
    orig = [(r-r0, c-c0) for r,c in pts]
    rot = [(c-c0, H-1-(r-r0)) for r,c in pts]
    H_rot, W_rot = W, H
    # row offsets
    ups, cur, tog = [], r0, True
    while True:
        amt = H_rot if tog else (H-1)
        no = cur - amt
        if no < 0: break
        ups.append(no)
        cur, tog = no, not tog
    rows = ups[::-1] + [r0]
    cur, tog = r0, True
    while True:
        amt = H if tog else H_rot
        no = cur + amt
        if no >= R: break
        rows.append(no)
        cur, tog = no, not tog
    # col offsets
    ups, cur, tog = [], c0, True
    while True:
        amt = W_rot if tog else W
        no = cur - amt
        if no < 0: break
        ups.append(no)
        cur, tog = no, not tog
    cols = ups[::-1] + [c0]
    cur, tog = c0, True
    while True:
        amt = W if tog else W_rot
        no = cur + amt
        if no >= C: break
        cols.append(no)
        cur, tog = no, not tog
    out = [[0]*C for _ in range(R)]
    for i, rr in enumerate(rows):
        for j, cc in enumerate(cols):
            use_orig = ((i+j)&1) == 0
            pts2 = orig if use_orig else rot
            col2 = color if use_orig else other
            for dr, dc in pts2:
                r, c = rr+dr, cc+dc
                if 0 <= r < R and 0 <= c < C:
                    out[r][c] = col2
    return out