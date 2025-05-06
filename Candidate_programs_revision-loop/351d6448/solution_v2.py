def solve(grid):
    H = len(grid)
    W = len(grid[0])
    colored = []
    for i, row in enumerate(grid):
        has_zero = False
        has_nz = False
        for v in row:
            if v == 0:
                has_zero = True
            else:
                has_nz = True
        if has_zero and has_nz:
            start = None
            end = None
            for j, v in enumerate(row):
                if v != 0:
                    if start is None:
                        start = j
                    end = j
            shape = row[start:end+1]
            colored.append((i, start, shape))
    colored.sort(key=lambda x: x[0])
    N = len(colored)
    _, start0, shape0 = colored[0]
    _, start1, shape1 = colored[1]
    delta_start = start1 - start0
    len0 = len(shape0)
    len1 = len(shape1)
    if shape0 == shape1:
        pred_shape = shape0
    elif len(set(shape0)) == 1 and len(set(shape1)) == 1 and shape0[0] == shape1[0]:
        c = shape0[0]
        delta_len = len1 - len0
        pred_len = len0 + N * delta_len
        pred_shape = [c] * pred_len
    else:
        pred_shape = shape0
    pred_start = start0 + N * delta_start
    out = [[0] * W for _ in range(3)]
    for k, v in enumerate(pred_shape):
        j = pred_start + k
        if 0 <= j < W:
            out[1][j] = v
    return out