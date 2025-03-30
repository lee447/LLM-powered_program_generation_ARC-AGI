```python
import numpy as np
from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    grid = np.array(grid)
    # Get all unique non-zero colors
    unique_colors = sorted(set(grid.flatten()) - {0})
    
    transformed_grid = np.zeros_like(grid)

    for color in unique_colors:
        mask = (grid == color)
        rows, cols = np.where(mask)
        
        if len(rows) == 0:
            continue
        
        # Translate position to form
        transformed_rows = rows - rows.min()
        transformed_cols = cols - cols.min()
        
        # Place the color in the top-left free area
        row_start = transformed_rows.min()
        col_start = transformed_cols.min()
        
        for r, c in zip(transformed_rows, transformed_cols):
            transformed_grid[row_start + r, col_start + c] = color
        
    return transformed_grid.tolist()
```