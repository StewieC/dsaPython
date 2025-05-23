import re
s = 'The rain in Spain'
match = re.search(r'\bain\b', s)

print('Start Index:', match.start())
print('End Index:', match.end())