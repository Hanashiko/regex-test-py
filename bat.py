import re

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(f"{mo1.group() = }")
mo2 = heroRegex.search("Tina Fey and Batman")
print(f"{mo2.group() = }")

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile загубив колесо')
print(f"{mo.group() = }\
\n{mo.groups()}")

batRegex = re.compile(r"Bat(wo)?man")
mo1 = batRegex.search('The Adventure of Batman')
print(f"{mo1.group() = }\
\n{mo1.groups() = }")
mo2 = batRegex.search('The Adventure of Batwoman')
print(f"{mo2.group() = }\
\n{mo2.groups() = }")

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search('The Adventure of Batman')
print(f"{mo1.group() = }\
\n{mo1.groups() = }")
mo2 = batRegex.search('The Adventure of Batwoman')
print(f"{mo2.group() = }\
\n{mo2.groups() = }")
mo3 = batRegex.search('The Adventure of Batwowowowoman')
print(f"{mo3.group() = }\
\n{mo3.groups() = }")

batRegex = re.compile(r"Bat(wo)+man")
mo1 = batRegex.search('The Adventure of Batman')
print(f"{(mo1 == None) = }")
mo2 = batRegex.search('The Adventure of Batwoman')
print(f"{mo2.group() = }\
\n{mo2.groups() = }")
mo3 = batRegex.search('The Adventure of Batwowowowoman')
print(f"{mo3.group() = }\
\n{mo3.groups() = }")

