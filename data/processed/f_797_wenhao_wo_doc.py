import random
import re


def f_797(target_words, n_sentences, vocabulary):
    """
    Generate sentences with spaces in certain target words replaced by underscores.

    Parameters:
    - target_words (list of str): List of words/phrases where spaces should be replaced with underscores.
    - n_sentences (int):          Number of sentences to generate. Must not be negative.
    - vocabulary (list of str):   List of words to use for generating sentences. Must not be empty.

    Returns:
    - list of str: A list of generated sentences in all lowercase, with specified words/phrases underscored.

    Raises:
    - ValueError: If n_sentences is negative or if the vocabulary is empty.

    Requirements:
    - random
    - re

    Notes:
    - Each sentence is generated by randomly sampling 10 words with replacement from a vocabulary,
      then concatenating with a single whitespace. Then, if any words from the target_words list
      appear in these sentences, spaces within those words are replaced with underscores; here the
      modification is insensitive to the case of the letters.
    - The function returns the processed sentences as a list of all lowercase strings.

    Examples:
    >>> random.seed(42)
    >>> f_797(['apple banana'], 1, ['apple', 'banana', 'cherry'])
    ['banana apple apple apple cherry cherry cherry apple_banana apple']
    >>> f_797(['Alice Charlie', 'ALICE BOB', 'aLiCe dAn'], 1, ['alice', 'bob', 'charlie', 'dan'])
    ['alice_charlie alice alice_charlie charlie alice_charlie dan alice']
    """
    if n_sentences < 0:
        raise ValueError("n_sentences cannot be negative.")
    if not vocabulary:
        raise ValueError("Vocabulary cannot be empty.")

    sentences = []
    for _ in range(n_sentences):
        sentence = " ".join(random.choices(vocabulary, k=10))
        for word in target_words:
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            sentence = pattern.sub(word.replace(" ", "_"), sentence)
        sentences.append(sentence.lower())
    return sentences

import unittest
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        self.vocabulary = [
            "apple",
            "banana",
            "cherry",
            "date",
            "elderberry",
            "fig",
            "grape",
            "honeydew",
        ]
        random.seed(42)
    def test_case_1(self):
        # Test with multiple target words and sentences
        target_words = ["apple banana", "banana cherry"]
        n_sentences = 1000
        results = f_797(target_words, n_sentences, ["apple", "banana", "cherry"])
        self.assertEqual(len(results), n_sentences)
        for target in target_words:
            underscored_target = target.replace(" ", "_")
            self.assertTrue(
                any(underscored_target in sentence for sentence in results),
                f"{underscored_target} not found in any sentences",
            )
    def test_case_2(self):
        # Test with a single target word in multiple occurrences
        target_words = ["apple"]
        n_sentences = 1
        results = f_797(target_words, n_sentences, ["apple"] * 10)
        self.assertEqual(len(results), n_sentences)
        self.assertTrue(
            results[0].count("apple") > 1,
            "Multiple 'apple' occurrences not replaced correctly",
        )
    def test_case_3(self):
        # Test with no target words
        target_words = []
        n_sentences = 1
        results = f_797(target_words, n_sentences, self.vocabulary)
        self.assertEqual(len(results), n_sentences)
        self.assertTrue(all(" " in sentence for sentence in results), "")
    def test_case_4(self):
        # Test case sensitivity
        target_words = ["Apple Banana"]
        n_sentences = 2
        results = f_797(target_words, n_sentences, self.vocabulary + ["apple banana"])
        self.assertEqual(len(results), n_sentences)
        for result in results:
            self.assertIn(
                "apple_banana", result, "Case sensitivity not handled properly"
            )
    def test_case_5(self):
        # Test generating zero sentences
        target_words = ["apple"]
        n_sentences = 0
        results = f_797(target_words, n_sentences, self.vocabulary)
        self.assertEqual(len(results), n_sentences, "No sentences should be generated")
    def test_case_6(self):
        # Test function handling invalid inputs - vocabulary
        target_words = ["apple"]
        n_sentences = 1
        with self.assertRaises(ValueError):
            f_797(target_words, n_sentences, [])
    def test_case_7(self):
        # Test function handling invalid inputs - n_sentences
        target_words = ["apple"]
        with self.assertRaises(ValueError):
            f_797(target_words, -1, self.vocabulary)
        with self.assertRaises(TypeError):
            f_797(target_words, 1.0, self.vocabulary)
    def test_case_8(self):
        # Test whitespace target word
        target_words = [" "]
        n_sentences = 1
        results = f_797(target_words, n_sentences, ["apple banana", "cherry"])
        assert len(results[0].split("_")) >= 10
    def test_case_9(self):
        # Test target word not in vocabulary
        target_words = ["mango"]
        n_sentences = 2
        results = f_797(target_words, n_sentences, ["apple", "banana", "cherry"])
        for sentence in results:
            self.assertNotIn(
                "mango",
                sentence,
                "Target word not in vocabulary should not appear in sentences.",
            )
