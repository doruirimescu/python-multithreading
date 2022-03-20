# python-multithreading
A framework for easily running multithreaded python functions

## Description
The library consists of two simple classes: `Thread` and `ThreadManager`. 

As the names imply, the `Thread` class encapsulates a single thread: it holds a list of arguments, which shall be supplied one by one to the function to be executed by the thread, and an id.

The `ThreadManager` takes a list of all arguments that the library user wants to run, the number of threads and the function to run. It creates a list of `Thread` objects, and it distributes to each thread the corresponding number of arguments to execute from the list of arguments.

#### How to use
`pyhton3 example.py`
