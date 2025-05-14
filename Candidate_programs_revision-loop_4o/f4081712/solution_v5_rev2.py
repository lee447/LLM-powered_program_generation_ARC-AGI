from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_largest_nonzero_rectangle(grid):
        n, m = len(grid), len(grid[0])
        max_area = 0
        top_left = (0, 0)
        bottom_right = (0, 0)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    for k in range(i, n):
                        for l in range(j, m):
                            if grid[k][l] == 0:
                                break
                            if all(grid[x][y] != 0 for x in range(i, k+1) for y in range(j, l+1)):
                                area = (k - i + 1) * (l - j + 1)
                                if area > max_area:
                                    max_area = area
                                    top_left = (i, j)
                                    bottom_right = (k, l)
        return top_left, bottom_right

    def extract_rectangle(grid, top_left, bottom_right):
        i1, j1 = top_left
        i2, j2 = bottom_right
        return [row[j1:j2+1] for row in grid[i1:i2+1]]

    def find_largest_rectangle_of_same_color(grid):
        n, m = len(grid), len(grid[0])
        max_area = 0
        top_left = (0, 0)
        bottom_right = (0, 0)
        
        for i in range(n):
            for j in range(m):
                color = grid[i][j]
                for k in range(i, n):
                    for l in range(j, m):
                        if grid[k][l] != color:
                            break
                        if all(grid[x][y] == color for x in range(i, k+1) for y in range(j, l+1)):
                            area = (k - i + 1) * (l - j + 1)
                            if area > max_area:
                                max_area = area
                                top_left = (i, j)
                                bottom_right = (k, l)
        return top_left, bottom_right

    top_left, bottom_right = find_largest_rectangle_of_same_color(grid)
    return extract_rectangle(grid, top_left, bottom_right)