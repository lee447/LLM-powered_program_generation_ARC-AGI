def solve(grid):
    H=len(grid);W=len(grid[0])
    shapes=[]
    for r in range(H-3):
        for c in range(W-3):
            color=None
            ok=True
            for i in range(4):
                for j in range(4):
                    v=grid[r+i][c+j]
                    if 1<=i<=2 and 1<=j<=2:
                        if v!=0: ok=False
                    else:
                        if v==0:
                            ok=False
                        else:
                            if color is None: color=v
                            elif v!=color: ok=False
                if not ok: break
            if ok:
                shapes.append((r,c))
    if not shapes: return []
    rs=[r for r,c in shapes]; cs=[c for r,c in shapes]
    dx=max(cs)-min(cs); dy=max(rs)-min(rs)
    horizontal=dx>=dy
    shapes.sort(key=lambda x: x[1] if horizontal else x[0])
    chunks=[]
    for r,c in shapes:
        chunk=[row[c:c+4] for row in grid[r:r+4]]
        chunks.append(chunk)
    if horizontal:
        out=[]
        for i in range(4):
            row=[]
            for chunk in chunks:
                row+=chunk[i]
            out.append(row)
        return out
    else:
        out=[]
        for chunk in chunks:
            out+=chunk
        return out