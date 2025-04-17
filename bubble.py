def bubble_sort(arr, order="ascending"):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (order == "ascending" and arr[j] > arr[j+1]) or (order == "descending" and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    order = input("Enter the sorting order (ascending/descending): ").lower()
    
    bubble_sort(numbers, order)
    print(f"Sorted list in {order} order: {numbers}")

    target = int(input("Enter the number to search: "))
    
    # Ensure the list is sorted in ascending order for binary search
    if order == "descending":
        numbers.reverse()
        
    index = binary_search(numbers, target)
    if index != -1:
        print(f"Number {target} is present at index {index}.")
    else:
        print(f"Number {target} is not present in the list.")
