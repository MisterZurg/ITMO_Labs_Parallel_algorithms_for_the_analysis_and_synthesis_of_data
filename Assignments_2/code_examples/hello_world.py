from mpi4py import MPI  # Initialization of communicator

comm = MPI.COMM_WORLD  # get communicator object
rank = comm.Get_rank()
world_size = comm.Get_size()


processor_name = MPI.Get_processor_name()

print("Hello world from processor {}, rank {} out of {} processors\n".format(
    processor_name, rank, world_size))