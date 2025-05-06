def solve(grid):
    h, w = len(grid), len(grid[0])
    def rot(m):
        return [ [m[len(m)-1-j][i] for j in range(len(m))] for i in range(len(m[0])) ]
    mats = []
    cols = set(c for row in grid for c in row if c != 0)
    for c in cols:
        base = [[c, c, c], [c, 0, c], [c, c, c]]
        for i in range(h-2):
            for j in range(w-2):
                blk = [grid[i+x][j:j+3] for x in range(3)]
                m = base
                for k in range(4):
                    if blk == m:
                        mats.append((i, j, c))
                        break
                    m = rot(m)
    mats.sort()
    out = [[0,0,0] for _ in range(3)]
    for idx,(_, __, c) in enumerate(mats[:3]):
        out[idx] = [c,c,c]
    return out