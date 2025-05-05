def solve(grid):
    h = len(grid)
    w = len(grid[0])
    greys = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    opens = []
    for r, c in greys:
        for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            rr, cc = r+dr, c+dc
            while 0 <= rr < h and 0 <= cc < w:
                if grid[rr][cc] == 0:
                    opens.append((rr, cc))
                    break
                if grid[rr][cc] in (2,4):
                    rr += dr
                    cc += dc
                    continue
                break
            if len(opens) == len(opens) and len(opens) < len(greys) and opens and opens[-1]:
                break
    if len(opens) != 2:
        return grid
    (r1, c1), (r2, c2) = opens
    dr = 1 if r2 > r1 else -1
    dc = 1 if c2 > c1 else -1
    for rr in range(r1, r2 + dr, dr):
        if grid[rr][c1] == 0:
            grid[rr][c1] = 4
    for cc in range(c1, c2 + dc, dc):
        if grid[r2][cc] == 0:
            grid[r2][cc] = 4
    rr0, rr1 = sorted((r1, r2))
    cc0, cc1 = sorted((c1, c2))
    for rr in range(rr0 + abs(dr), rr1, abs(dr)):
        for cc in range(cc0 + abs(dc), cc1, abs(dc)):
            if grid[rr][cc] == 0:
                grid[rr][cc] = 4
    return grid