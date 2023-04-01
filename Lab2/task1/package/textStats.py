import re
from collections import Counter


def split_into_sentences(text: str):
    """
    Splitting text into sentences
    """
    if text == "":
        return []

    sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    sentences = cleared_sentences(sentences)

    return sentences


def get_count_sentences(sentences: list):
    """
    Counting sentences in a provided list of sentences
    """
    print(sentences)
    return len(sentences)


def get_count_non_declarative(sentences: list[str]):
    """
    Counting amount of non-declarative sentences
    """
    count = 0
    for sentence in sentences:
        if not (sentence.endswith(".") or sentence.endswith("...")):
            count += 1

    return count


def get_avg_word_len(text: str):
    """
    Gets average word length
    """
    number_of_letters = 0
    sentences = split_into_sentences(text)
    words = get_actual_words(sentences)
    for word in words:
        number_of_letters += len(word)
    try:
        return number_of_letters / len(words)
    except ZeroDivisionError:
        return 0


def get_avg_sentence_len(text: str):
    """
    Gets average sentence length
    """
    number_of_letters = 0
    sentences = split_into_sentences(text)
    words = get_actual_words(sentences)
    for word in words:
        number_of_letters += len(word)

    try:
        return number_of_letters / len(sentences)
    except ZeroDivisionError:
        return 0


def get_actual_words(sentences: list[str]):
    """
    Splitting text into words
    """
    words = []
    for sentence in sentences:
        sentence = sentence.lower()
        sentence = re.sub(r'[^\w\s]', '', sentence)
        words += sentence.split()
    return words


def get_top_k_ngrams(text: str, k=10, n=4):
    """
    Returns the top-K repeated N-grams in a list of words.
    """
    sentences = split_into_sentences(text)
    words = get_actual_words(sentences)

    ngrams = []
    for i in range(len(words) - n + 1):
        ngrams.append(tuple(words[i:i + n]))
    top_ngrams = Counter(ngrams)

    return top_ngrams.most_common(k)


def cleared_sentences(sentences: list):
    """
    Making sentences contain only latin letters, numbers and separators
    """
    new_sentences = []
    for sentence in sentences:
        new_sentences.append(re.sub(r'\b\d+\b|[^a-zA-Z0-9!?. ]', '', sentence))

    return new_sentences
