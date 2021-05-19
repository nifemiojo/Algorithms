def change(amount):
    assert (1000 >= amount >= 24)
    if amount == 24:
        return [5, 5, 7, 7]
    elif amount == 25:
        return [5, 5, 5, 5, 5]
    elif amount == 26:
        return [7, 7, 7, 5]
    elif amount == 27:
        return [5, 5, 5, 5, 7]
    elif amount == 28:
        return [7, 7, 7, 7]

    coins = change(amount - 5)
    coins.append(5)

    return coins


for n in range(24, 1001):
    print(sum(change(n)))