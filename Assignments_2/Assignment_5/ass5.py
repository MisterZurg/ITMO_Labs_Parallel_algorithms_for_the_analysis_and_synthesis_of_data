from mpi4py import MPI
import numpy as np


# Get info
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# getRandomVector() is a helper func that accepts size
# returns vector filled with random nums.
def getRandomVector(size):
    return np.random.randint(100, size=size)


# splitVector() is a helper func that accepts vector,
# number of parts that vector is going to be partitioned
def splitVector(vc, parts):
    return np.split(vc, parts)

WORKER_POOL = size - 1

if rank == 0:
    VECTOR_SIZE = 100_000
    vector_1 = getRandomVector(VECTOR_SIZE)
    vector_2 = getRandomVector(VECTOR_SIZE)

    msg_s_1 = splitVector(vector_1, WORKER_POOL)
    msg_s_2 = splitVector(vector_2, WORKER_POOL)

    for worker in range(WORKER_POOL):
        """
        ... each worker must receive their fragment of both vectors
        """
        req_1 = MPI.COMM_WORLD.isend(msg_s_1[worker], dest=worker+1, tag=worker+1)
        req_2 = MPI.COMM_WORLD.isend(msg_s_2[worker], dest=worker+1, tag=worker+1001)

    dot_product = 0

    for worker in range(WORKER_POOL):
        dot_product += MPI.COMM_WORLD.recv(source=worker+1, tag=worker+2001)

    print(f"Dot-product of vector_1 and vector_2 is {dot_product}")
else:
    """
        Worker logic
    """
    resp_1 = MPI.COMM_WORLD.recv(source=0, tag=rank) # recv
    resp_2 = MPI.COMM_WORLD.recv(source=0, tag=rank+1000)
    """
        ... perform element-by-element multiplication
    """
    result = np.dot(resp_1, resp_2)

    print(f"Worker {rank} is performing sum")
    response = MPI.COMM_WORLD.isend(result, dest=0, tag=rank+2000)