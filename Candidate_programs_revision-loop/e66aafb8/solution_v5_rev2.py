import numpy as np
def solve(grid):
    G = np.array(grid)
    H,W = G.shape
    def find_block_height():
        for p in range(1, H//2+1):
            if (H - p) % 2: continue
            r0 = (H - p)//2
            top = G[:r0]
            bot = G[r0+p:]
            if np.array_equal(top, bot):
                return r0, p
        return 0, H
    def find_block_width(r0,p):
        sub = G[r0:r0+p]
        for q in range(1, W//2+1):
            if (W - q) % 2: continue
            c0 = (W - q)//2
            left = sub[:, :c0]
            right = sub[:, c0+q:]
            if np.array_equal(left, right):
                return c0, q
        return 0, W
    r0,p = find_block_height()
    c0,q = find_block_width(r0,p)
    return G[r0:r0+p, c0:c0+q].tolist()