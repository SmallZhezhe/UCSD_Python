"""For showing Counter in REPL"""
from collections import Counter
coins = ["quarter", "dime", "quarter", "penny", "nickel", "dime",
    "penny", "quarter"]
coin_counts = Counter(coins)
coin_counts

letters = Counter("hello world")
letters

animal_counts = Counter(animal for name, animal in animals)
animal_counts


coin_counts.most_common(1)
coin_counts.most_common()
letters.most_common(1)

coin_counts.elements()
list(coin_counts.elements())

coin_counts.update(["dime", "dime"])
coin_counts

coin_counts.subtract(["dime", "penny", "penny"])
coin_counts

coin_counts['nickel'] += 3
coin_counts
