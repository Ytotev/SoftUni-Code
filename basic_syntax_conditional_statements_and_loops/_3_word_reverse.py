#word = input()
# reversed_word = ''
# for letter in range(len(word) - 1, -1, -1):
#     reversed_word += word[letter]
#
# print(reversed_word)
# print(word[:: - 1])
my_string = "sparkbyexamples"
substring5 = my_string[::-1]

# Slice from index 0 to 4
substring1 = my_string[0:5] # Returns "spark"

# Slice from index 5 to the end
substring2 = my_string[5:] # Returns "byexamples"

# Slice from index 5 to index 7
substring3 = my_string[5:8] # Returns  "bye"

# Slice from the beginning to index 7
substring4 = my_string[:8] # Returns "sparkbye"
print(substring5)