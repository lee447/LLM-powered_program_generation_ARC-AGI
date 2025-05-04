def solve(grid):
    rows=len(grid)
    cols=len(grid[0])
    sep=None
    for j in range(cols):
        if any(grid[i][j]==5 for i in range(rows)):
            sep=j
            break
    lb=[row[:sep] for row in grid]
    rb=[row[sep+1:] for row in grid]
    def analyze(block):
        cnt={}
        for r in block:
            for v in r:
                cnt[v]=cnt.get(v,0)+1
        shape_colors=[c for c in cnt if c>1]
        if shape_colors:
            sc=shape_colors[0]
            return "shape",sc,cnt
        else:
            return "back",None,cnt
    a1,sc1,c1=analyze(lb)
    a2,sc2,c2=analyze(rb)
    if a1=="shape":
        shape_block=lb;shape_color=sc1;background_block=rb
    else:
        shape_block=rb;shape_color=sc2;background_block=lb
    bc_cnt={}
    for r in background_block:
        for v in r:
            bc_cnt[v]=bc_cnt.get(v,0)+1
    border_color=max(bc_cnt, key=lambda x:bc_cnt[x])
    h=len(shape_block);w=len(shape_block[0])
    mask=[[shape_block[i][j]==shape_color for j in range(w)] for i in range(h)]
    out=[[border_color]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if mask[i][j]:
                out[i][j]=shape_color
    return out