from mpi4py import MPI

# Get info
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

WORKER_POOL = 10
MESSAGE = "맨정신"

cycle_list = list(range(WORKER_POOL)) + [0]

for i in range(WORKER_POOL + 1):
    if i == rank or i == rank + WORKER_POOL:
        if i != 0:
            req = MPI.COMM_WORLD.irecv(source=cycle_list[i - 1], tag=i - 1)
            MESSAGE = req.wait()

            print(f"Worker {rank} received message: '{MESSAGE}' from worker {cycle_list[i - 1]}.")

        if i != WORKER_POOL:
            MPI.COMM_WORLD.send(MESSAGE, dest=cycle_list[i + 1], tag=i)

            print(f"Worker {rank} sent message to worker {cycle_list[i + 1]}.")
