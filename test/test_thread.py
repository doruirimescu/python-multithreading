import unittest
from multithreading import Thread

class TestThread(unittest.TestCase):
    def test_constructor(self):
        thread = Thread(["a", "b", "c"], lambda x: x, 1)
        self.assertEqual(thread.argument_list, ["a", "b", "c"])
        self.assertEqual(thread.id, 1)
        self.assertEqual(thread.results_list, [])

    def test_run(self):
        thread = Thread(["a", "b", "c"], lambda x: x + "x", 1)
        thread.run()
        self.assertEqual(thread.results_list, ["ax", "bx", "cx"])
        self.assertEqual(thread.getResults(), ["ax", "bx", "cx"])
