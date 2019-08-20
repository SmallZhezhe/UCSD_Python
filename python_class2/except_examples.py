things = [2.5, 'one']
for thing in things:
    try:
        print("In try block, going to convert {}"
              .format(repr(thing)))
        new_int = int(thing)
        print("After converting to int: {}".format(new_int))
    except ValueError:
        print("ValueError: Can't convert {} to integer!"
              .format(repr(thing)))
    else:
        print("Yay! No error occurred this time!")
    finally:
        print("Finally!")
    print("After the try is finished\n")

print("The loop is finished")


"""
try:
    print("This code might raise an exception.")
    # Some code goes here
except Exception1:
    print("If Exception1 happens, we come to this block.")
    # Code to deal with Exception1
    # We can optionally re-raise the exception to the calling code
    raise
except Exception2:
    print("If Exception2 happens, we come to this block.")
    # Code to deal with Exception2
else:
    print("Optionally, this block is when there are no exceptions.")
print("After all is done we continue here,")
print("Unless an unhandled exception occurred,")
print("or we re-raised the exception.")



try:
    print("This code might raise an exception")
    # Some code goes here
except (Exception1, Exception2):
    print("If Exception1 or Exception2 happens, we come here")
    # Code to deal with Exception1 and Exception2
    # We can optionally re-raise the exception to the calling code
finally:
    print("This block is always executed before leaving try-except")
    # Code to do some cleanup, no matter what happens
print("After all is done we continue here,")
print("Unless an unhandled exception occurred,")
print("or we re-raised the exception.")


"""
