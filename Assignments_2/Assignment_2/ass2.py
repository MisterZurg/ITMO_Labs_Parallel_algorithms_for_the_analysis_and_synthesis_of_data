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


data = MPI.COMM_WORLD.scatter(data, root=0)
print(f"Rank {rank} shows data:\n{data}\n")



# mpirun -n 2 python Assignments_2/Assignment_2/fair.py
