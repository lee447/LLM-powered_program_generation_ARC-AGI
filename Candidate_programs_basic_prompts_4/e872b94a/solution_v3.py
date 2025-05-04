from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid);w=len(grid[0])
    m=min(h,w)
    d1=sum(1 for i in range(m) if grid[i][i]==5)
    d2=sum(1 for i in range(m) if grid[i][w-1-i]==5)
    n=max(d1,d2)
    return [[0] for _ in range(n)]