#Import
from itertools import combinations_with_replacement

#Find combinations of all numbers (with repetition) of up to 5 numbers bewteen 1-10 with a sum of 15
numbers = range(1,11)
target_sum = 15

max_numbers = 5

#function to find combinations that sum to the target value
def find_combinations(numbers, target_sum, max_numbers):
    valid_combinations = []
    for r in range(1, max_numbers + 1):
        for combo in combinations_with_replacement(numbers, r):
            if sum(combo) == target_sum:
            valid_combinations.append(combo)
    return valid_combinations

valid_combinations = find_combinations(numbers, target_sum, max_numbers)

print(f"Total number of combinations: {len(valid_combinations)}")
print("Combinations that have a sum of 15:")
for combo in valid_combinations:
    print(combo)