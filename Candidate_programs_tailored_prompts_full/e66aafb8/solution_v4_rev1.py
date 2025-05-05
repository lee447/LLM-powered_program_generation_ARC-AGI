import numpy as np

def solve(grid):
    arr = np.array(grid)
    H, W = arr.shape
    zero = arr == 0
    rz = np.where(zero.any(axis=1))[0]
    cz = np.where(zero.any(axis=0))[0]
    r0, r1 = rz[0], rz[-1]
    c0, c1 = cz[0], cz[-1]
    top = r0
    bot = H - 1 - r1
    if top > bot:
        rows = list(range(bot, bot + top - bot))
    else:
        rows = list(range(r1 + 1, r1 + 1 + bot - top))
    stripe = [[grid[r][c] for c in range(c0, c1 + 1)] for r in rows]
    return stripe