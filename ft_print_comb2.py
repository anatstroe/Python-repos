def ft_print_comb2():
    for i in range(0, 99):
        for j in range(i + 1, 100):
            print("{:02d} {:02d}".format(i, j), end=", ")
    print("99 99", end="")

ft_print_comb2()