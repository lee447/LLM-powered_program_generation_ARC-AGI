import numpy as np
from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    grid = np.array(grid)
    output = np.zeros_like(grid)
    
    height, width = grid.shape

    # Creating an output grid following the same structure as seen in the output examples
    def propagate_color(from_color, to_color):
        if from_color != to_color:
            output[grid == from_color] = to_color

    # Base delta for transformation
    color_map = {
        3: 0,
        1: 1,
        2: 2,
        0: 0,
        8: 8,
        6: 6
    }

    # Check for key color distributions
    for color, replacement in color_map.items():
        if np.any(grid == color):
            propagate_color(color, replacement)

    return output.tolist()