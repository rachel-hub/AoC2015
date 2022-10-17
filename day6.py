# Turning on and off lights

# Modules
import numpy as np

# Code our lights as a numpy array where -1 is off and 1 is on
# Start with everything off
lights = -1 * np.ones((1000, 1000))

# Import data
f = open("Inputs/day6_input.txt", "r")
input_text = f.read().split("\n")
input_text = [x.split() for x in input_text if x is not ""]

# Functions for light control


def turn_on_lights(light_array, x_1, y_1, x_2, y_2):
    light_array[x_1:(x_2+1), y_1:(y_2 + 1)] = 1
    return light_array


def turn_off_lights(light_array, x_1, y_1, x_2, y_2):
    light_array[x_1:(x_2+1), y_1:(y_2 + 1)] = -1
    return light_array


def toggle_lights(light_array, x_1, y_1, x_2, y_2):
    light_array[x_1:(x_2+1), y_1:(y_2 + 1)] *= -1
    return light_array


# Apply instructions to lights
for k in range(len(input_text)):
    instruction = input_text[k]
    if instruction[0] == "toggle":
        [x1, y1] = [int(x) for x in instruction[1].split(",")]
        [x2, y2] = [int(x) for x in instruction[3].split(",")]
        print("toggle", x1, x2, y1, y2)
        lights = toggle_lights(lights, x1, y1, x2, y2)
    else:
        [x1, y1] = [int(x) for x in instruction[2].split(",")]
        [x2, y2] = [int(x) for x in instruction[4].split(",")]
        if instruction[1] == "on":
            print("on", x1, x2, y1, y2)
            lights = turn_on_lights(lights, x1, y1, x2, y2)
        elif instruction[1] == "off":
            print("off", x1, x2, y1, y2)
            lights = turn_off_lights(lights, x1, y1, x2, y2)

print(np.sum(lights > 0))

# Redefine instructions for part 2


def turn_on_lights(light_array, x_1, y_1, x_2, y_2):
    light_array[x_1:(x_2+1), y_1:(y_2 + 1)] += 1
    return light_array


def turn_off_lights(light_array, x_1, y_1, x_2, y_2):
    light_array[x_1:(x_2+1), y_1:(y_2 + 1)] += -1
    light_array[light_array < 0] = 0
    return light_array


def toggle_lights(light_array, x_1, y_1, x_2, y_2):
    light_array[x_1:(x_2+1), y_1:(y_2 + 1)] += 2
    return light_array


# This time lights need to start at 0
lights = np.zeros((1000, 1000))

# Apply new instructions to lights
for k in range(len(input_text)):
    instruction = input_text[k]
    if instruction[0] == "toggle":
        [x1, y1] = [int(x) for x in instruction[1].split(",")]
        [x2, y2] = [int(x) for x in instruction[3].split(",")]
        print("toggle", x1, x2, y1, y2)
        lights = toggle_lights(lights, x1, y1, x2, y2)
    else:
        [x1, y1] = [int(x) for x in instruction[2].split(",")]
        [x2, y2] = [int(x) for x in instruction[4].split(",")]
        if instruction[1] == "on":
            print("on", x1, x2, y1, y2)
            lights = turn_on_lights(lights, x1, y1, x2, y2)
        elif instruction[1] == "off":
            print("off", x1, x2, y1, y2)
            lights = turn_off_lights(lights, x1, y1, x2, y2)

print(np.sum(lights))
