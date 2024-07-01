import re

beginsWirhHelloRegex = re.compile(r'^Hello')
t1 = beginsWirhHelloRegex.search('Hello world!')
print(f"{t1 = }")
t2 = beginsWirhHelloRegex.search("He said hello.")
print(f"{(t2 == None) = }")

endsWirhNumberRegex = re.compile(r'\d$')
j1 = endsWirhNumberRegex.search("Your number is 42")
print(f"{j1 = }")
j2 = endsWirhNumberRegex.search("Your number is forty two.")
print(f"{(j2 == None) = }")

wholeStringIsNumRegex = re.compile(r'^\d+$')
l1 = wholeStringIsNumRegex.search("1234567890")
print(f"{l1 = }")
l2 = wholeStringIsNumRegex.search("123sd321312")
print(f"{(l2 == None) = }")
l3 = wholeStringIsNumRegex.search("12 2321323")
print(f"{(l3 == None) = }")