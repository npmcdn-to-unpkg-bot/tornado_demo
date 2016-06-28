# coding=utf-8
import hashlib
import base64
import uuid
import ldap
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA


# md5加密
def md5(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


# 获取UUID
def get_uuid():
    return str(uuid.uuid1()).replace('-', '')


# 域登录
def check_login(p_host, p_user_name, p_pass_word):
    try:
        base_dn = 'CN=%s,OU=HMZX,OU=L3UR,DC=ad,DC=huimai365,DC=com' % p_user_name
        conn = ldap.initialize(p_host)
        conn.set_option(ldap.OPT_NETWORK_TIMEOUT, 0)
        conn.simple_bind_s()
        conn.simple_bind_s(base_dn, p_pass_word)
        return '3'
    except ldap.LDAPError, e:
        return '4'


# RSA解密密码
def t_decrypt(p_encrypt_text, p_private_key):
    random_generator = Random.new().read
    rsakey = RSA.importKey(p_private_key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(p_encrypt_text), random_generator)
    return text


if __name__ == '__main__':
    txt = 'V4btN7jav0WsJ6V2M3hL+xbj4ZdYkNiP0FXiE7wqCU7vGtTlvPkQPhZMNxeIfv20MTZUIC3p6zy7VJk/oADxRrEc4eQmB/WNy9V79GZIXTlLrKuf9dG0pf9M7UI2viHLgXrt4hrdYebmFRSF771P+Vxtjp4XlIKjmj/CbkKydw%3D%3D'
    from config import private_key
    from urllib import unquote
    print txt
    print unquote(txt)
    print base64.b64decode(unquote(txt))
    print t_decrypt(unquote(txt), private_key)
