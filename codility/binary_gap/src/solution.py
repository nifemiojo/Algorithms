def solution(N):
    b = f'{N:b}'
    print(b)

    len_counter = 0
    lengths = []
    first_one = True

    for i in b:
        if i == "1" and first_one is True:
            first_one = False

        elif i == "1":
            if len_counter != 0:
                lengths.append(len_counter)
                len_counter = 0

        elif i == "0":
            len_counter += 1

    if len(lengths) == 0:
        return 0
    return max(lengths)


# 10010
# 1011001
# 00010010
# 101000

# len_counter = 0
# lengths = []
# first_one = true
# for i in b:

# if i is 1 and there isn't currently a one on
# the stack i.e. stack is empty then add 1 to the stack

# if i is 1 and 1 is on the stack then we set first_one to false
# , if len_counter is not zero append the current len_counter to lengths array 
# and reset len_counter to zero

# if i is 0 then add one to the len_counter