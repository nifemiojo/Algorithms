def minimumSwaps(arr):
    minSwaps = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            b = arr[i] - 1
            arr[i], arr[b] = arr[b], arr[i]
            minSwaps += 1
    return minSwaps