import redis

class RedisConnector:
    def __init__(self, host='localhost', port=6379, password=''):
        try:
            self.connection = redis.Redis(host=host, port=port)
        except Exception as err:
            print(err)
            raise err
