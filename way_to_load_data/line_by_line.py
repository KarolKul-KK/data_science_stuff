import re


starts_with_hash = 0 

with open('test.txt', 'r') as f:
    for line in f:
        if re.match("^#", line):

            starts_with_hash += 1