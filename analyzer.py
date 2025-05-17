from textblob import TextBlob

def sentiment_analysis(text):
    blob = TextBlob(text)
    rows = 20
    cols = 2
    all_counts = [[0 for _ in range(cols)] for _ in range(rows)]
    i=0

    for sentence in blob.sentences:
        all_counts[i][0] = sentence.sentiment.polarity
        all_counts[i][1] = sentence.sentiment.subjectivity
        i +=1
    return all_counts



def find_sentence_number(text):
    sentences = []
    current = ''

    for a in text:
        current += a
        if a in '.?!;:\n,':
            sentences.append(current)
            current = ''
    
    return sentences


def average_sentence_length(sentences):
    length = 0

    for sentence in sentences:
        for a in sentence:
            if a != ' ':
                length = length + 1

    
    return length / len(sentences)

def find_max_min_word(sentences):
    current = ''
    max_word = ''
    min_word = sentences[0]

    for sentence in sentences:
        for a in sentence:
            
            if a in ' .?!;,\n':
                if len(current) > len(max_word):
                    max_word = current
                if current!= '' and len(current) < len(min_word):
                    min_word = current

                current = ''
            else:
                current += a
    
    return max_word, min_word

def count_word(sentences):
    current = ''
    get_words = []

    for sentence in sentences:
        for a in sentence:
            if a in ' .!?,;\n':
                if current != '':
                    get_words.append(current)
                    current = ''

            else:
                current += a
    
    return get_words


def word_by_sentence(sentences):
    rows = 30
    cols = 15
    all_counts = [[0 for _ in range(cols)] for _ in range(rows)]

    i=0
    j=0

    for sentence in sentences:
        current = ''
        for a in sentence:
            if a in ' .!?,;\n':
                if current != '':
                    all_counts[i][j] = current
                    j += 1
                    
                    current = ''
                    
            else:
                current += a

        j= 0
        i += 1
                                
    return all_counts

def sentence_operations(all_counts):
    word_count = 0
    max = 0

    for i in all_counts:
        word_count = 0
        for a in i:
            if a != 0:
                word_count += 1
        if word_count > max:
            max = word_count
    return max
