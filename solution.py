
# import sys
#
# digit_string = sys.argv[1]
# stair_step = 1
# max_stair_step = int(digit_string)
# for i in range(max_stair_step):
#     max_stair_step -= 1
#     print(" " * max_stair_step + "#" * stair_step)
#     stair_step += 1

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b ** 2 - 4 * a * c

x_1 = ((-1) * b + D ** 0.5) / (2 * a)
x_2 = ((-1) * b - D ** 0.5) / (2 * a)

print(int(x_1))
print(int(x_2))
