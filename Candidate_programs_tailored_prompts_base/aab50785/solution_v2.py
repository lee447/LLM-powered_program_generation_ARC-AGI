from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    anchors = []
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j] == grid[i][j+1] == grid[i+1][j] == grid[i+1][j+1] == 8:
                anchors.append((i, j))
    anchors.sort()
    dirs = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    corners = [(0, 0), (0, 1), (1, 1), (1, 0)]
    result = []
    for ai, aj in anchors:
        row = []
        for (ci, cj), (di, dj) in zip(corners, dirs):
            r0, c0 = ai+ci, aj+cj
            val = 0
            k = 1
            while True:
                r, c = r0 + di*k, c0 + dj*k
                if r<0 or r>=h or c<0 or c>=w:
                    break
                if grid[r][c] != 0:
                    val = grid[r][c]
                    break
                k += 1
            row.append(val)
        result.append(row)
    return result