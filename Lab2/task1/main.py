from package import textStats


def main():
    text = ""
    text2 = "Lol."
    sentences = textStats.split_into_sentences(text)
    print(textStats.split_into_sentences(text))
    print(textStats.count_sentences(sentences))
    print(textStats.count_non_declarative(sentences))
    print(textStats.avg_sentence_len(text, sentences))
    print(textStats.avg_word_len(text))


if __name__ == '__main__':
    main()
