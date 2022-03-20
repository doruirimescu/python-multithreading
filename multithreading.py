#!/usr/bin/python
from utils import partitionDataIntoChunks, flatten2DList
import time
import threading

class Thread(threading.Thread):
    """
        Thread class which represnts a thread.
        Parameters:
            argument_list [list]: list of arguments to be passed to function_to_execute
            function_to_execute [function]: function to be executed by thread
        Returns:
            Thread object
    """
    def __init__(self, argument_list, function_to_execute, id=None):
        threading.Thread.__init__(self)
        self.argument_list = argument_list
        self.function_to_execute = function_to_execute
        self.results_list = list()
        self.id=id

    def run(self):
        for argument in self.argument_list:
            if self.id is not None:
                print("Thread {id} started".format(id=self.id))
            result = self.function_to_execute(*argument)
            self.results_list.append(result)

    def getResults(self):
        return self.results_list

class ThreadManager:
    def __init__(self, arguments, nThreads, functionToRun):
        self._set_argumentsList(arguments)
        self._set_nThreads(nThreads)
        self._set_functionToRun(functionToRun)
        self._setThreads()

    def _set_argumentsList(self, arguments):
        self.arguments = arguments

    def _set_nThreads(self, nThreads):
        self.nThreads = nThreads

    def _set_functionToRun(self, functionToRun):
        self.functionToRun = functionToRun

    def _setThreads(self):
        self.threads = list()
        arguments_per_thread = partitionDataIntoChunks(self.arguments, self.nThreads)
        id = 1
        for argument in arguments_per_thread:
            thread = Thread(argument, self.functionToRun, id)
            self.threads.append(thread)
            id += 1

    def run(self):
        self.start_time = time.time()
        for thread in self.threads:
            thread.start()

    def join(self):
        for thread in self.threads:
            thread.join()

    def getResults(self):
        results = list()
        for thread in self.threads:
            results.append(thread.getResults())
        return flatten2DList(results)

    def getRunningTimeInSeconds(self):
        return time.time() - self.start_time
