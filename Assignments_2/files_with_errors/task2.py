from mpi4py import MPI

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()
# fill the missing part
object1 = ...
object2 = ...
object3 = ...

list_of_objects = [object1, object2, object3]
if rank == 0:
    # send message/messages
    # remember how you can efficiently send data to multiple workers

if rank == 1:
    message = MPI.COMM_WORLD.recv(source=0, tag=0)
    print(message)
