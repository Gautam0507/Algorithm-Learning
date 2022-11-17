def BinarySearch(arr, searchKey, low, high):
    while low <= high:
        mid = (low + high) // 2

        if searchKey == arr[mid]:
            return mid
        elif (searchKey > arr[mid]):
            low = mid + 1
        else:
            high = mid - 1

def main():
    array = [3, 6, 5, 4, 7, 8, 9]
    Key = 4

    result = BinarySearch(array, Key, 0, len(array)-1)
    print(result)


if __name__ == "__main__":
    main()
