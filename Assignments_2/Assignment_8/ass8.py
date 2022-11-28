import time

from mpi4py import MPI

# Get info
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

MESSAGE = "Grzegorz Brzęczyszczykiewicz, Chrząszczyżewoszyce powiat Łękołody"


def wait_for_message(sleep_for=25):
    intervals = int(sleep_for / 5)

    for attempt in range(intervals):
        time.sleep(5)
        print(f"WAITING")


if rank == 0:
    """
        host logic
    """
    MPI.COMM_WORLD.send(MESSAGE, dest=1, tag=1)
    # host must spend 25 seconds in sleep mode before it receives the message
    wait_for_message()

    resp = MPI.COMM_WORLD.recv(source=1, tag=1)
    print(f"Host {rank} received worker message '{resp}'")

if rank == 1:
    """
        worker logic
    """
    req = MPI.COMM_WORLD.recv(source=0, tag=1)
    print(f"Worker {rank} received host message '{req}'")

    resp = "I got your" + req + "Sending it backwards"
    MPI.COMM_WORLD.isend(resp, dest=0, tag=1)
    print(f"Worker {rank} sent message '{resp}' to host")
