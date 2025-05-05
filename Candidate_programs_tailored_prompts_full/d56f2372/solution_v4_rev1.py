from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                col = grid[i][j]
                stack = [(i, j)]
                seen[i][j] = True
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and grid[nr][nc] == col:
                            seen[nr][nc] = True
                            stack.append((nr, nc))
                comps.append((col, cells))
    def vertical_sym(cells):
        rs = [r for r, c in cells]; cs = [c for r, c in cells]
        r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
        s = set(cells)
        for r, c in cells:
            mc = c0 + c1 - c
            if (r, mc) not in s:
                return False
        return True
    sym = [(col, cells) for col, cells in comps if vertical_sym(cells)]
    if len(sym) == 1:
        col, cells = sym[0]
    else:
        if sym:
            best = None; best_score = None
            for col, cells in sym:
                s = set(cells)
                score = 0
                for r, c in cells:
                    for dr, dc in ((1,1),(1,-1),(-1,1),(-1,-1)):
                        if (r+dr, c+dc) in s:
                            score += 1
                if best_score is None or score > best_score or (score == best_score and col > best[0]):
                    best = (col, cells); best_score = score
            col, cells = best
        else:
            best = None; best_score = None
            for col, cells in comps:
                s = sum(r+c for r, c in cells)/len(cells)
                if best_score is None or s < best_score:
                    best = (col, cells); best_score = s
            col, cells = best
    rs = [r for r, c in cells]; cs = [c for r, c in cells]
    r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
    out_h, out_w = r1-r0+1, c1-c0+1
    out = [[0]*out_w for _ in range(out_h)]
    for r, c in cells:
        out[r-r0][c-c0] = col
    return out