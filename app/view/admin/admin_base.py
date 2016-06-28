# -*- encoding: utf-8 -*-

import tornado.web
from datetime import datetime

import config
from common import base_state, base_redis
from helper import str_helper
from handler import base_handler
from logic import oper_log_logic


class AdminBaseHandler(base_handler.BaseHandler):
    def get_current_user(self):
        uuid = self.get_cookie('soc_user_right')
        if uuid is None:
            return None
        user = base_redis.get_obj(uuid)
        return user

    def is_edit(self):
        return 'edit' in self.request.path.lower()

    def clear_user_info(self):
        uuid = self.get_cookie('soc_user_right')
        if uuid is None:
            return None
        base_redis.delete(uuid)
        self.clear_all_cookies()

    def check_operation_right(self, right=None, user=None):
        # 判断用户权限'
        if right is None:
            right = self._right

        if self._rightKey is None or self._rightKey == '' or right is None or right == 0:
            return
        if user is None:
            user = self.current_user

        rights = user.get('rights', [])
        o_type = False
        for r in rights:
            if r.get('path', '') == self._rightKey:
                if r.get('right', 0) & right == right:
                    o_type = True
                break
        if not o_type:
            if self.get_arg('ajax', '') == 'ajax':
                self.out_fail(code=1004)
                self.finish()
            else:
                self.redirect('/Admin/NotRight')
            return

    def check_operation_right_custom_right(self, right_key, custom_right):
        user = self.current_user
        rights = user.get('rights', [])
        for r in rights:
            if r.get('path', '') != right_key:
                continue
            crs = r.get('customRight', [])
            for cr in crs:
                if custom_right == cr:
                    return True
            return False
        return False


class AdminRightBaseHandler(AdminBaseHandler):
    _rightKey = ''
    _right = 0

    _resetPwKey = 'ResetPassword'
    _exportUserKey = 'Export'
    _lockUserKey = 'Lock'

    def prepare(self):
        super(AdminRightBaseHandler, self).prepare()
        user = self.current_user
        if user is None:
            ''' 判断用户是否存在,如果不存在,重新登录 '''
            self.redirect('/login')
            return
        self.check_oper_right()


