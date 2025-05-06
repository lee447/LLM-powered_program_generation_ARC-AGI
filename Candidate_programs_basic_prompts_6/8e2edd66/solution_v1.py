from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n=len(grid)
    vals={v for row in grid for v in row if v!=0}
    c=vals.pop() if vals else 0
    M=[[c if grid[i][j]==0 else 0 for j in range(n)] for i in range(n)]
    ans=[[0]*(n*n) for _ in range(n*n)]
    for br in range(n):
        for bc in range(n):
            block= M if grid[br][bc]==0 else [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    ans[br*n+i][bc*n+j]=block[i][j]
    return ans