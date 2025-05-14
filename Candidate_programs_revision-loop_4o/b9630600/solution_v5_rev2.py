def solve(grid):
    def find_rectangles(grid):
        rectangles = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 3:
                    if (r == 0 or grid[r-1][c] != 3) and (c == 0 or grid[r][c-1] != 3):
                        end_r, end_c = r, c
                        while end_r < len(grid) and grid[end_r][c] == 3:
                            end_r += 1
                        while end_c < len(grid[0]) and grid[r][end_c] == 3:
                            end_c += 1
                        rectangles.append((r, c, end_r, end_c))
        return rectangles

    def fill_rectangles(grid, rectangles):
        for r1, c1, r2, c2 in rectangles:
            for r in range(r1, r2):
                for c in range(c1, c2):
                    if r == r1 or r == r2 - 1 or c == c1 or c == c2 - 1:
                        grid[r][c] = 3
                    else:
                        grid[r][c] = 0

    rectangles = find_rectangles(grid)
    fill_rectangles(grid, rectangles)
    return grid