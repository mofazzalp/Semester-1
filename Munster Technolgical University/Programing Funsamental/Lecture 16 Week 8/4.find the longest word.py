# Author : Mofazzal Hossain
# Description : find the longest word

longest_word_len = 0
longest_word = ''
while True:
    word = input('Enter a word or Type Stop to Exit ')
    if word.lower() == 'stop':
        break

    if len(word) > longest_word_len:
        longest_word_len = len(word)
        longest_word = word
print(longest_word, longest_word_len)
print(f"The longest word you entered is '{longest_word}' with a length of {longest_word_len} characters.")

