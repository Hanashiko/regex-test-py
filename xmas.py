import re
xmasRegex = re.compile(r'\d+\s\w+')
result = xmasRegex.findall('11 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(f"{result = }")

someRegex = re.compile(r'\w')
result = someRegex.findall("2 RoboCop eats 10 baby food. BABY FOOD.")
print(f"{result = }")