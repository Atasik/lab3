from mpi4py import MPI

def find_sum(vector):
    my_sum = 0.0
    for i in range(len(vector)):
        my_sum += vector[i]
    return my_sum

def find_maximum(vector):
    my_max = 0.0
    for i in range(len(vector)):
        if vector[i] > my_max:
            my_max = vector[i]
    return my_max

n_numbers = 1024

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

my_first_number = n_numbers*rank

vector = []
for i in range(n_numbers):
    vector.append(float(my_first_number + i))

my_sum = find_sum(vector)
my_max = find_maximum(vector)

# Perform reduction across all processes to get global sum and maximum
global_sum = comm.allreduce(my_sum, op=MPI.SUM)
global_max = comm.allreduce(my_max, op=MPI.MAX)

if rank == 0:
    print("The sum of the numbers is", global_sum)
    print("The largest number is", global_max)