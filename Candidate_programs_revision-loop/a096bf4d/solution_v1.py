from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0])
    sepRows=[i for i in range(h) if all(v==0 for v in grid[i])]
    sepCols=[j for j in range(w) if all(grid[i][j]==0 for i in range(h))]
    isSepRow=[i in sepRows for i in range(h)]
    isSepCol=[j in sepCols for j in range(w)]
    blockRowStarts=[i for i in range(h) if not isSepRow[i] and (i==0 or isSepRow[i-1])]
    blockColStarts=[j for j in range(w) if not isSepCol[j] and (j==0 or isSepCol[j-1])]
    if len(blockRowStarts)>1:
        bs=blockRowStarts[1]-blockRowStarts[0]-1
    else:
        first_sep=sepRows[0] if sepRows else h
        bs=first_sep-0-1
    interior=list(range(1,bs-1))
    for sr in blockRowStarts:
        best=None
        for dr in interior:
            for dc in interior:
                vals=[grid[sr+dr][sc+dc] for sc in blockColStarts]
                ref=vals[0]
                cnt=sum(1 for v in vals if v!=ref)
                if cnt>0 and (best is None or cnt>best[0]):
                    best=(cnt,dr,dc,ref)
        if best:
            _,dr,dc,ref=best
            for sc in blockColStarts:
                i,j=sr+dr,sc+dc
                if grid[i][j]!=ref:
                    grid[i][j]=ref
    return grid