def minimumBribes(q):
    total_number_of_bribes = 0

    for i in range(len(q)):
        num_of_bribes = 0

        for j in q[i+1:]:
            if j < q[i]:
                num_of_bribes += 1
        
        if num_of_bribes > 2:
            return "Too chaotic"
        else:
            total_number_of_bribes += num_of_bribes

    return total_number_of_bribes
