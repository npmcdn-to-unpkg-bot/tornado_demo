# -*- encoding: utf-8 -*-
import redis
import json

# redis缓存配置，根据实际情况修改
cache = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0,

    # 用户信息超时时间，秒
    'userTimeOut': 86400,
    # authtoken超时时间，秒
    'userRightTimeOut': 600,
    # authtoken超时时间，秒
    'apiTimeOut': 3600,
}

_conn = None
_cachekeypre = 'soc_right_user_%s'


def _get_redis():
    global _conn
    if not _conn:
        _conn = redis.ConnectionPool(host=cache['host'], port=cache['port'], db=cache['db'])
    return redis.Redis(connection_pool=_conn)


def get_str(key):
    r = _get_redis()
    key = _cachekeypre % key
    return r.get(key)


def set_str(key, val, time=0):
    r = _get_redis()
    key = _cachekeypre % key
    if time <= 0:
        r.set(key, val)
    else:
        r.setex(key,  val, time)


def delete(key):
    r = _get_redis()
    key = _cachekeypre % key
    return r.delete(key)


def get_obj(key):
    r = _get_redis()
    key = _cachekeypre % key
    val = r.get(key)
    if val is None:
        return None
    return json.loads(val)


def set_obj(key, val, time=0):
    if val is None:
        return
    json_val = json.dumps(val)
    r = _get_redis()
    key = _cachekeypre % key
    if time <= 0:
        r.set(key, json_val)
    else:
        r.setex(key,  json_val, time)


