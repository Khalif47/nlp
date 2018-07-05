# # nltk.download()
# # nltk.download('wordnet') 

# from itertools import product

# # nltk.download(wordnet, 'C:\\Users\\Abdul\\AppData\\Local\\Programs\\Python\\Python36-32\\nltk_data')

import numpy

file_1 = open("comparison_nlp/nlp/sample_text.txt", "r")
file_2 = open("comparison_nlp/nlp/sample_text_2.txt", "r")

words = {}
common_words = ['a', 'about', 'all', 'is', 'also', 'and', 'as', 'at', 'be', 'because', 'but', 'by', 'can', 'come', 'could', 'day', 'do', 'even', 'find', 'first', 'for',
'from', 'get', 'give', 'go', 'have', 'he', 'her', 'here', 'him', 'his', 'how', 'I', 'if', 'in', 'into', 'it', 'its', 'just', 'know', 'like', 'look', 'make', 'man', 'many', 'me', 'more', 'my', 'new', 'no', 'not', 'now', 'of', 'on', 'one', 'only', 'or', 'other', 'our', 'out', 'people', 'say', 'see', 'she', 'so', 'some', 'take', 'tell', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'think', 'this', 'those', 'time', 'to', 'two', 'up', 'use', 'very', 'want', 'way', 'we', 'well', 'what', 'when', 'which', 'who', 'will', 'with', 'would', 'year', 'you', 'your']

for line in file_1:
    for word in line.split():
        try:
            if words[word] is None:
                if word not in common_words:
                    words[word] = 1
            else:
                words[word] += 1
        except KeyError:
            if word not in common_words:
                    words[word] = 1
list_numbers = [] # list containing all count numbers
for item in words:
    list_numbers.append(words[item])

threshold = numpy.std(list_numbers, axis=0) + numpy.mean(list_numbers, axis=0)
print(threshold)


print(words)




