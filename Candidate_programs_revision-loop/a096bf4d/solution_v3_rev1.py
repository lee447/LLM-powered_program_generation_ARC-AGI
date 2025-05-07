from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0])
    sepRows=[i for i in range(h) if all(v==0 for v in grid[i])]
    sepCols=[j for j in range(w) if all(grid[i][j]==0 for i in range(h))]
    isSepRow=[i in sepRows for i in range(h)]
    isSepCol=[j in sepCols for j in range(w)]
    blockRowStarts=[i for i in range(h) if not isSepRow[i] and (i==0 or isSepRow[i-1])]
    blockColStarts=[j for j in range(w) if not isSepCol[j] and (j==0 or isSepCol[j-1])]
    used={v for row in grid for v in row}
    bc=blockColStarts[0]
    border=grid[blockRowStarts[0]][bc]
    if border==1: newc=4
    elif border==2: newc=6
    elif border==8: newc=7
    else:
        newc=next(c for c in range(10) if c not in used)
    sc=blockColStarts[1] if len(blockColStarts)>1 else blockColStarts[0]
    for sr in blockRowStarts:
        vals=[grid[sr+dr][sc+dc] for dr,dc in ((1,1),(1,2),(2,1),(2,2))]
        if len(set(vals))==1: continue
        from collections import Counter
        cnt=Counter(vals)
        if cnt[grid[sr+1][sc+1]]==1: dr,dc=1,2
        else: dr,dc=1,1
        grid[sr+dr][sc+dc]=newc
    return grid