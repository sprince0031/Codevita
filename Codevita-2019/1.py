import itertools
data = input()
numbers = data.split()
a, b = numbers[0], numbers[1]
a_digits = [int(a[i]) for i in range(0, len(a))]
# print(a_digits)
b_num = int(b)
if len(a) < len(b): # It is impossible to get a greater number if the number of digits of a is lesser than that of b.
    print(-1)
    exit()
elif len(a) == len(b):
    b_MSB = int(b[0])
    print(b_MSB) # Get the leftmost digit of the number we need to compare against so that we can filter out numbers.
    a_MSB = [digit for digit in a_digits if digit >= b_MSB]
    print(a_MSB) # list of all the digits in a that are greater than leftmost digit in b
    a_list = list(itertools.permutations(a_digits))
    print(a_list) # list of all permutations of digits of a
    required_a = [list(i) for i in a_list if i[0] in a_MSB]
    print(required_a)
    a_nums = [int("".join(map(str, i))) for i in required_a]
    print(a_nums)
    final_a = [i for i in a_nums if i > b_num]
    print(final_a)
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