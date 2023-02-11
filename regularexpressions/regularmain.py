import re

string = 'search 1'
a = (re.search('search',string))
# print(a.span())
# print(a.start())
# print(a.group())

x = pattern = re.compile('search')
b = pattern.findall(string)
c = pattern.fullmatch(string)
print(c)
# print(pattern.search(string))
