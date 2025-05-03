def solve(grid):
    h=len(grid)
    w=len(grid[0])
    A=[[grid[h-1-r][w-1-c] for c in range(w)] for r in range(h)]
    H=2*h
    W=2*w
    out=[[0]*W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            rr=r if r<h else 2*h-1-r
            cc=c if c<w else 2*w-1-c
            out[r][c]=A[rr][cc]
    return out