from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_largest_square(grid):
        n, m = len(grid), len(grid[0])
        max_size = 0
        top_left = (0, 0)
        dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    if dp[i][j] > max_size:
                        max_size = dp[i][j]
                        top_left = (i - max_size + 1, j - max_size + 1)
        
        return top_left, max_size

    def extract_square(grid, top_left, size):
        i, j = top_left
        return [row[j:j+size] for row in grid[i:i+size]]

    top_left, size = find_largest_square(grid)
    return extract_square(grid, top_left, size)