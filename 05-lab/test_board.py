import unittest
from solver import solve

class TestNQueens(unittest.TestCase):
    def test_correct_number_of_solutions(self):
        self.assertEqual(solve(1), 1)
        self.assertEqual(solve(2), 0)
        self.assertEqual(solve(3), 0)
        self.assertEqual(solve(4), 2)
        self.assertEqual(solve(5), 10)
        self.assertEqual(solve(6), 4)
        self.assertEqual(solve(7), 40)
        self.assertEqual(solve(8), 92)

if __name__ == '__main__':
    unittest.main(verbosity=2)