import itertools
import time
a, b = map(int, input().split())
startTime = time.time()
# a_digits = [int(a[i]) for i in range(0, len(a))]
# print(a_digits)
# b_num = int(b)
if len(str(a)) < len(str(b)): # It is impossible to get a greater number if the number of digits of a is lesser than that of b.
    print(-1)
else:
    a_list = list(itertools.permutations(str(a)))
    a_nums = [int("".join(i)) for i in a_list]
    # final_a = [i for i in a_nums if i > b_num]
    a_nums.sort()
    if len(str(a)) > len(str(b)):
        print(a_nums[0])
    else:
        flag = 0
        for number in a_nums:
            if number > b:
                print(number)
                flag = 1
                break
            else:
                continue
        if flag == 0:
            print(-1)
print("program finished in {} milliseconds".format((time.time() - startTime)*100))
