def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def flood(r0,c0,color,visited):
        stack=[(r0,c0)]
        comp=[]
        visited.add((r0,c0))
        while stack:
            r,c=stack.pop()
            comp.append((r,c))
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if 0<=nr<H and 0<=nc<W and (nr,nc) not in visited and grid[nr][nc]==color:
                    visited.add((nr,nc)); stack.append((nr,nc))
        return comp
    comps={4:[],6:[]}
    for color in (4,6):
        visited=set()
        for i in range(H):
            for j in range(W):
                if grid[i][j]==color and (i,j) not in visited:
                    c=flood(i,j,color,visited)
                    comps[color].append(c)
    size_count={4:{},6:{}}
    for color in (4,6):
        for c in comps[color]:
            size_count[color][len(c)]=size_count[color].get(len(c),0)+1
    shape_size=None;anchor_color=None
    for s in set(size_count[4])|set(size_count[6]):
        c4=size_count[4].get(s,0); c6=size_count[6].get(s,0)
        if c4==1 and c6>1:
            shape_size=s;anchor_color=4;break
        if c6==1 and c4>1:
            shape_size=s;anchor_color=6;break
    other_color = 6 if anchor_color==4 else 4
    anchor = [c for c in comps[anchor_color] if len(c)==shape_size][0]
    minr=min(r for r,c in anchor); minc=min(c for r,c in anchor)
    ars=[(r-minr,c-minc) for r,c in anchor]
    transforms=[
        lambda r,c:( r, c), lambda r,c:( r,-c),
        lambda r,c:(-r, c), lambda r,c:(-r,-c),
        lambda r,c:( c, r), lambda r,c:( c,-r),
        lambda r,c:(-c, r), lambda r,c:(-c,-r)
    ]
    norm_shapes=[]
    for f in transforms:
        tpts=[f(r,c) for r,c in ars]
        mr=min(r for r,c in tpts); mc=min(c for r,c in tpts)
        norm_shapes.append(frozenset((r-mr,c-mc) for r,c in tpts))
    new_grid=[row[:] for row in grid]
    for comp in comps[other_color]:
        if len(comp)==shape_size:
            mr=min(r for r,c in comp); mc=min(c for r,c in comp)
            offs=frozenset((r-mr,c-mc) for r,c in comp)
            if offs in norm_shapes:
                for r,c in comp:
                    new_grid[r][c]=anchor_color
    return new_grid