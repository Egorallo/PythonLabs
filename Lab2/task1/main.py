from package import textStats


def main():
    text = input("Enter text:")

    sentences = textStats.split_into_sentences(text)
    words = textStats.get_actual_words(text)
    print(textStats.split_into_sentences(text))

    print("num of sentences: ", textStats.count_sentences(sentences))
    print("num of non-decl. sentences: ", textStats.count_non_declarative(sentences))
    print("avg sentence length: ", textStats.avg_sentence_len(text, sentences))
    print("avf word length: ", textStats.avg_word_len(text))
    print("top k ngrams: ", textStats.top_k_ngrams(words))


if __name__ == '__main__':
    main()
