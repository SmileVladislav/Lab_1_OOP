class Matrix:
    def __init__(self, data):
        if not data or not data[0]:
            raise ValueError("Матриця не може бути порожньою")
        self._data = data
        self._rows = len(data)
        self._cols = len(data[0])

    def multiply_by_scalar(self, scalar):
        self._data = [[elem * scalar for elem in row] for row in self._data]
        return self._data

    def calculate_variant_sum(self):
        total_sum = 0.0
        for j in range(self._cols):
            column = [self._data[i][j] for i in range(self._rows)]
            if j % 2 == 0:
                total_sum += max(column)
            else:
                total_sum += min(column)
        return total_sum

    def get_data(self):
        return self._data

def main():
    try:
        matrix_obj = Matrix([
            [1.2, 3.4, 5.6],
            [7.8, 0.1, 2.3],
            [4.5, 6.7, 8.9]
        ])

        matrix_obj.multiply_by_scalar(2.5)
        
        for row in matrix_obj.get_data():
            print([round(x, 2) for x in row])

        print(f"\nResult (S): {matrix_obj.calculate_variant_sum()}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
