import re

with open(r'regex_test.txt', encoding = "utf-8-sig") as f:
    data = f.readlines()

ln_patt = re.compile(r'([A-Z][a-z]+) ([A-Z][a-zA-Z-]+)*')

for line in data:
    result = ln_patt.findall(line)
    if result:
        print(line.strip())
    else:
        print(None)