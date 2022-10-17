# Navigating where ( means +1 and ) means -1

# Import data
f = open("Inputs/day1_input.txt", "r")
input_text = f.read()

# Process the instructions to numbers
directions = [1 if x == "(" else -1 if x == ")" else None for x in input_text]

# Work out where this gets us to
print(sum(directions))

# Work out cumulative sum to get first time it's negative
# pre-allocate the array
current_floor = [None] * len(directions)
# The work through it, finding the first time the cumulative sius is <0
for k in range(len(directions)):
    if k == 0:
        current_floor[k] = directions[k]
    else:
        current_floor[k] = current_floor[k-1] + directions[k]
    if current_floor[k] < 0:
        # Python indexes from 0 but the problem indexes from 1 so +1
        print(k + 1)
        break

