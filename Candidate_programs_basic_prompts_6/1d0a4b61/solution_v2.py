from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    res = [row.copy() for row in grid]
    def find_h_period():
        for p in range(1, m):
            ok = True
            has = False
            for i in range(n):
                for j in range(m - p):
                    a, b = grid[i][j], grid[i][j+p]
                    if a != 0 and b != 0:
                        has = True
                        if a != b:
                            ok = False
                            break
                if not ok:
                    break
            if ok and has:
                return p
        return m
    def find_v_period():
        for p in range(1, n):
            ok = True
            has = False
            for i in range(n - p):
                for j in range(m):
                    a, b = grid[i][j], grid[i+p][j]
                    if a != 0 and b != 0:
                        has = True
                        if a != b:
                            ok = False
                            break
                if not ok:
                    break
            if ok and has:
                return p
        return n
    hp = find_h_period()
    for i in range(n):
        for j in range(m):
            if res[i][j] == 0:
                if j >= hp and res[i][j-hp] != 0:
                    res[i][j] = res[i][j-hp]
                elif j + hp < m and res[i][j+hp] != 0:
                    res[i][j] = res[i][j+hp]
    vp = find_v_period()
    for i in range(n):
        for j in range(m):
            if res[i][j] == 0:
                if i >= vp and res[i-vp][j] != 0:
                    res[i][j] = res[i-vp][j]
                elif i + vp < n and res[i+vp][j] != 0:
                    res[i][j] = res[i+vp][j]
    return res