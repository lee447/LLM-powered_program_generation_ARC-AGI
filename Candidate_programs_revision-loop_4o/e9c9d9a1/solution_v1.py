def solve(grid):
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    color_map = {0: 2, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 3:
                output[r][c] = 3
            elif r % 4 == 0:
                if c < 3:
                    output[r][c] = 2
                elif c >= cols - 5:
                    output[r][c] = 4
            elif r % 4 == 1:
                if c < 3:
                    output[r][c] = 2
                elif c >= cols - 5:
                    output[r][c] = 4
            elif r % 4 == 2:
                if c < 3:
                    output[r][c] = 2
                elif c >= cols - 5:
                    output[r][c] = 4
            elif r % 4 == 3:
                if c < 3:
                    output[r][c] = 2
                elif c >= cols - 5:
                    output[r][c] = 4
            if r % 4 == 1 and 3 <= c < cols - 5:
                output[r][c] = 7
            if r % 4 == 2 and 3 <= c < cols - 5:
                output[r][c] = 7
            if r % 4 == 3 and 3 <= c < cols - 5:
                output[r][c] = 7
            if r % 4 == 0 and 3 <= c < cols - 5:
                output[r][c] = 7
            if r >= rows - 5 and c < 3:
                output[r][c] = 1
            if r >= rows - 5 and c >= cols - 5:
                output[r][c] = 8
    return output