import re
from collections import Counter


def split_into_sentences(text: str):
    """
    Splitting text into sentences
    """
    sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)

    return sentences

def count_sentences(sentences: list):
    """
    Counting sentences in a provided list of sentences
    """
    return len(sentences)


def count_non_declarative(sentences: list[str]):
    """
    Counting amount of non-declarative sentences
    """
    count = 0
    for sentence in sentences:
        if not (sentence.endswith(".") or sentence.endswith("...")):
            count += 1

    return count


def avg_word_len(text: str):
    number_of_letters = 0
    words = get_actual_words(text)
    for word in words:
        number_of_letters+=len(word)

    return number_of_letters / len(words)


def avg_sentence_len(text: str, sentences: list[str]):
    number_of_letters = 0
    words = get_actual_words(text)
    for word in words:
        number_of_letters+=len(word)

    return number_of_letters / len(sentences)


def get_actual_words(text: str):
    return re.findall(r'\b(?![.,\d])\w*[a-zA-Z]\w*\b', text)


def top_k_ngrams(words, k=10, n=4):
    """
    Returns the top-K repeated N-grams in a list of words.
    """
    ngrams = []
    for word in words:
        for i in range(len(word)-n+1):
            ngrams.append(word[i:i+n])
    top_ngrams = Counter(ngrams)
    return top_ngrams.most_common(k)

