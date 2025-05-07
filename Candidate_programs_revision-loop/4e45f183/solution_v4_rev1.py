from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    br, bc = [], []
    for i in range(1, H):
        if all(grid[i-1][j] == 0 for j in range(W)) and any(grid[i][j] != 0 for j in range(W)):
            br.append(i)
    for j in range(1, W):
        if all(grid[i][j-1] == 0 for i in range(H)) and any(grid[i][j] != 0 for i in range(H)):
            bc.append(j)
    out = [row[:] for row in grid]
    if br:
        for t in range(br[0], H):
            if all(grid[t][j] == 0 for j in range(W)):
                B = t - br[0]
                break
        else:
            B = H - br[0]
    else:
        return out
    for bi, ri in enumerate(br):
        for bj, ci in enumerate(bc):
            cnt = {}
            for di in range(B):
                for dj in range(B):
                    v = grid[ri+di][ci+dj]
                    cnt[v] = cnt.get(v, 0) + 1
            mcol = min(cnt, key=cnt.get)
            Mcol = max(cnt, key=cnt.get)
            for di in range(B):
                for dj in range(B):
                    r, c = di, dj
                    if bi == 0 and bj == 0 and r + c < 2:
                        out[ri+di][ci+dj] = mcol
                    elif bi == 0 and bj == 1 and abs(c-2) > r:
                        out[ri+di][ci+dj] = mcol
                    elif bi == 0 and bj == 2 and r + (4-c) < 2:
                        out[ri+di][ci+dj] = mcol
                    elif bi == 1 and bj == 0 and abs(r-2) + abs(c-2) <= 2:
                        out[ri+di][ci+dj] = mcol
                    elif bi == 1 and bj == 1 and abs(r-2) + abs(c-2) <= 2:
                        out[ri+di][ci+dj] = mcol
                    elif bi == 1 and bj == 2 and abs(r-2) > (4-c):
                        out[ri+di][ci+dj] = mcol
                    elif bi == 2 and bj == 0 and (4-r) + (4-c) < 2:
                        out[ri+di][ci+dj] = mcol
                    elif bi == 2 and bj == 1 and abs(c-2) > (4-r):
                        out[ri+di][ci+dj] = mcol
                    elif bi == 2 and bj == 2 and (4-r) + c < 2:
                        out[ri+di][ci+dj] = mcol
                    else:
                        out[ri+di][ci+dj] = Mcol
    return out