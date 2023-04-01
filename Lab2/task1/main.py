from package import textStats


def main():
    text = input("Enter text:")
    k, n = map(int, input("Enter K & N:").split())

    sentences = textStats.split_into_sentences(text)

    print("num of sentences: ", textStats.count_sentences(sentences))
    print("num of non-declarative sentences: ", textStats.count_non_declarative(sentences))
    print("avg sentence length: ", textStats.avg_sentence_len(text))
    print("avg word length: ", textStats.avg_word_len(text))
    print(f"top {k} {n}-grams: ", textStats.top_k_ngrams(text, k, n))


if __name__ == '__main__':
    main()
