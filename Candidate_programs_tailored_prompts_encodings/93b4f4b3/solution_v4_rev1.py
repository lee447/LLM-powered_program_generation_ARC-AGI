from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    left_w = 6
    anchor = grid[0][0]
    stripe_rows = [r for r in range(h) if all(grid[r][c] == anchor for c in range(left_w))]
    bands = []
    for i in range(len(stripe_rows) - 1):
        r0, r1 = stripe_rows[i], stripe_rows[i + 1]
        rows = list(range(r0 + 1, r1))
        vals = set()
        counts = []
        starts = []
        for r in rows:
            cnt = 0
            row_starts = []
            for c in range(left_w, w):
                v = grid[r][c]
                if v != anchor and v != 0:
                    vals.add(v)
                    cnt += 1
                    row_starts.append(c)
            counts.append(cnt)
            if row_starts:
                starts.append(min(row_starts))
        color = vals.pop() if vals else anchor
        start_x = sum(starts) / len(starts) if starts else 0
        diff_sum = sum(counts[i+1] - counts[i] for i in range(len(counts)-1)) if len(counts)>1 else 0
        bands.append({'rows': rows, 'color': color, 'counts': counts, 'diff': diff_sum, 'start': start_x})
    P = [b for b in bands if b['diff'] > 0]
    N = [b for b in bands if b['diff'] < 0]
    Z = [b for b in bands if b['diff'] == 0]
    if len(P) < len(N):
        first, second = N, P
    else:
        first, second = P, N
    def sort_group(g):
        if g and g[0]['diff'] < 0:
            return sorted(g, key=lambda b: b['start'], reverse=True)
        return g
    ordered = sort_group(first) + sort_group(second) + Z
    out = [[anchor]*left_w for _ in range(h)]
    for r in stripe_rows:
        out[r] = [anchor]*left_w
    for band_src, band_dst in zip(ordered, bands):
        rows, color, counts = band_dst['rows'], band_src['color'], band_src['counts']
        for j, r in enumerate(rows):
            cr = counts[j]
            off = (4 - cr) // 2
            for k in range(cr):
                out[r][1 + off + k] = color
    return out