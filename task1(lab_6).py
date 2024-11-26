import math

def create_matrix():
    return [
        [44, -2, 5, 38, -91],
        [2, 0, 6, 3, 22],
        [13, 1, -4, 90, 11],
        [10, 34, 32, 31, 69]
    ]

def selection_sort_row(row):
    n = len(row)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if row[j] < row[min_idx]:
                min_idx = j
        row[i], row[min_idx] = row[min_idx], row[i]
    return row

def sort_rows(matrix):
    for i in range(len(matrix)):
        matrix[i] = selection_sort_row(matrix[i])
    return matrix

def sum_above_secondary_diagonal(matrix):
    n = len(matrix)
    result = []
    for col in range(n):
        sum_col = 0
        for row in range(n):
            if row + col < n - 1:  
                sum_col += matrix[row][col]
        result.append(sum_col)
    return result

def geometric_mean(values):
    product = 1
    count = 0
    for val in values:
        if val > 0:  
            product *= val
            count += 1
    if count == 0:
        return 0  
    return product**(1 / count)

if __name__ == "__main__":
    matrix = create_matrix()
    print("Початкова матриця:")
    for row in matrix:
        print(row)

    sorted_matrix = sort_rows(matrix)
    print("\nМатриця після сортування рядків за зростанням:")
    for row in sorted_matrix:
        print(row)

    sums = sum_above_secondary_diagonal(sorted_matrix)
    print("\nСуми елементів у стовпцях над допоміжною діагоналлю:")
    print(sums)

    geometric_avg = geometric_mean(sums)
    print("\nСереднє геометричне значення сум:")
    print(geometric_avg)