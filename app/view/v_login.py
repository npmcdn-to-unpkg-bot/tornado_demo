# coding=utf-8
import sys
import datetime
import logging
from urllib import unquote
from tornado import gen
from base import Base
from common import base_redis
from common import base_mysql
from common import base_misc
from models import SSOUser, SSORole, SSORoleRight, SSOFunc
from common import base_config


class Login(Base):
    def get(self):
        self.render("login.html")

    @gen.coroutine
    def post(self):
        try:
            account = self.get_argument("Account")
            password = self.get_argument("Password")
            password = base_misc.t_decrypt(unquote(password), base_config.private_key)

            if account and password:
                # 域验证
                msg = base_misc.check_login(base_config.ldap_config['ldap_host'], account, password)
                if msg == '3':
                    role = self.db.query(SSORole).filter(SSORole.role_name == 'guest').first()
                    role_id = 0
                    if role:
                        role_id = role.id

                    di_funcs = dict()
                    funcs = self.db.query(SSOFunc)
                    for func in funcs:
                        di_funcs[func.id] = func.path

                    li_right = list()
                    role_rights = self.db.query(SSORoleRight).filter(SSORoleRight.role_id == role_id)
                    for obj in role_rights:
                        di = dict()
                        di['id'] = obj.id
                        di['path'] = di_funcs[obj.func_id]
                        di['right'] = obj.func_right
                        di['customRight'] = []
                        li_right.append(di)

                    di_user = dict()
                    di_user['id'] = 0
                    di_user['username'] = account
                    di_user['rights'] = li_right

                    print '-----', di_user

                    uuid = base_misc.get_uuid()
                    base_redis.set_obj(uuid, di_user, base_redis.cache['userTimeOut'])
                    self.clear_all_cookies()
                    ex = datetime.datetime.now() + datetime.timedelta(minutes=30)
                    self.set_secure_cookie(name='soc_user_right', value=uuid, expires=ex)
                if msg == '4':
                    # obj = self.db.query(User).filter(User.username == account).first()
                    # 数据库账号验证
                    user = yield login(account, password)
                    if user:
                        msg = '3'
                        uuid = base_misc.get_uuid()
                        base_redis.set_obj(uuid, user, base_redis.cache['userTimeOut'])
                        self.clear_all_cookies()
                        ex = datetime.datetime.now() + datetime.timedelta(minutes=30)
                        self.set_secure_cookie(name='soc_user_right', value=uuid, expires=ex)
            else:
                msg = '5'
        except Exception, ex:
            msg = '1'
            logging.error(sys.exc_info())
        finally:
            pass

        self.write(msg)
        # -1  登录账户不存在
        # 1   登录失败
        # 2   登录账户被系统锁定
        # 4   登录账号或者密码错误
        # 3   登录验证成功,正在跳转首页
        # 5   用户名或者密码为空


@gen.coroutine
def login(username, password):
    user = yield base_mysql.POOL.execute("select id, username, password, role_id from sso_user where username=%s", (base_mysql.safe(username)))
    user = user.fetchone()
    if user and user[2] == base_misc.md5(password):
        role_rights = yield base_mysql.POOL.execute("SELECT sso_role_right.id, sso_func.path, sso_role_right.func_right, sso_role_right.custom_right FROM sso_role_right inner join sso_func on sso_role_right.func_id = sso_func.id where sso_role_right.role_id=%s", (user[3]))
        li_right = list()
        for obj in role_rights:
            di = dict()
            di['id'] = obj[0]
            di['path'] = obj[1]
            di['right'] = obj[2]
            di['customRight'] = []
            li_right.append(di)

        di_user = dict()
        di_user['id'] = user[0]
        di_user['username'] = user[1]
        di_user['rights'] = li_right
        raise gen.Return(di_user)
    else:
        raise gen.Return({})


class Logout(Base):
    def get(self):
        self.clear_user_info()
        self.redirect('/login')
