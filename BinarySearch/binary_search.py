def binary_search(lst, target):
    middle = 0
    start = 0
    end = len(lst) - 1  # Adjusted end to prevent index out of range
    steps = 0

    while start <= end:
        print(f"Step {steps}: {lst[start:end+1]}")

        steps += 1
        middle = (start + end) // 2

        if target == lst[middle]:
            return middle
        
        if target < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

def check_target_range(target, lst):
    if not lst:
        return False

    min_value, max_value = lst[0], lst[-1]
    
    if not (min_value <= target <= max_value):
        print(f"Error: Target {target} is out of range [{min_value}, {max_value}].")
        return False

    return True

genNum = list(range(1, 201))

while True:
    try:
        target_value = int(input("Enter Target: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if check_target_range(target_value, genNum):
        result = binary_search(genNum, target_value)

        if result != -1:
            print(f"Target {target_value} found at index {result}")
        else:
            print(f"Target {target_value} not found in list.")