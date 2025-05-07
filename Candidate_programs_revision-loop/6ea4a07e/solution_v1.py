from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m = {3:1,5:4,8:2}
    xs = {c for row in grid for c in row if c!=0}
    x = xs.pop() if xs else 0
    y = m.get(x,0)
    return [[0 if c==x else y for c in row] for row in grid]