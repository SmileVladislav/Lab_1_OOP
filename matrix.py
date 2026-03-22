def multiply_by_scalar(matrix, scalar):
    if not matrix or not matrix[0]:
        raise ValueError("Матриця порожня")
    return [[elem * scalar for elem in row] for row in matrix]


def calculate_specific_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_sum = 0.0

    for j in range(cols):
        column = [matrix[i][j] for i in range(rows)]
        if j % 2 == 0:
            total_sum += max(column)
        else:
            total_sum += min(column)
    return total_sum


def main():
    try:
        a = 2.5
        matrix_b = [
            [1.2, 3.4, 5.6],
            [7.8, 0.1, 2.3],
            [4.5, 6.7, 8.9]
        ]

        matrix_c = multiply_by_scalar(matrix_b, a)

        for row in matrix_c:
            print([round(x, 2) for x in row])

        result = calculate_specific_sum(matrix_c)
        print(f"\nResult: {result}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()