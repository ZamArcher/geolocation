
import sys

# if __name__ == "__main__":
# digit_string = sys.argv[1]
# digit_string_num = map(int, digit_string)
# print(sum(digit_string_num))

print(sum([int(x) for x in sys.argv[1]]))