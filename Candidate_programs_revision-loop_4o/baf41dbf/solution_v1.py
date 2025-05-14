from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_rectangles(grid, color):
        rectangles = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == color:
                    if not rectangles or (r > rectangles[-1][1] or c > rectangles[-1][3]):
                        rectangles.append([r, r, c, c])
                    else:
                        rectangles[-1][1] = max(rectangles[-1][1], r)
                        rectangles[-1][3] = max(rectangles[-1][3], c)
        return rectangles

    def fill_rectangle(grid, rect, color):
        for r in range(rect[0], rect[1] + 1):
            for c in range(rect[2], rect[3] + 1):
                grid[r][c] = color

    output = [row[:] for row in grid]
    rectangles = find_rectangles(grid, 3)
    for rect in rectangles:
        fill_rectangle(output, rect, 3)
    return output