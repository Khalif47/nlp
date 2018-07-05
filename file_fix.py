file_2 = open("comparison_nlp/nlp/sample_text_2.txt", "r")

list2 = []
for line in file_2:
    line = line.strip('\n')
    list2.append(line)


print(list2)