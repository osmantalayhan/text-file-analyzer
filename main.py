from analyzer import sentiment_analysis
from analyzer import find_sentence_number
from analyzer import average_sentence_length
from analyzer import find_max_min_word
from analyzer import count_word
from analyzer import word_by_sentence
from analyzer import sentence_operations

with open('overview.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
print(sentiment_analysis(text))
sentences = find_sentence_number(text)
print(average_sentence_length(sentences))
print(find_max_min_word(sentences))
print(count_word(sentences), len(count_word(sentences)))
all_counts = word_by_sentence(sentences)
print(all_counts)
print(sentence_operations(all_counts))
