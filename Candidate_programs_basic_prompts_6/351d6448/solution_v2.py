from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    groups = []
    curr = []
    for row in grid:
        if all(v == 5 for v in row):
            if curr:
                groups.append(curr)
                curr = []
        else:
            curr.append(row)
    if curr:
        groups.append(curr)
    starts, lengths, values = [], [], []
    for grp in groups:
        motif = None
        for r in grp:
            if any(v not in (0,5) for v in r):
                motif = r
                break
        if motif is None:
            continue
        idxs = [i for i,v in enumerate(motif) if v not in (0,5)]
        start = min(idxs)
        end = max(idxs)
        seq = motif[start:end+1]
        starts.append(start)
        lengths.append(end-start+1)
        values.append(seq)
    pred_start, pred_len, pred_vals = 0, 0, []
    if len(lengths) >= 2 and all(l == lengths[0] for l in lengths) and all(vs == values[0] for vs in values):
        step = starts[1] - starts[0]
        pred_start = starts[-1] + step
        pred_len = lengths[0]
        pred_vals = values[0]
    elif len(lengths) >= 2 and all(st == starts[0] for st in starts) and all(len(set(vs)) == 1 for vs in values):
        step_len = lengths[1] - lengths[0]
        pred_len = lengths[-1] + step_len
        pred_start = starts[0]
        color = values[0][0]
        pred_vals = [color] * pred_len
    else:
        return []
    out = [[0]*m for _ in range(3)]
    r = 1
    for i,v in enumerate(pred_vals):
        c = pred_start + i
        if 0 <= c < m:
            out[r][c] = v
    return out