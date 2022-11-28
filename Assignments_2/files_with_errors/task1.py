from mpi4py import MPI

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    message = "Hello, world!"
    req = MPI.COMM_WORLD.isend(message, dest=0, tag=0)  # non-blocking communication, if here we have any code, it will be executed


if rank == 1:
    req = MPI.COMM_WORLD.irecv(source=0, tag=1)
    print(message)