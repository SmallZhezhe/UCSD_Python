things = [2.5, 'one', '0']
for thing in things:
    result = None
    try:
        print("In try block, going to convert {}"
            .format(repr(thing)))
        new_int = int(thing)
        print("After converting to int: {}".format(new_int))
        result = 12 / new_int
    except ValueError:
        print("ValueError: Can't convert {} to integer!"
            .format(repr(thing)))
    except ZeroDivisionError:
        print("Divide by zero error, using 1")
        result = 1
    else:
        print("Yay! No error occurred, result={}"
            .format(result))
    finally:
        print("Finally block, result={}".format(result))
    print("In loop still, after the try/except is finished\n")
print("The loop is finished")
