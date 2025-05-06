from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    barrier = next(i for i,row in enumerate(grid) if all(x==5 for x in row))
    above = grid[:barrier]
    below = grid[barrier+1:]
    cntA = {2:0,4:0}
    cntB = {2:0,4:0}
    for row in above:
        for x in row:
            if x in cntA: cntA[x]+=1
    for row in below:
        for x in row:
            if x in cntB: cntB[x]+=1
    best, best_diff = None, None
    for k in (2,4):
        diff = cntB[k] - cntA[k]
        if best is None or diff > best_diff:
            best, best_diff = k, diff
    return [[best, best], [best, best]]