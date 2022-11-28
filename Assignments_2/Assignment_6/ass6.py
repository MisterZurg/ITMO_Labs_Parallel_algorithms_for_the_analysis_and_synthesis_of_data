from sys import getsizeof
import time

from mpi4py import MPI

# Get info
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# host should send a message to the worker, then the worker should send it back N-times
N = 10
NUMBER_OF_SHEET_ELEMENTS = 51

if rank == 0:
    """
        host logic
    """
    for i in range(NUMBER_OF_SHEET_ELEMENTS):
        current_list_size = 1000 * i
        my_list = [1337] * (current_list_size + 1)
        L = getsizeof(my_list)  # size in bytes

        # Start time of the sending process
        T = time.time()
        for attempt in range(N):
            MPI.COMM_WORLD.send(my_list, dest=1, tag=current_list_size + attempt)
            resp = MPI.COMM_WORLD.recv(source=1, tag=current_list_size + attempt + 1)

        # Time after sending/receiving the last msg
        T = time.time() - T

        # Measure bandwidth
        R = (2 * N * L) / T
        print(f"Iteration{i}: object_size {L}(bytes): {R} (MB/s)")
if rank == 1:
    """
        worker logic
    """
    for i in range(NUMBER_OF_SHEET_ELEMENTS):
        current_list_size = 1000 * i
        for attempt in range(N):
            req = MPI.COMM_WORLD.recv(source=0, tag=current_list_size + attempt)
            MPI.COMM_WORLD.send(req, dest=0, tag=current_list_size + attempt + 1)
