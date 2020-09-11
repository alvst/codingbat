def front_times(str, n):
	return(str[:3] * n)
	# for i in range(0, n):
	# 	charAt(i))
"""Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;"""


print(front_times('Chocolate', 2)) #→ 'ChoCho'
print(front_times('Chocolate', 3)) #→ 'ChoChoCho'
print(front_times('Abc', 3))# → 'AbcAbcAbc'
