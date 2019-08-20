"""Bad code to test"""

num = 5
nums = [1, 2, 3, 4, 5, 6, 7, 8]

def what(var):
    print(var)
    return var[0]

val = what(nums)
breakpoint() # import pdb; pdb.set_trace()
val = what(num)









"""
print(f'back from first call to what, returned {val}')
print(f'back from last call to what, returned {val}')
"""
