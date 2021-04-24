from connector import RedisConnector
import unittest
def test_1():
    assert True

class TestRedisConnector(unittest.TestCase):
    def test_connect(self):
        r = RedisConnector().get_connection()
        self.assertTrue(r is not None)

    def test_set(self):
        r = RedisConnector().get_connection()
        r.mset({'ding': 'DONG!'})
        res = r.get('ding').decode('utf-8')
        self.assertEqual(res, 'DONG!')

    def test_iterate(self):
        r = RedisConnector().get_connection()
        for key in r.scan_iter():
            print(f'>>>> {key}')
            print(r.exists(key))
            print(key, r.mget(key))
            self.assertNotEqual(r.mget(key), None)

    def test_pipeline(self):
        r = RedisConnector().get_connection()
        regs = {
            'gf1': {'Do': 'Done', 'Done': 51},
            'gf2': {'Do': 'Chess', 'Done': 77},
            'gf3': {'Do': 'Swipe', 'Done': 824},
        }
        with r.pipeline() as pipe:
            for key, value in regs.items():
                pipe.hmset(key, value)
            pipe.execute()
            self.assertEqual(r.bgsave(), True)

        for key, value in regs.items():
            resp = r.hgetall(key)
            print("lllllllllllll")
            print(resp)
            self.assertNotEqual(resp, None)
            for k1, v1 in regs[key].items():
                print(f'{k1}: {v1}')
                print(resp, type(resp))
                print(resp.get(k1, '0000>0'))
                self.assertEqual(resp[k1] == v1)