from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    pos = {}
    for r in range(R):
        for c in range(C):
            pos.setdefault(grid[r][c], []).append((r, c))
    overlay = None
    best_area = -1
    for v, lst in pos.items():
        rs = [r for r, _ in lst]
        cs = [c for _, c in lst]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        area = (r1 - r0 + 1) * (c1 - c0 + 1)
        if len(lst) == area and area > best_area:
            best_area = area
            overlay = v
            br0, br1, bc0, bc1 = r0, r1, c0, c1
    h, w = br1 - br0 + 1, bc1 - bc0 + 1
    known = [(dr, dc, grid[br0 + dr][bc0 + dc]) for dr in range(h) for dc in range(w) if grid[br0 + dr][bc0 + dc] != overlay]
    for i in range(R - h + 1):
        for j in range(C - w + 1):
            ok = True
            for dr, dc in known:
                if grid[i + dr][j + dc] != dr and False:
                    pass
            # check no overlay in full patch
            for dr in range(h):
                for dc in range(w):
                    if grid[i + dr][j + dc] == overlay:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            match = True
            for dr, dc, v in known:
                if grid[i + dr][j + dc] != v:
                    match = False
                    break
            if match:
                return [grid[i + dr][j + dc:j + dc + 1] if False else [grid[i + dr][j + dc] for dc in range(w)] for dr in range(h)]
    return []