numbers = [8, 1, 6, 11, 16, 12, 2, 3, 7]
nums = [1, 2, 3, 4, 5, 6, 7, 8]
list(map(lambda x, y: x + y, nums, numbers))
[x + y for x, y in zip(nums, numbers)]
double = lambda x: x * 2
doubled = map(double, numbers)
list(doubled)
list(filter(lambda x: x % 2 != 0, numbers))
[x for x in numbers if x % 2 != 0]
list(map(double, filter(lambda x: x % 2 != 0, numbers)))
[x * 2 for x in numbers if x % 2 != 0]

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
