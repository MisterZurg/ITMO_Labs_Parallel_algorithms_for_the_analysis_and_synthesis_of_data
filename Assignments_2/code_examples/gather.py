# Almost out of storage … If you run out, you can't create or edit files, send or receive email on Gmail, or back up to Google Photos.
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

send_message = "Hello World, I'm rank {:d}".format(rank)
receive_message = comm.gather(send_message, root=1)

if rank == 1:
    for i in range(size):
        print(receive_message[i], ' printed from rank {}'.format(rank))

# from mpi4py import MPI
#
# comm = MPI.COMM_WORLD
# size = comm.Get_size()
# rank = comm.Get_rank()
#
# data = (rank+1)**2
# data = comm.gather(data, root=0)
# if rank == 0:
#     for i in range(size):
#         assert data[i] == (i+1)**2
# else:
#     assert data is None