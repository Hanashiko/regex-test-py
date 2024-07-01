def isPhoneNumber(text: str) -> bool:
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True

print(f"{isPhoneNumber('643-134-1235') = }")
print(f"{isPhoneNumber('some text') = }")
print(f"{isPhoneNumber('213-123-d332') = }")

message = "Зателефонуй на мій телефон 841-241-1244. Не сплуйтай з 841-241-12433. бажано завтра о 8 ранку"
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print(f"Знайшов номер телефону: {chunk}")

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
myNumber = phoneNumRegex.search("Мій номер телефону: 832-323-3213.")
print(f"Знайдений номер телефону: {myNumber.group()}")

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
myNumber = phoneNumRegex.search("Мій номер телефону: 212-321-2133. Номер мого друга: 121-942-2421")
print(f"{myNumber.group() = }\
\n{myNumber.group(0) = }\
\n{myNumber.group(1) = }\
\n{myNumber.group(2) = }\
\n{myNumber.groups() = }")
areaCode, mainNumber = myNumber.groups()
print(f"{areaCode = }\
\n{mainNumber = }")

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
myNumber = phoneNumRegex.search("Мій номер: (212) 213-2312.")
print(f"{myNumber.group(1) = }\
\n{myNumber.group(2) = }")

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search("мій номер: 982-233-1231.")
print(f"{mo1.group() = }\
\n{mo1.groups()})")
mo2 = phoneRegex.search("мій номер: 312-1232")
print(f"{mo2.group() = }\
\n{mo2.groups()}")

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall("Перший мій номер: 321-233-1233\
\nДругий номер: 233-312-3123\
\nЩе якийсь номер: 833-323-3232")
print(f"{mo = }")

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall("Перший мій номер: 321-233-1233\
\nДругий номер: 233-312-3123\
\nЩе якийсь номер: 833-323-3232")
print(f"{mo = }")

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?
	(\s|-|\.)?
	\d{3}
	(\s|-|\.)
	\d{4}
	(\s*(ext|x|ext.)\s*\d{2,5})?
)''', re.VERBOSE)
mo = phoneRegex.findall("Мій телейон: (021)-222-1221")
print(f"{mo = }")