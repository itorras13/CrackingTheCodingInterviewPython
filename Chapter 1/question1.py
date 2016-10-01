def with_data_strucutre(s):
	characters = [False] * 127
	for char in s:
		value = ord(char)
		if characters[value]:
			return False
		else:
			characters[value] = True
	return True

def without_data_structure(s):
	string_array = list(s)
	string_array.sort()
	for i in range(len(string_array)-1):
		if string_array[i] == string_array[i+1]:
			return False
	return True


print with_data_strucutre("aba")
print with_data_strucutre("abcde ?")

print without_data_structure("aba")
print without_data_structure("abcde ?")