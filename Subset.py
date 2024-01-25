from itertools import combinations

# Given set of numbers
numbers = [1697976, 1970865, 1481237, 1583430, 1270113, 1188465, 1668778, 1857442, 1658671, 1349846, 1636211, 1887763,
           1887563, 1878763, 1987563, 1898763, 1887563, 1878963, 1855563, 1948763,1148763 
           ]

# Target sum C
C = 6342470

# Initialize variables to store the best sum and its corresponding subset
best_sum = 0
best_subset = []

# Check all possible combinations of the numbers
for r in range(1, len(numbers) + 1):
    for subset in combinations(numbers, r):
        current_sum = sum(subset)
        if best_sum < current_sum <= C:
            best_sum = current_sum
            best_subset = subset

print(best_sum, best_subset)
