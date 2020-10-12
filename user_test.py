import unittest
from user import Users
from user import Credentials
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = Users("Jeff", "1234")
    def test_init(self):
        self.assertEqual(self.new_user.username, "Jeff")
        self.assertEqual(self.new_user.password, "1234")

    def test_login(self):
        self.assertTrue(self.new_user.username, 'Jeff')
        self.assertTrue(self.new_user.password, '1234')
  
if __name__ == '__main__':
    unittest.main()