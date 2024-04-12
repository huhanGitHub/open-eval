import itertools
import string
import pandas as pd
import matplotlib.pyplot as plt


def f_876():
    """
    Generate all possible 3-letter combinations of the alphabet, save them in a pandas DataFrame,
    and draw a histogram of the frequency of the first letters in these combinations.

    This function uses itertools.product to create all possible combinations of three letters.
    It then creates a DataFrame from these combinations and plots a histogram to show the frequency
    of each letter appearing as the first letter in these combinations.

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame with all 3-letter combinations.
        - Axes: A matplotlib Axes object representing the histogram plot.

    Requirements:
    - itertools
    - string
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df, ax = f_876()
    >>> print(df.head())
       a  b  c
    0  a  a  a
    1  a  a  b
    2  a  a  c
    3  a  a  d
    4  a  a  e
    """
    LETTERS = list(string.ascii_lowercase)
    combinations = list(itertools.product(LETTERS, repeat=3))
    df = pd.DataFrame(combinations, columns=["a", "b", "c"])

    # Getting value counts and ensuring the correct order of letters
    value_counts = df["a"].value_counts().reindex(LETTERS, fill_value=0)

    # Plotting the histogram with the correct order
    ax = value_counts.plot(kind="bar")

    return df, ax


import unittest
import itertools
import string

LETTERS = list(string.ascii_lowercase)


class TestCases(unittest.TestCase):
    """Tests for the function f_876"""

    def test_dataframe_shape(self):
        """
        Test if the DataFrame has the correct shape (17576 rows, 3 columns)
        """
        df, _ = f_876()
        self.assertEqual(df.shape, (17576, 3))

    def test_dataframe_columns(self):
        """
        Test if the DataFrame has the correct column names (a, b, c)
        """
        df, _ = f_876()
        self.assertListEqual(list(df.columns), ["a", "b", "c"])

    def test_histogram_plot(self):
        """
        Test if the histogram plot is an instance of matplotlib Axes
        """
        _, ax = f_876()
        self.assertTrue(isinstance(ax, plt.Axes))

    def test_first_column_values(self):
        """
        Test if the first column of the DataFrame contains only lowercase letters
        """
        df, _ = f_876()
        self.assertTrue(all(letter in string.ascii_lowercase for letter in df["a"]))

    def test_no_empty_values(self):
        """
        Test if there are no empty values in the DataFrame
        """
        df, _ = f_876()
        self.assertFalse(df.isnull().values.any())

    def tearDown(self):
        plt.close()


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()