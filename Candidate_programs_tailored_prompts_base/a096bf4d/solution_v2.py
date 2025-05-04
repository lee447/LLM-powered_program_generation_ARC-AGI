from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    sep_rows = [i for i,row in enumerate(grid) if all(c==0 for c in row)]
    sep_cols = [j for j in range(len(grid[0])) if all(grid[i][j]==0 for i in range(len(grid)))]
    row_segments = [(sep_rows[i]+1, sep_rows[i+1]-1) for i in range(len(sep_rows)-1) if sep_rows[i]+1<=sep_rows[i+1]-1]
    col_segments = [(sep_cols[i]+1, sep_cols[i+1]-1) for i in range(len(sep_cols)-1) if sep_cols[i]+1<=sep_cols[i+1]-1]
    out = [row.copy() for row in grid]
    dr_offsets = []
    dc_offsets = []
    for r_start, r_end in row_segments:
        bh = r_end - r_start + 1
        r_mid_lo = r_start + bh//2 - 1
        r_mid_hi = r_start + bh//2
        found = False
        for c_start, c_end in col_segments:
            bw = c_end - c_start + 1
            c_mid_lo = c_start + bw//2 - 1
            c_mid_hi = c_start + bw//2
            cluster = [(r_mid_lo, c_mid_lo), (r_mid_lo, c_mid_hi), (r_mid_hi, c_mid_lo), (r_mid_hi, c_mid_hi)]
            vals = [grid[r][c] for r,c in cluster]
            cnt = {}
            for v in vals:
                cnt[v] = cnt.get(v,0) + 1
            if len(cnt) > 1:
                for (r,c),v in zip(cluster, vals):
                    if cnt[v] == 1:
                        dr_offsets.append(r - r_start)
                        dc_offsets.append(c - c_start)
                        found = True
                        break
            if found:
                break
        if not found:
            dr_offsets.append(bh//2 - 1)
            dc_offsets.append(bw//2 - 1)
    for bi, (r_start, r_end) in enumerate(row_segments):
        dr = dr_offsets[bi]
        dc = dc_offsets[bi]
        vals = []
        for c_start, c_end in col_segments:
            vals.append(grid[r_start+dr][c_start+dc])
        cnt = {}
        for v in vals:
            cnt[v] = cnt.get(v,0) + 1
        mode = max(cnt.keys(), key=lambda k: (cnt[k], -k))
        for c_start, c_end in col_segments:
            out[r_start+dr][c_start+dc] = mode
    return out