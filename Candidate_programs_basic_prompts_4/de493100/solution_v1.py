def solve(grid):
    def horiz_sym_between(g):
        H=len(g)
        if H%2!=0: return False
        for r in range(H//2):
            if g[r]!=g[H-1-r]: return False
        return True
    def horiz_sym_on(g):
        H=len(g)
        if H%2!=1: return False
        m=H//2
        for d in range(1,m+1):
            if g[m-d]!=g[m+d]: return False
        return True
    def vert_sym_between(g):
        H=len(g); W=len(g[0])
        if W%2!=0: return False
        for r in range(H):
            for c in range(W//2):
                if g[r][c]!=g[r][W-1-c]: return False
        return True
    def vert_sym_on(g):
        H=len(g); W=len(g[0])
        if W%2!=1: return False
        m=W//2
        for r in range(H):
            for d in range(1,m+1):
                if g[r][m-d]!=g[r][m+d]: return False
        return True

    g = [row[:] for row in grid]
    while True:
        H,W = len(g), len(g[0])
        did = False
        if H>1 and horiz_sym_between(g):
            g = g[:H//2]
            did = True
        elif H>1 and horiz_sym_on(g):
            g = g[:H//2+1]
            did = True
        if did: continue
        if W>1 and vert_sym_between(g):
            g = [row[:W//2] for row in g]
            did = True
        elif W>1 and vert_sym_on(g):
            g = [row[:W//2+1] for row in g]
            did = True
        if not did:
            return g