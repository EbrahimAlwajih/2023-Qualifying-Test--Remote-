def is_good_number(number):
    # Extracting each digit from the number
    # map(insert function here, insert iterable here)

    A, B, C, D, E, F = map(int, str(number))

    # Checking the condition
    return A * C + D * F == (A + B) * E - F

def count_good_numbers(L, R):
    count = 0
    for number in range(L, R + 1):
        if is_good_number(number):
            count += 1
    return count

# Given numbers
L = 137774
R = 545039

# Counting good numbers
count_good = count_good_numbers(L, R)
print (count_good)
