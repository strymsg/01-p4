# main guide https://github.com/strymsg/01-p4/tree/master/POCS/redis

import redis

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
    print(r.get("Bahamas"))