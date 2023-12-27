# Search for a pair of numbers (a, b) with a niceness of 605
# where both a and b are four-digit numbers

niceness_target = 605

# Initialize variables to store the found pair
found_pair = None

# Iterate over the range of four-digit numbers for both a and b
for a in range(1000, 10000):
    for b in range(1000, 10000):
        if (a ** 2 - b ** 2 - a * b) == niceness_target:
            found_pair = (a, b) # save the found pair in a tuple
            break  # Exit the inner loop if a pair is found
    if found_pair:
        print(type(found_pair))
        break  # Exit the outer loop if a pair is found

# Compute the final number as (10000*a) + b if a pair is found
final_number = (10000 * found_pair[0] + found_pair[1]) if found_pair else None

#print(final_number, found_pair)

r = 0
for i in range (100):
    r = (179 * r + 421) % 509
r


