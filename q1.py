def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return

# Task 1 
# create a function with only two variables (x and y) as inputs. If either one of x or y is not a number, the function must return -1. If both are numbers, then need to swap their values using only those two variables, and print the new swapped values.

if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
return -1
x, y = y, x
print(f"Swapped values: {x}, {y}")




# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

print("--- Q1 Task 2 ---")
print("Scenario 1 ('Apple', 10):", swap("Apple", 10))
print("Scenario 2 (9, 17):")
swap(9, 17)






