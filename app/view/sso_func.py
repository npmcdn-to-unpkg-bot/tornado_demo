# coding=utf-8
import tornado.web
from tornado import gen
from base import BaseRight
from models import SSOFunc
from common import base_state


class SSOFuncList(BaseRight):
    _rightKey = base_state.FuncManager
    _right = base_state.operation_view

    def get(self):
        self.render("sso_func/list.html", user=self.get_current_user())

    def post(self):
        parameters = self.get_args(['func_name', 'path', 'page_index'], None)
        query = self.db.query(SSOFunc)
        if parameters['func_name']:
            query = query.filter_by(func_name=parameters['func_name'])
        if parameters['path']:
            query = query.filter_by(path=parameters['path'])
        query = query.order_by(SSOFunc.id.desc())

        di_all_data = self.get_query(query)
        self.write(di_all_data)


class SSOFuncAdd(BaseRight):
    _rightKey = base_state.FuncManager
    _right = base_state.operation_add

    def get(self):
        self.render("sso_func/add.html", user=self.get_current_user())

    def post(self):
        obj = SSOFunc()
        for k, v in self.request.arguments.items():
            obj.__dict__[k[5:]] = v[0]
        print obj.__dict__
        self.db.add(obj)
        self.db.commit()
        self.redirect('/sso_func/list')


class SSOFuncUpdate(BaseRight):
    _rightKey = base_state.FuncManager
    _right = base_state.operation_edit

    def get(self, id):
        obj = self.db.query(SSOFunc).filter(SSOFunc.id == id).first()
        self.render("sso_func/update.html", user=self.get_current_user(), obj=obj)

    def post(self, id):
        up = grep_update(self.request)
        print up
        self.db.query(SSOFunc).filter(SSOFunc.id == id).update(up)
        self.redirect('/sso_func/list')


class SSOFuncDel(BaseRight):
    _rightKey = base_state.FuncManager
    _right = base_state.operation_del

    def post(self, id):
        di = dict()
        id = self.get_argument('id', 0)
        msg = self.db.query(SSOFunc).filter(SSOFunc.id == id).delete()
        self.db.commit()
        if msg == 1:
            di['msg'] = 'ok'
        else:
            di['msg'] = 'error'
        self.write(di)


def grep_update(req):
    update = {}
    for k, v in req.arguments.items():
        if k.startswith("obj__"):
            update[k[5:]] = v
    return update
