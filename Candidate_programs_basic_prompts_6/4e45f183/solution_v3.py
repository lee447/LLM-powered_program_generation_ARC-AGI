def solve(grid):
    n=len(grid)
    zero_rows=[i for i in range(n) if all(c==0 for c in grid[i])]
    zero_cols=[j for j in range(n) if all(grid[i][j]==0 for i in range(n))]
    row_bounds=[]
    prev=-1
    for r in zero_rows:
        if prev+1<r:
            row_bounds.append((prev+1,r))
        prev=r
    prev= -1
    col_bounds=[]
    for c in zero_cols:
        if prev+1<c:
            col_bounds.append((prev+1,c))
        prev=c
    R=len(row_bounds); C=len(col_bounds)
    def block(r,c):
        rs, re = row_bounds[r]; cs, ce = col_bounds[c]
        return [row[cs:ce] for row in grid[rs:re]]
    def rot(b):
        m=len(b)
        return [[b[m-1-j][i] for j in range(m)] for i in range(m)]
    blocks=[[block(r,c) for c in range(C)] for r in range(R)]
    rc=(R//2, C//2)
    target=blocks[rc[0]][rc[1]]
    best_rot=[[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            b=blocks[r][c]
            best_k=0; best_m=-1
            cur=b
            for k in range(4):
                match=sum(cur[i][j]==target[i][j] for i in range(len(cur)) for j in range(len(cur)))
                if match>best_m:
                    best_m=match; best_k=k
                cur=rot(cur)
            best_rot[r][c]=best_k
    out=[[0]*n for _ in range(n)]
    for r in range(R):
        for c in range(C):
            b=blocks[r][c]
            for _ in range(best_rot[r][c]):
                b=rot(b)
            rs, re = row_bounds[r]; cs, ce = col_bounds[c]
            for i in range(re-rs):
                for j in range(ce-cs):
                    out[rs+i][cs+j]=b[i][j]
    return out