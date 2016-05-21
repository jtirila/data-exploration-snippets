# Import the module to be tested

import sys
sys.path.append('../')
import prepare_data

# Import some other dependencies

import unittest
import csv
import os

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'simple_test_file.csv')

class TestPrepareData(unittest.TestCase):

    def test_read_csv_file_with_automatic_dialect_specification(self):
        """As automatic dialect detection fails for this particular test
           file, expect an error to be raised."""

        with self.assertRaises(csv.Error):
            prepare_data.read_csv_file(TESTDATA_FILENAME)[0]

    def test_read_csv_file_with_manual_dialect_specification(self):
        """When called with the dialect parameters in place, expect the
           read to be successful by comparing the first entry of the 
           result to an expected value."""

        self.assertEqual(
                prepare_data.read_csv_file(TESTDATA_FILENAME, 
                                           delimiter = ",", quotechar = "|", 
                                           has_header = True)[0], 
                ["Row0","val0","0"])

if __name__ == '__main__':
        unittest.main()
