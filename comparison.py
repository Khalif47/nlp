# # nltk.download()
# # nltk.download('wordnet') 

# from itertools import product
# from nltk.corpus import wordnet as wn
# # nltk.download(wordnet, 'C:\\Users\\Abdul\\AppData\\Local\\Programs\\Python\\Python36-32\\nltk_data')
import numpy
from PyDictionary import PyDictionary
import random

file_0 = open("comparison_nlp/nlp/sample_text.txt", "r")
file_2 = open("comparison_nlp/nlp/sample_text_2.txt", "r")




# print(wn.synsets("ball")[0].lemma_names())
def key_stats(file_1):
    common_words = ['a', 'about', 'all', 'is', 'also', 'and', 'as', 'at', 'be', 'because', 'but', 'by', 'can', 'come', 'could', 'day', 'do', 'even', 'find', 'first', 'for',
    'from', 'get', 'give', 'go', 'have', 'he', 'her', 'here', 'him', 'his', 'how', 'I', 'if', 'in', 'into', 'it', 'its', 'just', 'know', 'like', 'look', 'make', 'man', 'many', 'me', 'more', 'my', 'new', 'no', 'not', 'now', 'of', 'on', 'one', 'only', 'or', 'other', 'our', 'out', 'people', 'say', 'see', 'she', 'so', 'some', 'take', 'tell', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'think', 'this', 'those', 'time', 'to', 'two', 'up', 'use', 'very', 'want', 'way', 'we', 'well', 'what', 'when', 'which', 'who', 'will', 'with', 'would', 'year', 'you', 'your']
    words = {}
    for line in file_1:
        for word in line.split():
            word = word.strip(',')
            word = word.strip('.')
            word = word.strip('?')
            word = word.strip('-')
            word = word.strip(':')
            word = word.strip('"')
            word = word.strip("'")
            word = word.strip('[')
            word = word.strip(']')
            word = word.lower()
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
    #
    threshold = numpy.mean(list_numbers, axis=0) + 0.2*numpy.std(list_numbers, axis=0)
    vital_words_list = []
    for item in words:
        if words[item] >= threshold:
            vital_words_list.append([item, words[item]])

    return vital_words_list

def text_comparison(output_1, output_2):
    proximity_index = 0
    sum_index = 0
    for word in output_1:
        sum_index += word[1]
        for other_word in output_2:
            if word[0] in other_word[0] or other_word[0] in word[0]:
                proximity_index += word[1] + other_word[1]
    for other_word in output_2:
        sum_index += other_word[1]
    comparison_index = proximity_index/sum_index
    return comparison_index


t = key_stats(file_0)
b = key_stats(file_2)
print(text_comparison(t, b))
dictionary = PyDictionary()


# def respond(wordList):
#     output = ""
#     for word in wordList:
#         output = (output + " " + (random.choice(dictionary.synonym(word, "html.parser"))))
#     return output
dictionary=PyDictionary("hotel","ambush","joy","perceptive")
print(dictionary.getSynonyms())

# print(respond(['chicken', 'food']))