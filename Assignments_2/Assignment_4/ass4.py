import time
from dataclasses import dataclass

from mpi4py import MPI


# Message is a structure that defines the Message entity which is sent with MPI
@dataclass
class MessageTime:
    send_time: time = 0


# get_current_time() is a helper function that returns current time./
def get_current_time():
    return time.asctime(time.localtime(time.time()))


# sleep_for() is a helper function that defines the time between sending a message from a worker
def sleep_for(pause=10):
    time.sleep(pause)


TAI_LOPEZ_QUOTE = [
    "Here in my garage, just bought this new Lamborghini here.",
    "It’s fun to drive up here in the Hollywood hills.",
    "But you know what I like more than materialistic things?",
    "Knowledge.",
    "In fact, I’m a lot more proud of these seven new bookshelves that I had to get installed to hold two thousand new books that I bought.",
    "It’s like the billionaire Warren Buffett says, “the more you learn, the more you earn.”"
]

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    # that kind of message you should send in order to calculate
    # time on worker?
    print(f"=================================================================")
    print(f"Master rank={rank} goes brr at {get_current_time()}")
    print(f"=================================================================")

    sleep_for(15)

    print(f"=================================================================")
    print(f"Master rank={rank} wakes up at {get_current_time()}")
    print(f"=================================================================")

    message = MPI.COMM_WORLD.recv(source=1, tag=0)

    print(f"=================================================================")
    print(f"Worker with rank {rank}, got message")
    print(f"Operation tooked {1000 * (time.time() - message.send_time):.4f} ms")
    print(f"=================================================================")

# this program will work only with single worker
if rank == 1:
    my_message_time = MessageTime(send_time=time.time())

    req = MPI.COMM_WORLD.send(my_message_time, dest=0, tag=0)

    for line in TAI_LOPEZ_QUOTE:
        print(line)
        sleep_for(0.5)
