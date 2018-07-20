capitals="A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"

characters="a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
word=raw_input("word please")
score=0

capital_found = False
lower_found = False

for i in range(0,len(word)):
	a=i


	if not lower_found:

		for i in range(0,26):
			if word[a]==characters[i]:
				score=score+5
				lower_found = True
				break

	if not capital_found:

		for i in range(0,26):
			if word[a]==capitals[i]:
				score=score+5
				capital_found = True
				break


print score