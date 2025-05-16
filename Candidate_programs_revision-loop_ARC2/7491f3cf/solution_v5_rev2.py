from collections import Counter
def solve(grid):
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    cols = [j for j in range(w) if all(grid[i][j]==border for i in range(h))]
    blocks = [(cols[i]+1, cols[i+1]) for i in range(len(cols)-1) if cols[i+1]-cols[i]>1]
    rseps = [i for i in range(h) if all(grid[i][j]==border for j in range(w))]
    r0, r1 = rseps[0]+1, rseps[1]
    inner = [(i,j) for i in range(r0,r1) for j in range(w) if grid[i][j]!=border]
    cnt = Counter(grid[i][j] for i,j in inner)
    bg, _ = cnt.most_common(1)[0]
    hole = None; hole_b = None; diag = None
    for b, (c0, c1) in enumerate(blocks):
        cntb = Counter(grid[i][j] for i in range(r0,r1) for j in range(c0,c1) if grid[i][j]!=border and grid[i][j]!=bg)
        for col, num in cntb.items():
            if num>= (r1-r0):
                pts = [(i-r0, j-c0) for i in range(r0,r1) for j in range(c0,c1) if grid[i][j]==col]
                if all((d,d) in pts for d in range(r1-r0)):
                    hole, hole_b, diag = col, b, 'main'; break
                if all((d,(c1-c0-1)-d) in pts for d in range(r1-r0)):
                    hole, hole_b, diag = col, b, 'anti'; break
        if hole is not None:
            break
    for b in range(hole_b+1, len(blocks)):
        c0, c1 = blocks[b]
        n = r1-r0
        for d in range(n):
            i = r0 + d
            j = c0 + (d if diag=='main' else (n-1-d))
            if grid[i][j]==hole:
                grid[i][j] = bg
    return grid