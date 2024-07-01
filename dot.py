import re

atRegex = re.compile(r'.at')
result = atRegex.findall("The cat in the hat sat on the flat mat.")
print(f"{result = }")

atRegex = re.compile(r'..at')
result = atRegex.findall("The cat in the hat sat on the flat mat.")
print(f"{result = }")

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(f"{mo.group() = }\
\n{mo.groups() = }\
\n{mo.group(1) = }\
\n{mo.group(2) = }")

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search("<To serve man> for dinner.>")
print(f'{mo.group() = }')

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search("<To serve man> for dinner.>")
print(f"{mo.group() = }")

noNewLineRegex = re.compile('.*')
res = noNewLineRegex.search('Serve the public trust.\nProtect the\
innocent.\nUphold the law.')
print(f"{res.group() = }")

newLineRegex = re.compile('.*', re.DOTALL)
res = newLineRegex.search('Serve the public trust.\nProtect the\
innocent.\nUphold the law.')
print(f"{res.group() = }")
