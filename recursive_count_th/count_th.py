'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
	count = 0
	substring = "th"
	my_str = word.find(substring)
	if my_str >= 0:
		my_word = word[my_str + len(substring):]
		count = count + 1 + count_th(my_word)
	return count

print(count_th("thethetoothhurts"))