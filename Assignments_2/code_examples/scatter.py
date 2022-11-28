from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

class Amogus:
    def __init__(self):
        self.sugoma = "SUS!"

object1 = list(range(42))                   # <- filled
object2 = Amogus()                          # <- filled
object3 = np.array([[1, 2], [3, 4]])        # <- filled

list_of_objects = [object1, object2, object3]

if rank == 0:
    data = list_of_objects
else:
    data = None

# note that rank == 0 will receive data as well and we lose original data list for rank == 0
data = MPI.COMM_WORLD.scatter(data, root=0)
print('rank {} has data: {}'.format(rank, data))