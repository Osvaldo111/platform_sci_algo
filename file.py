from math import gcd
VOWELS = 'aeiou'
FIRST_THRESHOLD = 1.5
SECOND_THRESHOLD = 1.0
# read input files
with open('addresses.txt', 'r') as f:
    addresses = [line.strip() for line in f]

with open('drivers.txt', 'r') as f:
    drivers = [line.strip() for line in f]

# calculate suitability scores for all driver-address pairs
scores = {}
for driver in drivers:
    num_vowels = sum([1 for c in driver.lower() if c in VOWELS])
    num_consonants = sum([1 for c in driver.lower() if c.isalpha() and c not in VOWELS])
    for address in addresses:
        if gcd(len(driver), len(address)) > 1:
            if len(address) % 2 == 0:
                score = num_vowels * FIRST_THRESHOLD
            else:
                score = num_consonants * SECOND_THRESHOLD
            score *= 1.5 # 50% above the SS
        else:
            if len(address) % 2 == 0:
                score = num_vowels * FIRST_THRESHOLD
            else:
                score = num_consonants * SECOND_THRESHOLD
        scores[(driver, address)] = score

# find maximum score matching
assigned_addresses = set()
assigned_drivers = set()
total_score = 0
matching = []
for i in range(len(drivers)):
    max_score = 0
    max_pair = None
    for pair, score in scores.items():
        driver, address = pair
        if driver not in assigned_drivers and address not in assigned_addresses:
            if score > max_score:
                max_score = score
                max_pair = pair
    if max_pair is not None:
        matching.append(max_pair)
        total_score += max_score
        driver, address = max_pair
        assigned_drivers.add(driver)
        assigned_addresses.add(address)

print("Total suitability score (SS):", total_score)
for driver, address in matching:
    print("Driver", driver, "is assigned to address:", address)