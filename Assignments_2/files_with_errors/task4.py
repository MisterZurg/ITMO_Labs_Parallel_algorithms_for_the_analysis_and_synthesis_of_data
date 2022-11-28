from mpi4py import MPI
from time import sleep

def sleep_for(time=10):
    sleep(time)

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    # that kind of message you should send in order to calculate
    # time on worker?
    message = "Hello, world!"
    # this program will work only with single worker
    req = MPI.COMM_WORLD.isend(message, dest=1, tag=0)

# this program will work only with single worker
if rank == 1:
    message = MPI.COMM_WORLD.recv(source=1, tag=0)
    # perform additional calculations in order to determine 
    # the time to transfer the message
    print(message)
