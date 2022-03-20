import unittest
from python_multithreading.multithreading import ThreadManager, Thread


class TestThreadManager(unittest.TestCase):
    def test_constructor(self):
        function_to_run = lambda x: x
        thread_manager = ThreadManager([["a", "b", "c"], ["d", "e", "f"]], 2, function_to_run)

        self.assertEqual(thread_manager.nThreads, 2)
        self.assertEqual(thread_manager.functionToRun, function_to_run)
        self.assertEqual(len(thread_manager.threads), 2)

        self.assertEqual(thread_manager.arguments, [["a", "b", "c"], ["d", "e", "f"]])

        self.assertEqual(thread_manager.threads[0].argument_list , [["a", "b", "c"]])
        self.assertEqual(thread_manager.threads[1].argument_list , [["d", "e", "f"]])

    def test_run_1_thread(self):
        function_to_run = lambda x: x + "x"
        thread_manager = ThreadManager([["a"], ["b"], ["c"], ["1"], ["2"]], 1, function_to_run)
        thread_manager.run()
        thread_manager.join()

        self.assertEqual(thread_manager.getResults(), ["ax", "bx", "cx", "1x", "2x"])

    def test_run_2_thread(self):
        function_to_run = lambda x: x + "x"
        thread_manager = ThreadManager([["a"], ["b"], ["c"], ["1"], ["2"]], 2, function_to_run)
        thread_manager.run()
        thread_manager.join()

        self.assertEqual(thread_manager.getResults(), ["ax", "bx", "cx", "1x", "2x"])

    def test_run_3_thread(self):
        function_to_run = lambda x: x + "x"
        thread_manager = ThreadManager([["a"], ["b"], ["c"], ["1"], ["2"]], 3, function_to_run)
        thread_manager.run()
        thread_manager.join()

        self.assertEqual(thread_manager.getResults(), ["ax", "bx", "cx", "1x", "2x"])

    def test_run_4_thread(self):
        function_to_run = lambda x: x + "x"
        thread_manager = ThreadManager([["a"], ["b"], ["c"], ["1"], ["2"]], 4, function_to_run)
        thread_manager.run()
        thread_manager.join()

        self.assertEqual(thread_manager.getResults(), ["ax", "bx", "cx", "1x", "2x"])
