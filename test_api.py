import unittest


class MyTestCase(unittest.TestCase):
    def test_db_connection(self):
        self.assertEqual(True, False)

    def test_endpoints(self):
        pass


if __name__ == '__main__':
    unittest.main()
