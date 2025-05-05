from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    zeros = [all(grid[r][c] == 0 for c in range(w)) for r in range(h)]
    bands = []
    start = None
    for r in range(h):
        if not zeros[r] and start is None:
            start = r
        if zeros[r] and start is not None:
            bands.append((start, r - 1))
            start = None
    if start is not None:
        bands.append((start, h - 1))
    out = [row[:] for row in grid]
    colors = [8, 8, 3]
    for i, (r0, r1) in enumerate(bands):
        pts = [(r, c) for r in range(r0, r1 + 1) for c in range(w) if grid[r][c] == 2]
        cols = sorted({c for _, c in pts})
        # split left vs right by largest gap
        j, mx = 0, -1
        for k in range(len(cols) - 1):
            gap = cols[k+1] - cols[k]
            if gap > mx:
                mx = gap
                j = k
        left_set = set(cols[:j+1])
        right_set = set(cols[j+1:])
        left_pts = [(r, c) for r, c in pts if c in left_set]
        right_pts = [(r, c) for r, c in pts if c in right_set]
        # classify shape fullness
        def is_filled(pts):
            cs = [c for _, c in pts]
            rs = [r for r, _ in pts]
            if not cs: return False
            bb_w = max(cs) - min(cs) + 1
            bb_h = max(rs) - min(rs) + 1
            return len(pts) == bb_w * bb_h
        lf = is_filled(left_pts)
        rf = is_filled(right_pts)
        if lf and rf:
            lc = colors[(i+2) % len(colors)]
            rc = colors[i % len(colors)]
            for r, c in left_pts:
                out[r][c] = lc
            for r, c in right_pts:
                out[r][c] = rc
        else:
            # single‐side logic: choose perfect‐hollow first, else larger gap side
            def hollow(pts):
                if not pts: return False
                cs = [c for _, c in pts]
                rs = [r for r, _ in pts]
                bb_w = max(cs) - min(cs) + 1
                bb_h = max(rs) - min(rs) + 1
                interior = (bb_w-2)*(bb_h-2) if bb_w>2 and bb_h>2 else 0
                holes = 0
                for r, c in pts:
                    if (min(rs)<r<max(rs)) and (min(cs)<c<max(cs)) and grid[r][c]==0:
                        holes += 1
                return holes == interior and interior>0
            if hollow(left_pts) or hollow(right_pts):
                # if one is perfect hollow, color that
                if hollow(left_pts) and not hollow(right_pts):
                    target = left_pts
                elif hollow(right_pts) and not hollow(left_pts):
                    target = right_pts
                else:
                    # both perfect: alternate by band index
                    target = right_pts if i % 2 == 0 else left_pts
                nc = colors[i] if i < len(colors) else colors[-1]
                for r, c in target:
                    out[r][c] = nc
            else:
                # fallback: alternate by band index
                target = right_pts if i % 2 == 0 else left_pts
                nc = colors[i] if i < len(colors) else colors[-1]
                for r, c in target:
                    out[r][c] = nc
    return out