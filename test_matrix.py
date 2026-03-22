import unittest
from matrix import multiply_by_scalar, calculate_specific_sum

class TestMatrixLab(unittest.TestCase):
    def test_multiply_scalar(self):
        matrix = [[1.0, 2.0], [3.0, 4.0]]
        result = multiply_by_scalar(matrix, 2.0)
        self.assertEqual(result, [[2.0, 4.0], [6.0, 8.0]])

    def test_specific_sum(self):
        matrix = [[10.0, 5.0], [1.0, 2.0]]
        result = calculate_specific_sum(matrix)
        self.assertEqual(result, 12.0)

    def test_empty_matrix(self):
        with self.assertRaises(ValueError):
            multiply_by_scalar([], 5.0)

if __name__ == "__main__":
    unittest.main()