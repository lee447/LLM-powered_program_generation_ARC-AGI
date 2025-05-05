def solve(grid):
    H=len(grid);W=len(grid[0])
    black={}
    for r in range(H):
        for c in range(W):
            if grid[r][c]==0:
                black.setdefault(r,set()).add(c)
    best_len=0
    best_seq=[]
    for s in (1,-1):
        for r in black:
            for c in black[r]:
                seq=[]
                rr,cc=r,c
                while rr in black and cc in black[rr]:
                    seq.append((rr,cc))
                    rr+=1;cc+=s
                if len(seq)>best_len:
                    best_len=len(seq)
                    best_seq=seq
    out=[row[:] for row in grid]
    for r,c in best_seq:
        out[r][c]=8
    return out