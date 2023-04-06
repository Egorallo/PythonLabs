import unittest

from package.textStats import (
    get_count_sentences,
    get_count_non_declarative,
    get_avg_sentence_len,
    get_avg_word_len,
    get_top_k_ngrams,
    split_into_sentences
)


class TestCountSentences(unittest.TestCase):
    def test_zero_case(self):
        self.assertEqual(get_count_sentences((split_into_sentences(""))), 0)

    def test_multi_case(self):
        self.assertEqual(get_count_sentences(split_into_sentences("Wild huh? Yeah, kinda...")), 2)

    def test_adv_case(self):
        self.assertEqual(
            get_count_sentences(split_into_sentences("Mr. Crack, what's the d12eal? Enough was enough..!")), 2)


class TestCountNonDeclarative(unittest.TestCase):
    def test_zero_case(self):
        self.assertEqual(get_count_non_declarative(split_into_sentences("Fine knowin ya, fella...")), 0)

    def test_multi_case(self):
        self.assertEqual(get_count_non_declarative(
            split_into_sentences("Alrighty, where is Joe?? Apples are red. In case you've missed it tho??")), 2)

    def test_adv_case(self):
        self.assertEqual(get_count_non_declarative(split_into_sentences("Well, fish is it nah! ye ye.")), 1)


class TestAvgSentenceLength(unittest.TestCase):
    def test_zero_case(self):
        self.assertEqual(get_avg_sentence_len(""), 0)

    def test_multi_case(self):
        self.assertEqual(get_avg_sentence_len("fish grab them. True yeah?"), 10)

    def test_adv_case(self):
        self.assertEqual(get_avg_sentence_len("dis crazy enough.. Well might be, might not. Aboba1234!"), 14)


class TestAvgWordLength(unittest.TestCase):
    def test_zero_case(self):
        self.assertEqual(get_avg_word_len("1234."), 0)

    def test_multi_case(self):
        self.assertEqual(get_avg_word_len("fish grab all. fast crazy naah!"), 4)

    def test_adv_case(self):
        self.assertEqual(get_avg_word_len("is00 a word? n 00"), 2.5)


class TestTopKnGrams(unittest.TestCase):
    def test_zero_case(self):
        self.assertEqual(get_top_k_ngrams("note and book", 5, 4), [])

    def test_multi_case(self):
        self.assertEqual(get_top_k_ngrams("z x c z x", 1, 2), [(('z', 'x'), 2)])

    def test_adv_case(self):
        self.assertEqual(get_top_k_ngrams("a b c d a b c d"),
                         [(('a', 'b', 'c', 'd'), 2), (('b', 'c', 'd', 'a'), 1), (('c', 'd', 'a', 'b'), 1),
                          (('d', 'a', 'b', 'c'), 1)])
