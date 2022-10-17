# Working out how much wrapping paper to buy

# Import data
f = open("Inputs/day2_input.txt", "r")
input_text = f.read()
# Split on the newline character to get separate presents
input_text = input_text.split()
# Make integer and sort so that we can always work by position
present_dims = [[int(y) for y in x.split("x")] for x in input_text]
present_dims = [sorted(x) for x in present_dims]

# Write a function for calculating the paper we need


def calculate_paper(dim_list):
    out = 3 * dim_list[0] * dim_list[1]
    out += 2 * dim_list[1] * dim_list[2]
    out += 2 * dim_list[0] * dim_list[2]
    return out


# Test examples
print(calculate_paper([2, 3, 4]))
print(calculate_paper([1, 1, 10]))

# Now work out all our paper
total_paper = 0
for k in range(len(present_dims)):
    total_paper += calculate_paper(present_dims[k])

print(total_paper)

# Now a function to calculate ribbon


def calculate_ribbon(dim_list):
    out = 2 * dim_list[0]
    out += 2 * dim_list[1]
    out += dim_list[0] * dim_list[1] * dim_list[2]
    return out


# Test examples
print(calculate_ribbon([2, 3, 4]))
print(calculate_ribbon([1, 1, 10]))

# Now work out all our paper
total_ribbon = 0
for k in range(len(present_dims)):
    total_ribbon += calculate_ribbon(present_dims[k])

print(total_ribbon)
