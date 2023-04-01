from mpi4py import MPI

a = 2.6
b = 3.3

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    print(a-b)
if rank == 1:
    print(a+b)
if rank == 2:
    print(a*b)
