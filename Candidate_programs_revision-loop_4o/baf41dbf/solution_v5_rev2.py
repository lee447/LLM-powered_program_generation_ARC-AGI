from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_rectangles(grid, color):
        rectangles = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == color and (r, c) not in visited:
                    min_r, max_r, min_c, max_c = r, r, c, c
                    stack = [(r, c)]
                    while stack:
                        cr, cc = stack.pop()
                        if (cr, cc) in visited:
                            continue
                        visited.add((cr, cc))
                        min_r, max_r = min(min_r, cr), max(max_r, cr)
                        min_c, max_c = min(min_c, cc), max(max_c, cc)
                        for nr, nc in [(cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)]:
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == color and (nr, nc) not in visited:
                                stack.append((nr, nc))
                    rectangles.append([min_r, max_r, min_c, max_c])
        return rectangles

    def fill_rectangle(grid, rect, color):
        for r in range(rect[0], rect[1] + 1):
            for c in range(rect[2], rect[3] + 1):
                if r == rect[0] or r == rect[1] or c == rect[2] or c == rect[3]:
                    grid[r][c] = color

    output = [row[:] for row in grid]
    rectangles = find_rectangles(grid, 3)
    for rect in rectangles:
        fill_rectangle(output, rect, 3)
    return output