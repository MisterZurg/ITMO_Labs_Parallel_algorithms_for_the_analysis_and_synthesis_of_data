from mpi4py import MPI
"""
    We have to find different parts form Simple communication communication slide 13
"""

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()


if rank == 0:
    message = "Hello, world!" #                     |
    req = MPI.COMM_WORLD.isend(message, dest=1, tag=0) # send message from current rank == 0 to destination rank == 1


if rank == 1: #                              |
    req = MPI.COMM_WORLD.irecv(source=0, tag=0)
    """
        Core corrected part
    """
    message = req.wait()  # wait for the message
    print(message)


# mpirun -n 2 python Assignments_2/Assignment_1/ass1.py