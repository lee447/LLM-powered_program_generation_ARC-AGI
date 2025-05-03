def solve(grid):
    h,len_row= len(grid),len(grid[0])
    row_has = [any(cell!=0 for cell in row) for row in grid]
    blocks_r=[]
    for i,v in enumerate(row_has):
        if v and (not blocks_r or i!=blocks_r[-1][1]+1):
            blocks_r.append([i,i])
        elif v:
            blocks_r[-1][1]=i
    sep_rows={i for i,v in enumerate(row_has) if not v}
    inner_rows=set()
    for a,b in blocks_r:
        pass
    for i in range(len(blocks_r)-1):
        for r in range(blocks_r[i][1]+1,blocks_r[i+1][0]):
            inner_rows.add(r)
    outer_rows=sep_rows-inner_rows
    col_has=[any(grid[r][c]!=0 for r in range(h)) for c in range(len_row)]
    blocks_c=[]
    for i,v in enumerate(col_has):
        if v and (not blocks_c or i!=blocks_c[-1][1]+1):
            blocks_c.append([i,i])
        elif v:
            blocks_c[-1][1]=i
    sep_cols={i for i,v in enumerate(col_has) if not v}
    inner_cols=set()
    for i in range(len(blocks_c)-1):
        for c in range(blocks_c[i][1]+1,blocks_c[i+1][0]):
            inner_cols.add(c)
    outer_cols=sep_cols-inner_cols
    all_block_rows={r for a,b in blocks_r for r in range(a,b+1)}
    all_block_cols={c for a,b in blocks_c for c in range(a,b+1)}
    min_c,min_r=min(all_block_cols),min(all_block_rows)
    max_c,max_r=max(all_block_cols),max(all_block_rows)
    out=[row[:] for row in grid]
    for r in inner_rows:
        for c in range(min_c,max_c+1):
            out[r][c]=2
    for c in inner_cols:
        for r in all_block_rows:
            out[r][c]=2
    for r in outer_rows:
        for c in inner_cols:
            out[r][c]=1
    for c in outer_cols:
        for r in inner_rows:
            out[r][c]=1
    return out