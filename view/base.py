# coding=utf-8
import json
from common import base_redis
import tornado.web

from common.base_page import build_page_html


class Base(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        uuid = self.get_secure_cookie('soc_user_right')
        if uuid:
            user = base_redis.get_obj(uuid)
        else:
            user = None
        return user

    def clear_user_info(self):
        self.clear_all_cookies()

    def get_arg(self, key, default=None, strip=True):
        val = self.get_argument(key, default, strip)
        if val is not None and isinstance(val, unicode):
            val = val.encode('utf-8')
        return val

    def get_args(self, ls=[], default=None, map={}):
        for l in ls:
            map[l] = self.get_arg(l, default)
        return map

    def get_query(self, query=None):
        page_index = int(self.get_arg('page_index', '1'))
        page_size = 15
        query_total = query.count()
        if query_total % page_size == 0:
            page_total = query_total / page_size
        else:
            page_total = query_total / page_size + 1
        query = query.limit(page_size).offset((page_index - 1) * page_size).all()

        di = dict()
        li = list()
        for q in query:
            q = q.__dict__
            if '_sa_instance_state' in q:
                del q['_sa_instance_state']

            if q['create_at']:
                q['create_at'] = q['create_at'].strftime('%Y-%m-%d %H:%M:%S')
            if q['update_at']:
                q['update_at'] = q['update_at'].strftime('%Y-%m-%d %H:%M:%S')
            li.append(q)
        di['page_index'] = page_index
        di['rows'] = li
        di['page_info'] = build_page_html(page_index, page_total)
        return di

    def check_operation_right(self, right=None, user=None):
        # 判断用户权限'
        rightKey = self._rightKey
        right = self._right
        user = self.current_user
        if rightKey and right and user:
            rights = user.get('rights', [])
            o_type = False
            for r in rights:
                if r.get('path', '') == self._rightKey:
                    li_right = r.get('right', [])
                    if li_right and str(right) in li_right:
                        o_type = True
                    break

            if not o_type:
                self.redirect('/NotRight')
        else:
            self.redirect('/NotRight')

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('sys_error/404.html')
        elif status_code == 500:
            self.render('sys_error/500.html')
        else:
            # super(Base, self).write_error(status_code, **kwargs)
            self.render('sys_error/error.html')


class BaseUserRight(Base):
    def prepare(self):
        super(BaseUserRight, self).prepare()
        user = self.get_current_user()
        if not user:
            ''' 判断用户是否存在,如果不存在,重新登录 '''
            self.redirect('/login')
            return


class BaseRight(Base):
    _rightKey = ''
    _right = 0

    def prepare(self):
        super(BaseRight, self).prepare()
        user = self.get_current_user()
        if not user:
            ''' 判断用户是否存在,如果不存在,重新登录 '''
            self.redirect('/login')
            return
        self.check_operation_right()


