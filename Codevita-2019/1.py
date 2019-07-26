import itertools
data = input()
numbers = data.split()
a, b = numbers[0], numbers[1]
a_digits = [int(a[i]) for i in range(0, len(a))]
# print(a_digits)
b_num = int(b)
if len(a) < len(b):
    print(-1)
    exit()
elif len(a) == len(b):
    b_MSB = int(b[0])
    a_MSB = [digit for digit in a_digits if digit >= b_MSB]
    a_list = list(itertools.permutations(a_digits))
    required_a = [list(i) for i in a_list if i[0] in a_MSB]
    a_nums = [int("".join(map(str, i))) for i in required_a]
    final_a = [i for i in a_nums if i > b_num]
    if len(final_a) != 0:
        final_a.sort()
        print(final_a[0])
    else:
        print(-1)
else:
    a_list = list(itertools.permutations(a_digits))
    a_nums = [int("".join(map(str, i))) for i in a_list]
    final_a = [i for i in a_nums if i > b_num]
    final_a.sort()
    print(final_a[0])