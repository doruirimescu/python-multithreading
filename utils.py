def partitionDataIntoChunks(data, chunk_size):
    """
        Partition data into chunks of size chunk_size.
        Parameters:
            data [list]: list of data
            chunk_size [int]: size of each chunk
        Returns:
            list of chunks partitioned into chunks of size chunk_size. Last chunk may be smaller than chunk_size.
    """
    return [data[x:x+chunk_size] for x in range(0, len(data), chunk_size)]

def flatten2DList(data):
    """
        Flatten a 2D list.
        Parameters:
            data [list]: list of data
        Returns:
            list of data flattened
    """
    return [item for sublist in data for item in sublist]
