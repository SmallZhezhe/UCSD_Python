"""For showing defaultdict in the REPL"""
from collections import defaultdict


animals = [
    ("diane", "dog"), ("kurt", "cat"), ("mary", "mouse"),
    ("cory", "cat"), ("margaret", "mouse")
    ]

animal_counts = {}
for name, animal in animals:
    if animal not in animal_counts:
        animal_counts[animal] = 0
    animal_counts[animal] += 1

animal_counts


animal_counts = {}
for name, animal in animals:
    try:
        animal_counts[animal] += 1
    except KeyError:
        animal_counts[animal] = 1

animal_counts


animal_counts = defaultdict(int)
for name, animal in animals:
    animal_counts[animal] += 1

animal_counts

'bird' in animal_counts
animal_counts['bird']
animal_counts


animals
animal_owners = defaultdict(list)
for name, animal in animals:
    animal_owners[animal].append(name)

animal_owners
animal_owners['cat']
