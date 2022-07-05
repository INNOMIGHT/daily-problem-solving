string = input()
string_list = string.split()
word_dict = {"apples", "banana"}
frequency_dict = {}
for word in word_dict:
    frequency_dict[word] = 0
for i in string_list:
    if i in frequency_dict.keys():
        frequency_dict[i] += 1
    

print(frequency_dict)
# Output - {'apples': 2, 'banana': 1}