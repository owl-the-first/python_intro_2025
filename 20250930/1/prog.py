def Pareto(*args):
    result = []
    if len(args) == 2 and type(args[0]) == int:
        return args
    for i in range(len(args)):
        f = 1
        for j in range(len(args)):
            if (i != j and args[i][0] <= args[j][0] and args[i][1] <= args[j][1] and
                    (args[i][0] < args[j][0] or args[i][1] < args[j][1])):
                f = 0
                break
        if f:
            result.append(args[i])
        else:
            continue
    return tuple(result)

print(Pareto(*eval(input())))
