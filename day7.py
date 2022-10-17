# Bitwise logic gates

# Import data
f = open("Inputs/day7_input.txt", "r")
input_text = f.read().split("\n")
input_text = [x.split(" -> ") for x in input_text if x != ""]
input_dict = {x[1]: x[0] for x in input_text}

# Define a function to recurse through the circuit and calculate a value


def recurse_circuit(circuit_dict, value):
    print(value)
    if isinstance(value, int):
        return value
    elif value.isdigit():
        return int(value)
    else:
        cur_val = circuit_dict[value]
        if isinstance(cur_val, int):
            return cur_val
        elif cur_val.isdigit():
            return int(cur_val)
        elif "AND" in cur_val:
            [v1, v2] = cur_val.split(" AND ")
            a = recurse_circuit(circuit_dict, v1) & recurse_circuit(circuit_dict, v2)
            circuit_dict[value] = a
            return a
        elif "OR" in cur_val:
            [v1, v2] = cur_val.split(" OR ")
            a = recurse_circuit(circuit_dict, v1) | recurse_circuit(circuit_dict, v2)
            circuit_dict[value] = a
            return a
        elif "LSHIFT" in cur_val:
            [v1, v2] = cur_val.split(" LSHIFT ")
            a = recurse_circuit(circuit_dict, v1) << int(v2)
            circuit_dict[value] = a
            return a
        elif "RSHIFT" in cur_val:
            [v1, v2] = cur_val.split(" RSHIFT ")
            a = recurse_circuit(circuit_dict, v1) >> int(v2)
            circuit_dict[value] = a
            return a
        elif "NOT" in cur_val:
            v = cur_val.split("NOT ")[1]
            a = ~ recurse_circuit(circuit_dict, v)
            if a < 0:
                a += 65536
            circuit_dict[value] = a
            return a
        else:
            return recurse_circuit(circuit_dict, cur_val)


print(recurse_circuit(input_dict, "a"))

# Now repeat but overriding wire b to 956 after import
input_dict = {x[1]: x[0] for x in input_text}
input_dict["b"] = 956

print(recurse_circuit(input_dict, "a"))
