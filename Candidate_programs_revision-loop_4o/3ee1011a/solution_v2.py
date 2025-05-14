from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    non_zero_coords = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 0:
                non_zero_coords.append((r, c, grid[r][c]))
    
    min_r = min(coord[0] for coord in non_zero_coords)
    max_r = max(coord[0] for coord in non_zero_coords)
    min_c = min(coord[1] for coord in non_zero_coords)
    max_c = max(coord[1] for coord in non_zero_coords)
    
    output_size = max(max_r - min_r, max_c - min_c) + 3
    output_grid = [[0] * output_size for _ in range(output_size)]
    
    for r in range(output_size):
        for c in range(output_size):
            if r == 0 or r == output_size - 1 or c == 0 or c == output_size - 1:
                output_grid[r][c] = non_zero_coords[0][2]
            else:
                output_grid[r][c] = 0
    
    for r, c, color in non_zero_coords:
        output_grid[r - min_r + 1][c - min_c + 1] = color
    
    return output_grid