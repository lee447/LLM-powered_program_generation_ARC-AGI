from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0]) if H else 0
    ans = [row[:] for row in grid]
    anchors = []
    for i in range(H - 4):
        for j in range(W - 4):
            ok = True
            for di in range(5):
                if grid[i + di][j] != 3 or grid[i + di][j + 4] != 3:
                    ok = False
                    break
            if not ok:
                continue
            for dj in range(5):
                if grid[i][j + dj] != 3 or grid[i + 4][j + dj] != 3:
                    ok = False
                    break
            if not ok:
                continue
            for di in range(1, 4):
                for dj in range(1, 4):
                    if grid[i + di][j + dj] == 3:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                anchors.append((i, j))
    if anchors:
        anchors.sort(key=lambda x: x[0])
        for idx, (i, j) in enumerate(anchors):
            col = 8 if idx == len(anchors) - 1 else 1
            for di in range(1, 4):
                for dj in range(1, 4):
                    ans[i + di][j + dj] = col
    return ans