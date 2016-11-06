import unittest
from application import Application

class Test_Create_Client(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_create_client(self):
        self.app.add_client()
        # success Login asserts: Client is created
        self.app.login_as_client()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()



