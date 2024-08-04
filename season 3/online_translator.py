# we can solve this program with two way
# first way ------------------------------

dictionary = dict()
dict_word_number = int(input())
# use '_' in loop, when we don't need loop variable
for _ in range(dict_word_number):
    english, persian = input().split(' ')
    dictionary[english] = persian

sentence = input()
sentence_list = sentence.split(' ')

for word in sentence_list:
    if word in dictionary.keys():
        sentence = sentence.replace(word,dictionary[word])
print(sentence)

# second way ------------------------------

dictionary2 = {}
dic_word_number = int(input())
for i in range(0,dic_word_number):
    english, persian = input().split()
    dictionary2[english] = persian

sentence2 = input().split()
translate_sentence = str()
for word in sentence2:
    if word in dictionary2:
        translate_sentence = translate_sentence + dictionary2[word] +' '
    else:
        translate_sentence = translate_sentence + word +' '
print(translate_sentence)