from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    output = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell == 1:
                new_row.append(2)
            elif cell == 2:
                new_row.append(3)
            elif cell == 3:
                new_row.append(4)
            elif cell == 4:
                new_row.append(5)
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
            elif output[i][j] == 4:
                if j > 0 and output[i][j-1] == 4:
                    output[i][j] = 5
                elif j < len(output[i]) - 1 and output[i][j+1] == 4:
                    output[i][j] = 5
    return output