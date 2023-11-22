def binary_search(lst, target):
    middle = 0
    start = 0
    end = len(lst)
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

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target_value = 20

result = binary_search(my_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Invalid index. Target {target_value} not found in list.")