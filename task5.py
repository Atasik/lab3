from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
   
data = "Hello world from process {}".format(rank)

data = comm.gather(data,root=0)

if rank == 0:
  for i in range(1, size):
    value = data[i]
    print(value)