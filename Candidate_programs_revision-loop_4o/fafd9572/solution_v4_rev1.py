from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    color_map = {1: 2, 2: 3, 3: 4, 4: 5}
    output = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell in color_map:
                new_row.append(color_map[cell])
            else:
                new_row.append(cell)
        output.append(new_row)
    
    for i in range(len(output)):
        for j in range(len(output[i])):
            if output[i][j] == 2:
                if j > 0 and output[i][j-1] == 2:
                    output[i][j] = 3
                elif j < len(output[i]) - 1 and output[i][j+1] == 2:
                    output[i][j] = 3
            elif output[i][j] == 3:
                if j > 0 and output[i][j-1] == 3:
                    output[i][j] = 4
                elif j < len(output[i]) - 1 and output[i][j+1] == 3:
                    output[i][j] = 4
    return output