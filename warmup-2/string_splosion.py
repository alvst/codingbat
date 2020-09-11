def string_splosion(str):
	"""Given a non-empty string like "Code" return a string like "CCoCodCode"."""
	# print(len(str))
	new_string = ""
	for i  in range(0, len(str)):
		# print(i)
		# print(str[i])
		new_string = new_string + str[0:i] 
		# print(new_string)

	return(new_string + str)

print(string_splosion('Code')) # → 'CCoCodCode'
print(string_splosion('abc')) # → 'aababc'
print(string_splosion('ab')) # → 'aab'