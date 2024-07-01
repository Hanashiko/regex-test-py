import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(f"{mo1.group() = }\
\n{mo1.groups() = }")
mo2 = haRegex.search("Ha")
print(f"{(mo2 == None) = }")

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search("HaHaHaHaHaHaHaHaHa")
print(f"{mo1.group() = }")

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = nongreedyHaRegex.search("HaHaHaHaHaHaHaHaHa")
print(f"{mo1.group() = }")