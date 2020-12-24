
import sys

digit_string = sys.argv[1]
stair_step = 1
max_stair_step = int(digit_string)
for i in range(max_stair_step):
    max_stair_step -= 1
    print(" " * max_stair_step + "#" * stair_step)
    stair_step += 1

