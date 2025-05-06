from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    ans = [row[:] for row in grid]
    used = set()
    for j in range(w):
        rs = [i for i in range(h) if grid[i][j] == 4]
        if len(rs) == 2:
            r1, r2 = rs[0], rs[1]
            seg = [grid[i][j] for i in range(r1+1, r2)]
            if all(v in (0,6) for v in seg):
                for i in range(r1+1, r2):
                    ans[i][j] = 8 if grid[i][j] == 0 else 7
                used.add((r1, j)); used.add((r2, j))
    for i in range(h):
        cs = [j for j in range(w) if grid[i][j] == 4 and (i,j) not in used]
        if len(cs) == 2:
            c1, c2 = cs[0], cs[1]
            seg = [grid[i][j] for j in range(c1+1, c2)]
            if seg and all(v in (0,6) for v in seg):
                for j in range(c1+1, c2):
                    ans[i][j] = 8 if grid[i][j] == 0 else 7
            elif seg and all(v in (7,8) for v in seg):
                for j in range(c1+1, c2):
                    ans[i][j] = 6 if grid[i][j] == 7 else 0
    return ans