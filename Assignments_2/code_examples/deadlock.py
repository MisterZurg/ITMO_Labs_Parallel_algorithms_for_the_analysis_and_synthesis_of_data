from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()
print(rank)
n_ranks = MPI.COMM_WORLD.Get_size()

message_to_send = list(range(150))

MPI.COMM_WORLD.send(message_to_send, dest=1 - rank, tag=0)  # send message from current rank to rank 0 or 1. The program is stuck here


recieved_message = MPI.COMM_WORLD.recv(source=1 - rank, tag=0)

print(recieved_message)