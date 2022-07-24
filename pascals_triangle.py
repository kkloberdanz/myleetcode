def gen(num_rows):
    if num_rows <= 0:
        return []
    if num_rows == 1:
        return [[1]]

    triangle = [[1], [1, 1]]
    for row_idx in range(2, num_rows):
        row = [1]
        previous_row = triangle[row_idx - 1]
        for after in range(1, len(previous_row)):
            before = after - 1
            row.append(previous_row[before] + previous_row[after])
        row.append(1)
        triangle.append(row)
    return triangle
