# You can remove 'pass' if you written code in the function 

# Exercise 1
def count_characters(text):
	return len(text)
	pass

# Exercise 2
def remove_spaces(text):
	new_str=""
	for i in text:
		if i != " ":
			new_str += i
	return new_str
	pass

# Exercise 3
def count_vowels(text):
	count=0
	text1=text.lower()
	for i in  text1:
		if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
			count += 1
	return count
	pass

# Exercise 4
def replace_vowels(text):
	new_str=""
	for i in text:
		if i in "aeiouAEIOU":
			i='*'
		new_str+=i
	return new_str
	pass

# Exercise 5
def count_words(text):
	words=text.split()
	return len(words)
	pass

# Exercise 6
def find_longest_word(text):
	maxim=0
	longest=""
	words = text.split()
	for i in range(len(words)):
		if len(words[i])>maxim:
			maxim=len(words[i])
			longest=words[i]
	return longest
	pass
