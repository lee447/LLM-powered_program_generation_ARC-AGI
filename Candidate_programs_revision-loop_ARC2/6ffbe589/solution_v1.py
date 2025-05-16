from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    th_num, th_den = 2, 5
    for size in range(min(n, m), 0, -1):
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                cnt = 0
                for x in range(i, i + size):
                    for y in range(j, j + size):
                        if grid[x][y] != 0:
                            cnt += 1
                if cnt * th_den >= th_num * size * size:
                    return [row[j:j + size] for row in grid[i:i + size]]
    return []