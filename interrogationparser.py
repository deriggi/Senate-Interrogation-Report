import re
# read a file and count words

def readFile(filepath):
	lines=[]
	allwords = {}
	with open(filepath) as f:
		lines = f.read().splitlines();
		for line in lines:
			print line
			processALine(line, allwords)
	f.close()
	return lines;

def removeCharAtEnd(word, lechar):
	indexdot = word.rfind(lechar)
	
	if indexdot == len(word) -1:
		word = word[0:len(word)-1]

	return word

def processALine(line, allwords):
	# if line is 5 words or more, use it
	parts = re.split('\s', line);

	for part in parts:
		part = part.lower()
		part = part.strip()
		part = re.sub('[\(\)\,\[\]\}\{\"\'\^]', '', part)
		part = removeCharAtEnd(part, '.')
		print part
	# lowercase all words
	# strip each of []{}"
	# ignore if is < 3


	print len(parts)



numlines = len(readFile('C:/Users/jderiggi/Documents/InterrogationReport/cia.txt'))
print '{0} lines in the file'.format(numlines)