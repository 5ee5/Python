import random
from collections import Counter

animals = ['cat', 'dog', 'sheep']
weights = [0.5, 0.4, 0.1]

selected_values = random.choices(animals, weights=weights, k=1000)

summary = Counter(selected_values)
for animal, count in summary.items():
    percentage = (count / 1000) * 100
    print(f"{animal}: {count} ({percentage:.2f}%)")