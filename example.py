
from multithreading import ThreadManager

def test_function(one_arg):
    print("Thread started", one_arg)
    for i in range(10):
        print(i, "From thread", one_arg)
    print("Thread ended")
    return one_arg

#Define number of threads
N_THREADS = 10

#List of arguments for each individual function call
ARGUMENT_LIST = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]
RESULT_LIST = list()

tm = ThreadManager(ARGUMENT_LIST, N_THREADS, test_function)
tm.run()
tm.join()
RESULT_LIST=tm.getResults()
print(RESULT_LIST)
print("Total running time:", tm.getRunningTimeInSeconds(), "seconds")
