#Take a sentence as input...
sentence = input("Type any sentence:")
sentence = sentence.lower()

#convert the sentence into a list...
sentence_list = sentence.split()
No_of_words = len(sentence_list)#Counting number of words in the sentence...

sentence_new = sentence.replace('python', 'java') #replace all occurences of python with java
sentence_new = sentence_new.title() #capitalize every first letter of words in the sentence

print(f'The sentence has {No_of_words} words.')
print(f'This is the resulting sentence: \n{sentence_new}')

#Code by Gerald Kumero