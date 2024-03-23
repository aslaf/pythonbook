"""
026
Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an
“ay”. If a word begins with a vowel you just add “way” to the end. For example, pig becomes igpay,
banana becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the
user to enter a word and change it into Pig Latin. Make sure the new word is displayed in lower case.
"""

word = input("Enter a word: ")
vowels = "a", "e", "i", "o", "u"
# end = "way"
# end2 = "ay"
first = word[0]
length = len(word)
rest = word[1:length]

if first not in vowels:
    newword = rest + first +"ay"
else:
    newword = rest + "way"
print(newword.lower())


"""
if word[0] in vowels:
    print(word[1:] + "way")
else:
    print(word[1:] + word[0] + "ay")
"""