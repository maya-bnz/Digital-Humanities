import collections
import xlsxwriter

plot_file = open('plot_file.txt', 'r', encoding='utf-8')
a = plot_file.read()

workbook = xlsxwriter.Workbook('word_count.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Word')
worksheet.write('B1', 'Counter')

row = 1

# the following code was taken from 'GeeksforGeeks' website
# the purpose of this code is to count the frequency of words from a text file and extract the k most common words

# Instantiate a dictionary, and for every word in the file,
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}
# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in a.lower().split():
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace(":", "")
    word = word.replace("\"", "")
    word = word.replace("!", "")
    word = word.replace("â€œ", "")
    word = word.replace("â€˜", "")
    word = word.replace("*", "")
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

# Print most common word
n_print = int(input("How many most common words to print: "))# 28862
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    worksheet.write(row, 0, word)
    worksheet.write(row, 1, count)
    row += 1
    # print(word, ": ", count)

workbook.close()
# Close the file
plot_file.close()
