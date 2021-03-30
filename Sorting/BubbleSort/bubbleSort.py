def countSwaps(a, n):
    # Define swap count and sorted variables
    swapCounter = 0
    sorted = False
    # Loop until array is sorted
    while sorted == False:
        sorted = True
        for i in range(n-1):
            if a[i] > a[i+1]:
                # Conduct the swap where elements are not in order
                # Loop terminates if this conditional branch is not entered
                sorted = False
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
                swapCounter += 1
        # Decrement the range which comparisons take place
        n -= 1
        if not(n):
            sorted = True
    print(f"Array is sorted in {swapCounter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a, n)
