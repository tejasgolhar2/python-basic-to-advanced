# Write a program to test the given tuple is distinct

# Distinct Tuple : Tuple containg distinct individual elements i.e., no repetition allowed

def distinctTuple(v_tuple):
    n_list = set(v_tuple)
    if len(n_list)==len(v_tuple):
        print("Tuple is distinct")
    else:
        print("Tuple isn't distinct")


tuple1 = (1,1,232,455,6,1,6,2,6,2)
distinctTuple(tuple1)