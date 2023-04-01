from mpi4py import MPI
coms = MPI.COMM_WORLD
rank = coms.Get_rank()
print("Hello world from process", rank)