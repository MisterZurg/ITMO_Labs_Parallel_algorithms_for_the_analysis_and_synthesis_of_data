from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()

message_to_send = list(range(150))

req = MPI.COMM_WORLD.isend(message_to_send, dest=1-rank, tag=0)  # non-blocking communication, both 0 and 1 nodes will proceed to receiving operation


recieved_message = MPI.COMM_WORLD.recv(source=1-rank, tag=0)  # here we have request object, not the message itself
# recieved_message = req.wait()  # wait for the message

print(recieved_message)