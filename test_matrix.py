import unittest
from matrix import Matrix

class TestMatrixLab(unittest.TestCase):
    def test_multiply_scalar(self):
        
        initial_data = [[1.0, 2.0], [3.0, 4.0]]
        matrix_obj = Matrix(initial_data)
        result = matrix_obj.multiply_by_scalar(2.0)
        self.assertEqual(result, [[2.0, 4.0], [6.0, 8.0]])

    def test_specific_sum(self):
       
        matrix_data = [[10.0, 5.0], [1.0, 2.0]]
        matrix_obj = Matrix(matrix_data)
        result = matrix_obj.calculate_variant_sum()
        self.assertEqual(result, 12.0)

    def test_empty_matrix(self):
        
        with self.assertRaises(ValueError):
            Matrix([])

if __name__ == "__main__":
    unittest.main()
