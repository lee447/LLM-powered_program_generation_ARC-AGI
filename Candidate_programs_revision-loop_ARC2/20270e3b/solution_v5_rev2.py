from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sep = None
    for c in range(w):
        v = grid[0][c]
        if v in (1,7) and all(grid[r][c] == v for r in range(h)):
            sep = c
            break
    def replace7(g):
        return [[4 if x==7 else x for x in row] for row in g]
    if sep is not None:
        L = replace7([row[:sep] for row in grid])
        R = replace7([row[sep+1:] for row in grid])
        lw, rw = len(L[0]), len(R[0])
        off = lw - rw
        for i in range(len(R)):
            for j in range(len(R[0])):
                if R[i][j] != 1:
                    L[i][off+j] = R[i][j]
        return L
    pure = {i for i,row in enumerate(grid) if row[0] in (1,7) and all(x==row[0] for x in row)}
    G = replace7([row for i,row in enumerate(grid) if i not in pure])
    if len(G)==h and len(G[0])==w:
        base = G[:h-2]
        block = [row[w-3:] for row in G][2:]
        return [base[i]+block[i] for i in range(h-2)]
    return G