import tempfile
import unittest

import pandas
from pandas.util.testing import assert_frame_equal

from lookout.style.typos.preprocessing import filter_splits, print_frequencies
from lookout.style.typos.utils import Columns


class PreprocessingTest(unittest.TestCase):
    def test_filter_splits(self):
        data = pandas.DataFrame([["get value", "get"],
                                 ["get value", "value"],
                                 ["gut", "gut"],
                                 ["put tok", "put"],
                                 ["put tok", "tok"],
                                 ["put", "put"]], columns=[Columns.Split, Columns.Token])
        vocabulary = {"get", "value", "put"}
        result = pandas.DataFrame([["get value", "get"],
                                   ["get value", "value"],
                                   ["put", "put"]], columns=[Columns.Split, Columns.Token],
                                  index=[0, 1, 5])
        assert_frame_equal(filter_splits(data, vocabulary), result)

    def test_print_frequencies(self):
        id_stats = pandas.DataFrame([[23], [6], [17]], columns=[Columns.Frequency],
                                    index=["get", "token", "set"])
        vocabulary = {"get", "set"}
        with tempfile.NamedTemporaryFile() as vocabulary_file:
            print_frequencies(vocabulary, id_stats, vocabulary_file.name)
            with open(vocabulary_file.name) as f:
                lines = []
                for line in f:
                    lines.append(line.strip())
            self.assertEqual(len(lines), 2)
            self.assertIn("get,23", lines)
            self.assertIn("set,17", lines)


if __name__ == "__main__":
    unittest.main()
