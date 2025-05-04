from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R=len(grid); C=len(grid[0])
    block_cols=set(c for r in range(R) for c in range(C) if grid[r][c]!=0)
    if not block_cols: return [row[:] for row in grid]
    minc=min(block_cols); maxc=max(block_cols)
    is_block=[any(grid[r][c]!=0 for c in range(C)) for r in range(R)]
    out=[[grid[r][c] for c in range(C)] for r in range(R)]
    for r in range(R):
        if is_block[r]:
            for c in range(minc,maxc+1):
                if grid[r][c]==0: out[r][c]=2
        else:
            above=any(is_block[i] for i in range(r))
            below=any(is_block[i] for i in range(r+1,R))
            if above and below:
                for c in range(C):
                    out[r][c]=2 if minc<=c<=maxc else 1
            else:
                for c in range(minc,maxc+1):
                    if c not in block_cols:
                        out[r][c]=1
    return out