"""Slice examples for REPL"""
# List indexing and slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Slices [start:end] or [start:end:increment]
start = 1
end = 6
increment = 2

greet = "GREETINGS"
greet[0:5]
greet[-1]
greet[10:]

numbers[start:end]
numbers[start:]
numbers[:end]
numbers[start:end:increment]
numbers[start::increment]
numbers[:end:increment]
numbers[::increment]

# Reverse the list by modifying the increment
numbers[::-1]


# Note we have not changed the values of the variable
numbers
# How can we find the last item in the list?
numbers[len(numbers)-1]
# But that's kind of ugly, is there a better way?
# YES! Isn't Python great?
numbers[-1]
# Slice from [-5] to the end
numbers[-5:]
# Oh, we really wanted the other end
numbers[-5::-1]
# How about a partial backwards slice?
numbers[-5:-9]
# Wait, what happened?
# That pesky default again!
numbers[-5:-9:-1]
# Or, could we reorder the original start and end?
numbers[-9:-5]


# A negative increment seems to reverse start and end
# Negative increments are useful but tricky
numbers[:9:-1]
numbers[0:9:-1]
numbers[9::-1]

# We can slice strings the same way
greetings = "Greetings Pythonistas"
greetings[:9]
greetings[10:16]
