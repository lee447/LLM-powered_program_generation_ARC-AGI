from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    B = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    anchors = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] not in (0, 1)]
    out = [row[:] for row in grid]
    for ar, ac, color in anchors:
        for br, bc in B:
            dr = ar - br
            dc = ac - bc
            if dr == 0 and dc == 0:
                continue
            valid = True
            for brp, bcp in B:
                rr, cc = brp + dr, bcp + dc
                if not (0 <= rr < h and 0 <= cc < w):
                    valid = False
                    break
                cell = grid[rr][cc]
                if (rr, cc) == (ar, ac):
                    if cell != color:
                        valid = False
                        break
                else:
                    if cell != 0:
                        valid = False
                        break
            if valid:
                for brp, bcp in B:
                    rr, cc = brp + dr, bcp + dc
                    if (rr, cc) != (ar, ac):
                        out[rr][cc] = color
                break
    return out