import math

def sorting_decorator(sort_func):
    def wrapper(instance, *args, **kwargs):
        if instance.enable_sorting:
            return sort_func(instance, *args, **kwargs)
        return args[0]  
    return wrapper

class Matrix:
    def __init__(self, rows=4, cols=5, elements=None):
        self.matrix = self._generate_matrix(rows, cols, elements)
        self.enable_sorting = True  

    def _generate_matrix(self, rows, cols, elements):
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        if elements:
            for (i, j, value) in elements:
                matrix[i][j] = value
        return matrix

    @staticmethod
    def selection_sort_row(row):
        n = len(row)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if row[j] < row[min_idx]:
                    min_idx = j
            row[i], row[min_idx] = row[min_idx], row[i]
        return row

    @sorting_decorator
    def sort_rows(self, matrix):
        for i in range(len(matrix)):
            matrix[i] = self.selection_sort_row(matrix[i])
        return matrix

    def sum_above_secondary_diagonal(self):
        n = len(self.matrix)
        result = []
        for col in range(n):
            sum_col = 0
            for row in range(n):
                if row + col < n - 1:  
                    sum_col += self.matrix[row][col]
            result.append(sum_col)
        return result

    @staticmethod
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

    def __str__(self):
        return "\n".join(str(row) for row in self.matrix)

if __name__ == "__main__":
    
    elements = [
        (0, 0, 44), (0, 1, -2), (0, 2, 5), (0, 3, 38), (0, 4, -91),
        (1, 0, 2), (1, 1, 0), (1, 2, 6), (1, 3, 3), (1, 4, 22),
        (2, 0, 13), (2, 1, 1), (2, 2, -4), (2, 3, 90), (2, 4, 11),
        (3, 0, 10), (3, 1, 34), (3, 2, 32), (3, 3, 31), (3, 4, 69)
    ]

    matrix_instance = Matrix(rows=4, cols=5, elements=elements)

    print("Початкова матриця:")
    print(matrix_instance)

    sorted_matrix = matrix_instance.sort_rows(matrix_instance.matrix)
    print("\nМатриця після сортування рядків за зростанням:")
    print(matrix_instance)

    sums = matrix_instance.sum_above_secondary_diagonal()
    print("\nСуми елементів у стовпцях над допоміжною діагоналлю:")
    print(sums)

    geometric_avg = matrix_instance.geometric_mean(sums)
    print("\nСереднє геометричне значення сум:")
    print(geometric_avg)
  
    matrix_instance.enable_sorting = False
    unsorted_matrix = matrix_instance.sort_rows(matrix_instance.matrix)
    print("\nМатриця без сортування (вимкнуто декоратор):")
    print(matrix_instance)
