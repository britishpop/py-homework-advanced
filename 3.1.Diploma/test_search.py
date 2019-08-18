from functionality import saver
import unittest

from fixtures.user_data import expect_user
from fixtures.user_data import criteria
from fixtures.user_data import filtered_data
from fixtures.user_data import raw_data

class TestFiltering(unittest.TestCase):

    def test_return_right_score(self):
        result = saver.get_score_for_user(expect_user, criteria)
        self.assertEqual(result, 103)


    def test_filtering_users(self):
        result = saver.filter_for_users(raw_data, criteria)
        self.assertEqual(result, filtered_data)


if __name__ == '__main__':
    suite_1 = unittest.TestLoader().loadTestsFromTestCase(TestFiltering)
    unittest.TextTestRunner(verbosity=2).run(suite_1)
