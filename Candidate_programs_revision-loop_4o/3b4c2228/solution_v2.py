def solve(grid):
    def is_square_of_color(x, y, color):
        return all(grid[i][j] == color for i in range(x, x+2) for j in range(y, y+2))
    
    def find_squares_of_color(color):
        squares = []
        for i in range(len(grid) - 1):
            for j in range(len(grid[0]) - 1):
                if is_square_of_color(i, j, color):
                    squares.append((i, j))
        return squares
    
    def create_output_grid(squares):
        output_grid = [[0, 0, 0] for _ in range(3)]
        for x, y in squares:
            if x < 3 and y < 3:
                output_grid[x][y] = 1
        return output_grid
    
    red_squares = find_squares_of_color(2)
    return create_output_grid(red_squares)