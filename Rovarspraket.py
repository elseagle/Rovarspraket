# Rovarspraket
'''Rovarspraket which means "Robbers Language" is sweedish is not very complicated.
You take an ordinary word and replace the consonants with the consonant doubled
with an 'o' in between them. For example 'b' becomes 'bob', m becomes 'mom'.
Vowels are intact. Make a program that translates any length of string into
Rovarspraket. For added difficulty, make it able to translate to and from Rovarspraket

list(input a word)
consonants =

for n  in word:
	if n in consonants:

		n+'o'+n
	else:
		continue

'''

word = input('Enter word: ')
consonants = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
              'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y',
              'Z']
word_list = list(word)
for n  in word:
    if n in consonants:
        new = word_list.insert((word_list.index(n)), (n + "o" + n))
        word_list.remove(n)

    else:
        continue
print("".join(word_list))
