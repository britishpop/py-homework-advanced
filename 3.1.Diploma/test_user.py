from classes import vk_users
import unittest
from mock import patch
from fixtures.user_data import raw_user
from fixtures.user_data import expect_user


class TestUser(unittest.TestCase):


    @patch('classes.vk_users.MainUser.data', return_value=raw_user) #говорит, что нет такого аттрибута
    def test_return_right_user_data(self, f):
        result = self.obj.get_user_data()
        self.assertEqual(result, expect_user)


    # def test_return_right_photos(self):
    #     data = [{'id': 288668576, 'likes': 1459882, 'url': 'https://pp.userapi.com/c7003/v7003978/1edb/S9N9m1NFFx4.jpg'}, {'id': 263219656, 'likes': 972081, 'url': 'https://pp.userapi.com/c9591/u00001/136592355/x_dbfafe4c.jpg'}, {'id': 263219735, 'likes': 868439, 'url': 'https://pp.userapi.com/c9591/u00001/136592355/x_d51dbfac.jpg'}]
    #     result = self.obj_2.get_top_3_photos()
    #     self.assertEqual(len(result), len(data))


if __name__ == '__main__':
    suite_1 = unittest.TestLoader().loadTestsFromTestCase(TestUser)
    unittest.TextTestRunner(verbosity=2).run(suite_1)
