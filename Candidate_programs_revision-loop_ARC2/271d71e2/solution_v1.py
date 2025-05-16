def solve(grid):
    h=len(grid); w=len(grid[0])
    from collections import Counter,deque
    flat=[c for row in grid for c in row]
    border_color=Counter(flat).most_common(1)[0][0]
    is_border_row=[sum(1 for x in row if x==border_color)>w/2 for row in grid]
    is_border_col=[sum(1 for i in range(h) if grid[i][j]==border_color)>h/2 for j in range(w)]
    rows=[]; i=0
    while i<h:
        if not is_border_row[i]:
            j=i
            while j<h and not is_border_row[j]: j+=1
            rows.append((i,j)); i=j
        else: i+=1
    cols=[]; j=0
    while j<w:
        if not is_border_col[j]:
            k=j
            while k<w and not is_border_col[k]: k+=1
            cols.append((j,k)); j=k
        else: j+=1
    if len(rows)==1: rows=[(0,h//2),(h//2+ (h%2),h)]
    if len(cols)==1: cols=[(0,w//2),(w//2+ (w%2),w)]
    RR=len(rows); CC=len(cols)
    background=[[None]*CC for _ in range(RR)]
    shapes=[[None]*CC for _ in range(RR)]
    for ri,(r0,r1) in enumerate(rows):
        for cj,(c0,c1) in enumerate(cols):
            cnt=Counter()
            for i in range(r0,r1):
                for j in range(c0,c1):
                    cnt[grid[i][j]]+=1
            bg=cnt.most_common(1)[0][0]
            background[ri][cj]=bg
            pts=[(i-r0,j-c0,grid[i][j]) for i in range(r0,r1) for j in range(c0,c1) if grid[i][j]!=bg]
            shapes[ri][cj]=pts
    mapping = {(0,0):(1,0),(1,0):(1,1),(1,1):(0,1),(0,1):(0,0)}
    out=[row[:] for row in grid]
    for ri in range(RR):
        for cj in range(CC):
            r0,r1=rows[ri]; c0,c1=cols[cj]
            for i in range(r0,r1):
                for j in range(c0,c1):
                    if out[i][j]!=border_color: out[i][j]=background[ri][cj]
    for dri,dci in mapping.items():
        di,dj=dri; si,sj=dci
        for dr,dc,col in shapes[si][sj]:
            i=rows[di][0]+dr; j=cols[dj][0]+dc
            if 0<=i<h and 0<=j<w and out[i][j]!=border_color:
                out[i][j]=col
    return out