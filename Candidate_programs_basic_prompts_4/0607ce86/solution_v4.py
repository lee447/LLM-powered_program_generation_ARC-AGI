from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    segments = []
    for r, row in enumerate(grid):
        c = 0
        while c < w:
            if row[c] != 0:
                start = c
                vals = []
                while c < w and row[c] != 0:
                    vals.append(row[c])
                    c += 1
                seg_len = c - start
                segments.append((r, start, seg_len, len(set(vals))))
            else:
                c += 1
    L_single = min(l for _, _, l, d in segments if d == 1 and l >= 2)
    L_multi = min(l for _, _, l, d in segments if d > 1 and l >= 2)
    cnt_single = {}
    for r, s, l, d in segments:
        if d == 1 and l >= L_single:
            cnt_single[r] = cnt_single.get(r, 0) + 1
    exemplar_single = max(cnt_single, key=lambda r: cnt_single[r])
    run_positions = sorted(s for r, s, l, d in segments if r == exemplar_single and d == 1 and l >= L_single)
    single_pattern = grid[exemplar_single][run_positions[0]:run_positions[0] + L_single]
    exemplar_multi = None
    for r in range(h):
        row_segs = [(s, l, d) for rr, s, l, d in segments if rr == r]
        for s, l, d in row_segs:
            if s <= run_positions[0] < s + l and d > 1 and l >= L_multi:
                exemplar_multi = r
                break
        if exemplar_multi is not None:
            break
    multi_pattern = grid[exemplar_multi][run_positions[0]:run_positions[0] + L_multi]
    out = []
    for r, row in enumerate(grid):
        nr = [0] * w
        if row[run_positions[0]] == single_pattern[0]:
            for s in run_positions:
                for i, v in enumerate(single_pattern):
                    nr[s + i] = v
        elif row[run_positions[0]] == multi_pattern[0]:
            for s in run_positions:
                for i, v in enumerate(multi_pattern):
                    nr[s + i] = v
        out.append(nr)
    return out