from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    shape_color = next(cell for row in grid for cell in row if cell != 0)
    coords = [(r,c) for r, row in enumerate(grid) for c, v in enumerate(row) if v==shape_color]
    rs = [r for r,_ in coords]; cs = [c for _,c in coords]
    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)
    center_r = (min_r+max_r+1)//2
    center_c = (min_c+max_c+1)//2
    h_bbox = max_r-min_r+1
    w_bbox = max_c-min_c+1
    shape_dim = h_bbox if h_bbox>=w_bbox else w_bbox
    shift_mag = shape_dim if shape_dim%2==1 else shape_dim-1
    base_shift = (0, -shift_mag)
    rel = []
    for k in range(4):
        sr, sc = base_shift
        dr, dc = sr, sc
        for _ in range(k):
            dr, dc = -dc, dr
        for r,c in coords:
            dr0, dc0 = r-center_r, c-center_c
            drp, dcp = dr0, dc0
            for _ in range(k):
                drp, dcp = -dcp, drp
            rel.append((drp+dr, dcp+dc))
    min_rr = min(r for r,_ in rel)
    max_rr = max(r for r,_ in rel)
    min_cc = min(c for _,c in rel)
    max_cc = max(c for _,c in rel)
    H = max_rr-min_rr+1
    W = max_cc-min_cc+1
    out = [[0]*W for _ in range(H)]
    for r,c in rel:
        out[r-min_rr][c-min_cc] = shape_color
    return out