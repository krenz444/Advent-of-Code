f = open('input.txt', 'r')

words = f.readlines()

print len(words) 

badwords = ['xy', 'ab', 'cd', 'pq']
vowels = 'aeiou'


count = 0

for word in words:
    if not any(badword in word for badword in badwords):
        vowelcount = 0
	for char in word:
	    for vowel in vowels:
		if char == vowel:
		    vowelcount += 1
	if vowelcount >= 3:
	    lastchar = ''
	    for char in word:
		if char == lastchar:
		    count += 1
		    break
		lastchar = char
            


print count
