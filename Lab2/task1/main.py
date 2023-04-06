from package import textStats


def main():

    text = input("Enter text:")
    while True:
        try:
            k, n = map(int, input("Enter K & N:").split())
            break
        except ValueError:
            pass

    sentences = textStats.split_into_sentences(text)

    print("num of sentences: ", textStats.get_count_sentences(sentences))
    print("num of non-declarative sentences: ", textStats.get_count_non_declarative(sentences))
    print("avg sentence length: ", textStats.get_avg_sentence_len(text))
    print("avg word length: ", textStats.get_avg_word_len(text))
    print(f"top {k} {n}-grams: ", textStats.get_top_k_ngrams(text, k, n))


if __name__ == '__main__':
    main()
