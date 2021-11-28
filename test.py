from solver import *
import unittest

class TestSolver(unittest.TestCase):

    def test_get_car_positions(self):
        test_array = [ [".",".",".","."],[".",".","0","."],[".",".","0","."] ]
        test_array1 = [ ["1","1","1","."],[".",".","0","."],[".",".","0","."] ]
        dd = {'0': [[1, 2], [2, 2]] }
        dd1 = {'0': [[1, 2], [2, 2]], '1': [[0,0],[0,1],[0,2]] }
        self.assertEqual(get_car_positions(test_array), dd)
        self.assertEqual(get_car_positions(test_array1), dd1)

    def test_is_solved(self):
        test_array = [ [".",".",".","."],[".",".","0","."],[".",".","0","."] ]
        test_array1 = [ [".",".","0","."],[".",".","0","."],[".",".","0","."] ]
        test_array2 = [ [".",".","1","."],[".",".","0","."],[".",".","0","."] ]
        self.assertTrue(is_solved(test_array))
        self.assertTrue(is_solved(test_array1))
        self.assertFalse(is_solved(test_array2))

    def test_get_possible_moves(self):
        car = [[1, 2], [2, 2]]
        car1 = [[0, 2], [1, 2]]
        car2 = [[0, 1], [0, 2], [0, 3]]
        car3 = [[0, 1], [0, 2]]
        test_array = [ [".",".",".","."],[".",".","0","."],[".",".","0","."] ]
        test_array1 = [ [".",".","0","."],[".",".","0","."],[".",".",".","."] ]
        test_array2 = [ [".","0","0","0"],[".",".",".","."],[".",".",".","."] ]
        test_array3 = [ [".","0","0","."],[".",".",".","."],[".",".",".","."] ]
        test_array4 = [ [".","0","0","1"],[".",".",".","."],[".",".",".","."] ]
        possible_moves = [[ [".",".","0","."],[".",".","0","."],[".",".",".","."] ]]
        possible_moves1 = [[ [".",".",".","."],[".",".","0","."],[".",".","0","."] ]]
        possible_moves2 = [[ ["0","0","0","."],[".",".",".","."],[".",".",".","."] ]]
        possible_moves3 = [[ ["0","0",".","."],[".",".",".","."],[".",".",".","."] ], [ [".",".","0","0"],[".",".",".","."],[".",".",".","."] ] ]
        possible_moves4 = [[ ["0","0",".","1"],[".",".",".","."],[".",".",".","."] ]]

        self.assertEqual(get_possible_moves(test_array,car),possible_moves)
        self.assertEqual(get_possible_moves(test_array1,car1),possible_moves1)
        self.assertEqual(get_possible_moves(test_array2,car2),possible_moves2)
        self.assertEqual(get_possible_moves(test_array3,car3),possible_moves3)
        self.assertEqual(get_possible_moves(test_array4,car3),possible_moves4)

if __name__ == '__main__':
    unittest.main()