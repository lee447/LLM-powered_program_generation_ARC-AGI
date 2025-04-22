def solve(grid):
    H=len(grid);W=len(grid[0])
    bands=(H-1)//6
    starts=[1,7,13]
    motifs=[
        [(0,1),(1,0),(1,1),(1,2)],   # T shape
        [(1,1,)],                   # center dot
        [(0,1),(1,0),(1,1),(1,2),(2,1)]  # cross
    ]
    out=[row[:] for row in grid]
    for b in range(bands):
        r0=1+b*6
        for j,c0 in enumerate(starts):
            color=None
            # find border color
            for dc in range(5):
                v=grid[r0][c0+dc]
                if v!=0:
                    color=v;break
            if color is None:continue
            for dr,dc in motifs[j]:
                r=r0+1+dr; c=c0+1+dc
                out[r][c]=color
    return out
def solve(grid):
    H=len(grid);W=len(grid[0])
    bands=(H-1)//6
    starts=[1,7,13]
    motifs=[
        [(0,1),(1,0),(1,1),(1,2)],   
        [(1,1,)],                   
        [(0,1),(1,0),(1,1),(1,2),(2,1)]  
    ]
    out=[row[:] for row in grid]
    for b in range(bands):
        r0=1+b*6
        for j,c0 in enumerate(starts):
            # detect border
            col=None
            for x in range(5):
                v=grid[r0][c0+x]
                if v!=0:
                    col=v;break
            if col is None:continue
            for cell in motifs[j]:
                if len(cell)==2:
                    dr,dc=cell
                    out[r0+1+dr][c0+1+dc]=col
                else:
                    dr=cell[0]; dc=cell[0]
                    out[r0+1+dr][c0+1+dc]=col
    return out