from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    header_row = next(r for r in range(H) if any(v == 1 for v in grid[r]))
    pr = next(r for r in range(header_row + 1, H) if any(v == 5 for v in grid[r]))
    pairs = []
    c = 0
    while c < W:
        if grid[pr][c] == 5:
            pairs.append((c, c + 1))
            c += 2
        else:
            c += 1
    pillars = []
    for pc, qc in pairs:
        pts = []
        for r in range(pr + 1, H):
            for c in (pc, qc):
                v = grid[r][c]
                if v not in (0, 5):
                    pts.append((r, v))
        pts.sort()
        if pts:
            seen = []
            for r, v in pts:
                if v not in seen:
                    seen.append(v)
                if len(seen) == 2:
                    break
            sel = []
            for v in seen:
                for r2, vv in pts:
                    if vv == v:
                        sel.append((r2, vv))
                        break
            pillars.append(sel)
    n = len(pairs)
    max_layer = 0
    layers = []
    for sel in pillars:
        ls = []
        for r, v in sel:
            layer = (r - pr - 1) // 3
            ls.append((layer, v))
            max_layer = max(max_layer, layer)
        layers.append(ls)
    slots = max_layer + 1
    out_h = slots * 3 - 1
    out_w = n * 3 - 1
    out = [[0] * out_w for _ in range(out_h)]
    for p, ls in enumerate(layers):
        for layer, v in ls:
            br = layer * 3
            bc = p * 3
            for dr in (0, 1):
                for dc in (0, 1):
                    out[br + dr][bc + dc] = v
    return out