# Deciding whether strings are naughty or nice

# Import data
f = open("Inputs/day5_input.txt", "r")
input_text = f.read().split()

# Functions


def count_distinct_vowels(string):
    vowel_count = (string.count("a") > 0) + (
            string.count("e") > 0) + (
            string.count("i") > 0) + (
            string.count("o") > 0) + (
            string.count("u") > 0)
    return vowel_count


def count_vowels(string):
    vowel_count = string.count("a") + \
            string.count("e") + \
            string.count("i") + \
            string.count("o") + \
            string.count("u")
    return vowel_count


def contains_repeated_letters(string):
    for k in range(len(string) - 1):
        a = string[k]
        b = string[k+1]
        if a == b:
            return True
    return False


def check_unwanted_strings(string):
    if string.count("ab") > 0:
        return True
    if string.count("cd") > 0:
        return True
    if string.count("pq") > 0:
        return True
    if string.count("xy") > 0:
        return True
    return False


def naughty_or_nice(string):
    # First condition - at least three vowels
    if count_vowels(string) < 3:
        return "naughty"
    # Second condition - must have repeated letters
    if not contains_repeated_letters(string):
        return "naughty"
    # Third condition, no specified strings
    if check_unwanted_strings(string):
        return "naughty"
    else:
        return "nice"

string_type_counts = {"nice": 0,
                      "naughty": 0}

for k in range(len(input_text)):
    string_type = naughty_or_nice(input_text[k])
    string_type_counts[string_type] = string_type_counts[string_type] + 1

print(string_type_counts)


# New functions for part 2


def contains_repeated_pair(string):
    for n in range(len(string) - 1):
        pair = string[n:(n+2)]
        if string.count(pair) > 1:
            return True
    return False


def contains_symmetrical_trio(string):
    for n in range(len(string) - 2):
        if string[n] == string[n+2]:
            return True
    return False


def naughty_or_nice_2(string):
    if not contains_repeated_pair(string):
        return "naughty"
    if not contains_symmetrical_trio(string):
        return "naughty"
    return "nice"


string_type_counts_2 = {"nice": 0,
                       "naughty": 0}

for k in range(len(input_text)):
    string_type = naughty_or_nice_2(input_text[k])
    string_type_counts_2[string_type] = string_type_counts_2[string_type] + 1

print(string_type_counts_2)

# print(naughty_or_nice_2("qjhvhtzxzqqjkmpb"))
# print(naughty_or_nice_2("xxyxx"))
# print(naughty_or_nice_2("uurcxstgmygtbstg"))
# print(naughty_or_nice_2("ieodomkazucvgmuy"))

# print(naughty_or_nice("ugknbfddgicrmopn"))
# print(naughty_or_nice("aaa"))
# print(naughty_or_nice("jchzalrnumimnmhp"))
# print(naughty_or_nice("haegwjzuvuyypxyu"))
# print(naughty_or_nice("dvszwmarrgswjxmb"))
