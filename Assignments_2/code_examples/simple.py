from mpi4py import MPI

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    message = "Hello, world!"
    MPI.COMM_WORLD.send(message, dest=1, tag=0)   # send message from current rank == 0 to destination rank == 1


if rank == 1:
    message = MPI.COMM_WORLD.recv(source=0, tag=0)
    print(message)  # receive message from rank == 0 and print

# mpirun -np 2 python Assignments_2/code_examples/simple.py