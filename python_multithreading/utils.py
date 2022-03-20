def partitionDataIntoNChunks(data, n):
    """
        Partition data into chunks of size n.
        Parameters:
            data [list]: list of data
            n [int]: number of chunks
        Returns:
            list of chunks partitioned into chunks of size n. Last chunk may be larger than the rest.
    """
    partitions = list()
    chunk_size = int(len(data) / n)
    partitions = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    if len(partitions) > n:
        partitions[-2] += partitions[-1]
        partitions.pop()
    return partitions

def flatten2DList(data):
    """
        Flatten a 2D list.
        Parameters:
            data [list]: list of data
        Returns:
            list of data flattened
    """
    return [item for sublist in data for item in sublist]
