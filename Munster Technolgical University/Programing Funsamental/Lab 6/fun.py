import math

password_pools = {
    "Lowercase": 26,
    "Lower & Upper Case": 52,
    "Alphanumeric": 36,
    "Alphanumeric & Upper Case": 62,
    "Common ASCII Characters": 30,
    "Diceware Words List": 7776,
    "English Dictionary Words": 171000
}

for pool, size in password_pools.items():
    entropy = math.log2(size)
    print(f"{pool}:\n\tEntropy per character: {entropy:.2f} bits\n\tTotal combinations: {2**entropy:.0f}\n")