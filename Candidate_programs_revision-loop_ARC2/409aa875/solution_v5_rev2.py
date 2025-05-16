from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = 7
    out = [row[:] for row in grid]
    vals = {grid[r][c] for r in range(h) for c in range(w) if grid[r][c] != bg}
    if 9 in vals and 0 not in vals and 2 not in vals:
        coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 9]
        rs = [r for r, _ in coords]; cs = [c for _, c in coords]
        r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
        out[(r0 + r1) // 2][(c0 + c1) // 2] = 1
        return out
    if 0 in vals and 9 not in vals and 2 not in vals:
        rows = sorted(r for r in range(h) if any(grid[r][c] == 0 for c in range(w)))
        shift = len(rows) - 1
        for i, r in enumerate(rows[:-1]):
            xs = sorted(c for c in range(w) if grid[r][c] == 0)
            cnt = len(xs) // 2 or 1
            sel = xs[:cnt] if i % 2 == 0 else xs[-cnt:]
            nr = r - shift
            for c in sel:
                out[nr][c] = 9
        return out
    if 2 in vals:
        rows = sorted(r for r in range(h) if any(grid[r][c] == 2 for c in range(w)))
        top0, top1 = rows[0], rows[1]
        xs0 = sorted(c for c in range(w) if grid[top0][c] == 2)
        groups = []
        g = [xs0[0]]
        for x in xs0[1:]:
            if x == g[-1] + 1:
                g.append(x)
            else:
                groups.append(g)
                g = [x]
        groups.append(g)
        g2 = groups[1]
        for c in g2:
            out[top0][c] = 9
        out[top1][g2[0]] = 9
        shift = len(rows) - 1
        new_rows = [rows[0] - shift, rows[-2] - shift]
        base = xs0[0]
        for nr in new_rows:
            if 0 <= nr < h:
                for c in xs0:
                    off = c - base
                    if off % 3 == 0 and 0 <= off < w:
                        out[nr][off] = 9
        return out
    return out