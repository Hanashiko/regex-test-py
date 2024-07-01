import re

message = 'Agent Alice gave the secret documents to Agent Bob.'
nameRegax = re.compile(r'Agent \w+')
res = nameRegax.sub('CENSORED', message)
print(f"{res = }\n{message = }")

agentNamesReges = re.compile(r'Agent (\w)\w*')
res = agentNamesReges.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(f"{res = }")