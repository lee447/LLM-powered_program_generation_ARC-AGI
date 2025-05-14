from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    top, bottom, left, right = None, None, None, None
    
    for i in range(n):
        if 7 in grid[i]:
            if top is None:
                top = i
            bottom = i
    
    for j in range(m):
        for i in range(n):
            if grid[i][j] == 7:
                if left is None:
                    left = j
                right = j
                break
    
    if top is not None and bottom is not None and left is not None and right is not None:
        return [row[left:right+1] for row in grid[top:bottom+1]]
    
    return []