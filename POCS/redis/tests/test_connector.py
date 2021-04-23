from connector import RedisConnector
import unittest
def test_1():
    assert True

class TestRedisConnector(unittest.TestCase):
    def test_connect(self):
        r = RedisConnector()
        self.assertTrue(r.connection is not None)

    def test_set(self):
        r = RedisConnector()
        r.connection.mset({'ding': 'DONG!'})
        res = r.connection.get('ding').decode('utf-8')
        self.assertEqual(res, 'DONG!')
