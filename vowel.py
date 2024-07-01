import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
result = vowelRegex.findall('RoboCop eats bady food. BABY FOOD.')
print(f"{result = }")

vowelRegex = re.compile(r'[^aeiouAEIOU]')
result = vowelRegex.findall('RoboCop eats bady food. BABY FOOD.')
print(f"{result = }")