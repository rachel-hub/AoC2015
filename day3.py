# Delivering presents to houses on an infinite grid

# Import data
f = open("Inputs/day3_input.txt", "r")
input_text = f.read()

# Process the instructions to numbers
# Use complex numbers to index the 2d grid
directions = [1 if x == ">" else
              -1 if x == "<" else
              1j if x == "^" else
              -1j if x == "v" else
              None for x in input_text]

print(input_text[0:10])
print(directions[0:10])

# Navigate the grid and use a dictionary to record presents
presents = {0: 1}
current_location = 0

for k in range(len(directions)):
    current_location += directions[k]
    try:
        presents[current_location]
    except KeyError:
        presents[current_location] = 1
    else:
        presents[current_location] = presents[current_location] + 1

# The number of houses with at least one present in the length of the dictionary
print(len(presents))

# Now repeat but with Santa and robo santa taking turns

new_presents = {0: 2}
santa_location = 0
robo_santa_location = 0
for k in range(len(directions)):
    if k % 2 == 1:  # Odd number so Santa moves
        santa_location += directions[k]
        current_location = santa_location
    else:  # Must be even number so robo santa moves
        robo_santa_location += directions[k]
        current_location = robo_santa_location
    try:
        new_presents[current_location]
    except KeyError:
        new_presents[current_location] = 1
    else:
        new_presents[current_location] = new_presents[current_location] + 1

# Number of houses visited is again the dictionary length
print(len(new_presents))
