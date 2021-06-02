def minimumBribes(q):
    number_of_bribes = 0

    for i in range(len(q) - 1, 0, -1):
        if q[i-1] == i + 1:
            number_of_bribes += 1
            q[i-1], q[i] = q[i], q[i-1]
        elif q[i-2] == i + 1:
            number_of_bribes += 2
            q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]
        else:
            print("Too chaotic")
            return
    print(number_of_bribes)
