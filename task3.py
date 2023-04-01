from mpi4py import MPI
import sys

# Check that there are two ranks
n_ranks = MPI.COMM_WORLD.Get_size()

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

if rank %2 == 0 and rank != n_ranks-1:
    message = "Hello, world!"
    MPI.COMM_WORLD.send(message, rank+1, tag=0)
if rank %2 == 1:
    message = MPI.COMM_WORLD.recv(source=rank-1, tag=0)
    print(message)