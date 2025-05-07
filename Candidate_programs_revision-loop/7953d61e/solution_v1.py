from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    def transpose(m):
        return [[m[r][c] for r in range(len(m))] for c in range(len(m[0]))]
    def flipud(m):
        return m[::-1]
    def f(m):
        return flipud(transpose(m))
    mats = [grid]
    for _ in range(3):
        mats.append(f(mats[-1]))
    res = [[0]*(2*n) for _ in range(2*n)]
    for br in range(2):
        for bc in range(2):
            m = mats[br*2+bc]
            for i in range(n):
                for j in range(n):
                    res[br*n+i][bc*n+j] = m[i][j]
    return res