def stepPerms(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)

res = stepPerms(5)
print(res)