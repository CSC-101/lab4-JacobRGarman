import data
import lab4
import unittest
import math

# Write your test cases for each part below.
class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        input = [[], [10, 11], [12]]
        result = lab4.first_element(input)
        expected = [10, 12]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates_1(self):
        input = [data.Point(1, 2), data.Point(3, 4)]
        result = lab4.x_coordinates(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input = [data.Point(0, 0), data.Point(-1, -2)]
        result = lab4.x_coordinates(input)
        expected = [0, -1]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        input = [data.Point(1, 2), data.Point(-1, -1)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(1, 2)]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        input = [data.Point(1, 1), data.Point(2, 2)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(1, 1), data.Point(2, 2)]
        self.assertEqual(expected, result)

    # Part 4
    def test_distance_1(self):
        p1 = data.Point(0, 0)
        p2 = data.Point(3, 4)
        result = lab4.distance(p1, p2)
        expected = 5.0
        self.assertAlmostEqual(expected, result)

    def test_distance_2(self):
        p1 = data.Point(1, 2)
        p2 = data.Point(4, 6)
        result = lab4.distance(p1, p2)
        expected = 5.0
        self.assertAlmostEqual(expected, result)

    # Part 5
    def test_manhattan_distance_1(self):
        p1 = data.Point(0, 0)
        p2 = data.Point(3, 4)
        result = lab4.manhattan_distance(p1, p2)
        expected = 7
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        p1 = data.Point(1, 1)
        p2 = data.Point(4, 5)
        result = lab4.manhattan_distance(p1, p2)
        expected = 7
        self.assertEqual(expected, result)

    # Part 6
    def test_distance_all_1(self):
        input = [data.Point(0, 0), data.Point(3, 4)]
        result = lab4.distance_all(input)
        expected = [0.0, 5.0]
        self.assertEqual(expected, result)

    def test_distance_all_2(self):
        input = [data.Point(1, 2), data.Point(6, 8)]
        result = lab4.distance_all(input)
        expected = [math.sqrt(5), math.sqrt(100)]
        self.assertAlmostEqual(expected[0], result[0])
        self.assertAlmostEqual(expected[1], result[1])

if __name__ == '__main__':
    unittest.main()
