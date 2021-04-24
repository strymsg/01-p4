from connector import RedisConnector
import unittest
import json
from datetime import timedelta
import time

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
            #print(f'>>>> {key}')
            #print(r.exists(key))
            #print(key, r.mget(key))
            self.assertNotEqual(r.mget(key), None)

    def test_hset_and_pipeline(self):
        r = RedisConnector().get_connection()
        regs = {
            'gf1': 'Done',
            'gf2': 'Chess',
            'gf3': 'Swipe',
        }
        with r.pipeline() as pipe:
            for key, value in regs.items():
                pipe.hset('hsetv1', key, value)
            pipe.execute()
            self.assertEqual(r.bgsave(), True)

        for field, value in regs.items():
            resp = r.hget('hsetv1', field)
            #print(f'>> {resp} {resp.decode("utf-8")} {regs[field]}')
            self.assertEqual(resp.decode('utf-8'), regs[field])

    def test_set_serialized(self):
        r = RedisConnector().get_connection()
        d = {
            'lista': [1,2,4,'c'],
            'clista': [-5,23, 2.4, 'com'],
            'dd': {'almacen1': 'San Diego'}
        }
        r.set('obj1', json.dumps(d))
        self.assertEqual(r.get('obj1').decode('utf-8'), json.dumps(d))
        #print('GET')
        #print(r.get('obj1'))
        #print(r.get('obj1').decode('utf-8'))

    def test_key_expiry(self):
        r = RedisConnector().get_connection()
        r.setex("runner", timedelta(seconds=2), value="exists")
        #print(r.get("runner"))
        #print(r.ttl("runner"), r.pttl("runner"))
        self.assertEqual(r.get("runner").decode('utf-8'), "exists")
        time.sleep(1)
        # time to live should have decreased some value
        self.assertLess(r.pttl("runner"), 2000)
        #self.assertEqual(r.pttl("runner"), )