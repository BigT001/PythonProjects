def binary_search(list, target):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("step", steps, ":", str(list[start:end+1]))

        steps = steps + 1
        middle = (start + end) // 2

        if target == list[middle]:
            return middle
        
        if target < list[middle]:
            end = middle -1

        else:
            start = middle + 1

    return -1

Mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tarGet = 5

result = binary_search(Mylist, tarGet)
print(f"Target {tarGet} found at index {result}" if result != -1 else f"Target {tarGet} not found in the list")