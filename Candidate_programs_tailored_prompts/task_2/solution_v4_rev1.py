def solve(grid):
    h, w = len(grid), len(grid[0])
    ac = {8}
    coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] in ac]
    if not coords:
        return grid
    rs, cs = zip(*coords)
    top, bottom, left, right = min(rs), max(rs), min(cs), max(cs)
    H, W = bottom - top + 1, right - left + 1
    sides = {}
    if left > 0:
        nbr = [grid[r][left - 1] for r in range(top, bottom + 1)]
        sides['left'] = len(set(nbr) - ac)
    else:
        sides['left'] = -1
    if right < w - 1:
        nbr = [grid[r][right + 1] for r in range(top, bottom + 1)]
        sides['right'] = len(set(nbr) - ac)
    else:
        sides['right'] = -1
    if top > 0:
        nbr = [grid[top - 1][c] for c in range(left, right + 1)]
        sides['top'] = len(set(nbr) - ac)
    else:
        sides['top'] = -1
    if bottom < h - 1:
        nbr = [grid[bottom + 1][c] for c in range(left, right + 1)]
        sides['bottom'] = len(set(nbr) - ac)
    else:
        sides['bottom'] = -1
    cluster_side = max(sides, key=sides.get)
    opp = {'left':'right','right':'left','top':'bottom','bottom':'top'}[cluster_side]
    if opp == 'left':
        c0 = left - W
        return [[grid[r][c0 + j] for j in range(W)] for r in range(top, bottom + 1)]
    if opp == 'right':
        c0 = right + 1
        return [[grid[r][c0 + j] for j in range(W)] for r in range(top, bottom + 1)]
    if opp == 'top':
        r0 = top - H
        return [[grid[r0 + i][c] for c in range(left, right + 1)] for i in range(H)]
    if opp == 'bottom':
        r0 = bottom + 1
        return [[grid[r0 + i][c] for c in range(left, right + 1)] for i in range(H)]
    return grid