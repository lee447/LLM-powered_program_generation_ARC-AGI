def solve(grid):
    h=len(grid); w=len(grid[0])
    fives=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==5]
    def has_color(r,c):
        for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0<=nr<h and 0<=nc<w and grid[nr][nc] not in (0,5):
                return True
        return False
    if has_color(*fives[0]):
        origin, target = fives[0], fives[1]
    else:
        origin, target = fives[1], fives[0]
    dr=target[0]-origin[0]; dc=target[1]-origin[1]
    out=[row[:] for row in grid]
    out[target[0]][target[1]]=0
    for r in range(h):
        for c in range(w):
            v=grid[r][c]
            if v not in (0,5):
                nr, nc = r+dr, c+dc
                if 0<=nr<h and 0<=nc<w:
                    out[nr][nc]=v
    return out