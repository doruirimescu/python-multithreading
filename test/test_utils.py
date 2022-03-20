import unittest
from utils import flatten2DList, partitionDataIntoNChunks


class TestThreadManager(unittest.TestCase):


    def test_partitionDataIntoNChunks(self):
        result = partitionDataIntoNChunks([1, 2], 2)
        self.assertEqual(result, [[1], [2]])

        result = partitionDataIntoNChunks([1, 2, 3], 3)
        self.assertEqual(result, [[1], [2], [3]])

        result = partitionDataIntoNChunks([1, 2, 3], 2)
        self.assertEqual(result, [[1], [2, 3]])

        result = partitionDataIntoNChunks([1, 2, 3], 1)
        self.assertEqual(result, [[1, 2, 3]])

        result = partitionDataIntoNChunks([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
        self.assertEqual(result, [[1, 2, 3, 4], [5, 6, 7, 8, 9]])

        result = partitionDataIntoNChunks([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
        self.assertEqual(result, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        result = partitionDataIntoNChunks([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6], [7, 8, 9]])

        result = partitionDataIntoNChunks([["a", "b", "c"], [1, 2]], 1)
        self.assertEqual(result, [[["a", "b", "c"], [1, 2]]])

        result = partitionDataIntoNChunks( [ ["a", "b", "c"], [1, 2] ], 2)
        self.assertEqual(result, [ [ ["a", "b", "c"]], [[1, 2] ] ] )

        result = partitionDataIntoNChunks( [ ["args1"], ["args2"], ["args3"] ], 2)
        self.assertEqual(result, [ [["args1"]], [["args2"], ["args3"]]] )


    def flatten2DListTemplate(self, data, expected_result):
        result = flatten2DList(data)
        self.assertEqual(result, expected_result)

    def test_flatten2DList(self):
        self.flatten2DListTemplate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.flatten2DListTemplate([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
