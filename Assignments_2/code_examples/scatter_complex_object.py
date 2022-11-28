from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


class TMP:
    def __init__(self):
        self.a = 5

    def forward(self):
        print("Hi!")


if rank == 0:
    data = TMP()
else:
    data = None

# note that rank == 0 will receive data as well and we lose original data list for rank == 0
data = MPI.COMM_WORLD.bcast(data, root=0)
print('rank {} has data: {}'.format(rank, data.a))
print('rank {} has method: '.format(rank))
data.forward()