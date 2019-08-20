"""Some weird examples of making generator functions for REPL"""

def all_together(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

def all_together(*iterables):
    for iterable in iterables:
        yield from iterable

def strange_number_generator():
    for i in range(1, 10, 2):
        yield i
    for i in range(10, 21, 2):
        yield i

def first_odds():
    for i in range(1, 10, 2):
        yield i

def next_evens():
    for i in range(10, 21, 2):
        yield i

def strange_number_generator():
    yield from first_odds()
    yield from next_evens()
