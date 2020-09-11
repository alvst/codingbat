def string_match(a, b):
	"""Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings."""
	count = 0
	for i  in range(0, len(b)-1):
		if a[i:i+2] == b[i:i+2]:
			count += 1
	return count



print(string_match('xxcaazz', 'xxbaaz')) # → 3
print(string_match('abc', 'abc')) # → 2
print(string_match('abc', 'axc')) # → 0
