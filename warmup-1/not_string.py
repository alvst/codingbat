def not_string(str):
"""Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged."""

print(not_string('candy')) # → 'not candy'
print(not_string('x')) # → 'not x'
print(not_string('not bad')) # → 'not bad'
