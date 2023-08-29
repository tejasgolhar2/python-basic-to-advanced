# Three Equal Chunks
# Given a list slice it into Three Equal Chunks and reverse each chunk.

# sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]
# Output

# Chunk-1 = [18, 55, 21]
# Chunk-2 = [22, 24, 33]
# Chunk-3 = [79, 35, 68]

sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]

groups = len(sample_list)/3
val = int(groups)

start = 0
end = val

for item in range(1,4):
    o_list = sample_list[start:end]
    o_list.reverse()
    print(f"Chunk-{item} =",o_list)
    start=end
    end+=val
