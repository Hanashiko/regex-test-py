import re

robocop = re.compile(r'robocop', re.I)
res = robocop.search("RoboCop is part man, part machine, all cop.")
print(f"{res.group() = }")

res = robocop.search("ROBOCOP protects the innocent.")
print(f"{res.group() = }")

res = robocop.search("Al, why does your programming book talk about robocop so much?")
print(f"{res.group() = }")