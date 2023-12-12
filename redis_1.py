import redis

r = redis.StrictRedis(host='nadejnei.net', port = 16379, password = '123456')
r.set('kirill', '1', ex=20)
result = r.get('kirill')

print(result.decode())