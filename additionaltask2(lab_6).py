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
        self.rows = rows
        self.cols = cols
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

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Розмірності матриць не збігаються!")
        result = Matrix(rows=self.rows, cols=self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    def __str__(self):
        return "\n".join(str(row) for row in self.matrix)

if __name__ == "__main__":
    elements_1 = [
        (0, 0, 44), (0, 1, -2), (0, 2, 5), (0, 3, 38), (0, 4, -91),
        (1, 0, 2), (1, 1, 0), (1, 2, 6), (1, 3, 3), (1, 4, 22),
        (2, 0, 13), (2, 1, 1), (2, 2, -4), (2, 3, 90), (2, 4, 11),
        (3, 0, 10), (3, 1, 34), (3, 2, 32), (3, 3, 31), (3, 4, 69)
    ]
    matrix1 = Matrix(rows=4, cols=5, elements=elements_1)

    elements_2 = [
        (0, 0, 10), (0, 1, 5), (0, 2, -1), (0, 3, 3), (0, 4, 8),
        (1, 0, 1), (1, 1, -3), (1, 2, 7), (1, 3, 0), (1, 4, -2),
        (2, 0, 8), (2, 1, -1), (2, 2, 5), (2, 3, 12), (2, 4, -10),
        (3, 0, 3), (3, 1, 14), (3, 2, 6), (3, 3, 11), (3, 4, -7)
    ]
    matrix2 = Matrix(rows=4, cols=5, elements=elements_2)

    print("Перша матриця:")
    print(matrix1)
    print("\nДруга матриця:")
    print(matrix2)

    result_matrix = matrix1 + matrix2
    print("\nРезультат додавання матриць:")
    print(result_matrix)
