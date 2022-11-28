import time
from dataclasses import dataclass

from mpi4py import MPI


# Get my rank
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Message is a structure that defines the Message entity which is sent with MPI
@dataclass
class Message:
    text: str = ""
    send_time: time = 0


# send_cooldown() is a helper function that defines the time between sending a message from a worker
def send_cooldown():
    time.sleep(0.25)


if rank == 0:
    for src in range(1, size):
        data = MPI.COMM_WORLD.recv(source=src, tag=src)

        print(f"Worker with rank {src}, got message {data.text}")
        print(f"Operation tooked {1000 * (time.time() - data.send_time):.4f} ms")
else:
    my_msg = Message(text="우리 사랑하지 말아요")

    send_cooldown()

    my_msg.send_time = time.time()
    MPI.COMM_WORLD.send(my_msg, dest=0, tag=rank)

# mpirun -n 3 python task3.py