# coding=utf-8
from tornado_mysql import pools
import MySQLdb

pools.DEBUG = True


POOL = pools.Pool(
    dict(host='127.0.0.1', port=3306, user='root', passwd='root', db='assetss', charset='utf8'),
    max_idle_connections=1,
    max_recycle_sec=3)


def safe(s):
    return MySQLdb.escape_string(s)