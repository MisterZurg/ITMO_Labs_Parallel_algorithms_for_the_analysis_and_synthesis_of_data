from mpi4py import MPI

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    req = MPI.COMM_WORLD.irecv(source=0, tag=0)
    message = req.wait()  # wait for the message
    print(message)

if rank == 1:
    message = "Hi!"
    req = MPI.COMM_WORLD.isend(message, dest=1, tag=0)  # send message and move forward
    req.wait()