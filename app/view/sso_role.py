# coding=utf-8
import tornado.web
from tornado import gen
from base import BaseRight
from models import SSORole, SSORoleRight
from common import base_state


class SSORoleList(BaseRight):
    _rightKey = base_state.RoleManager
    _right = base_state.operation_view

    def get(self):
        self.render("sso_role/list.html", user=self.get_current_user())

    def post(self):
        parameters = self.get_args(['role_name', 'page_index'], None)
        query = self.db.query(SSORole)
        if parameters['role_name']:
            query = query.filter_by(role_name=parameters['role_name'])
        query = query.order_by(SSORole.id.desc())

        di_all_data = self.get_query(query)

        self.write(di_all_data)


class SSORoleAdd(BaseRight):
    _rightKey = base_state.RoleManager
    _right = base_state.operation_add

    def get(self):
        self.render("sso_role/add.html", user=self.get_current_user())

    def post(self):
        obj = SSORole()
        for k, v in self.request.arguments.items():
            obj.__dict__[k[5:]] = v[0]
        print obj.__dict__
        self.db.add(obj)
        self.db.commit()
        self.redirect('/sso_role/list')


class SSORoleUpdate(BaseRight):
    _rightKey = base_state.RoleManager
    _right = base_state.operation_edit

    def get(self, id):
        hosts = self.db.query(SSORole).filter(SSORole.id == id).first()
        self.render("sso_role/update.html", user=self.get_current_user(), obj=hosts)

    def post(self, id):
        up = grep_update(self.request)
        print up
        self.db.query(SSORole).filter(SSORole.id == id).update(up)
        self.redirect('/sso_role/list')


class SSORoleDel(BaseRight):
    _rightKey = base_state.RoleManager
    _right = base_state.operation_del

    def post(self, id):
        di = dict()
        id = self.get_argument('id', 0)
        msg = self.db.query(SSORoleRight).filter(SSORoleRight.role_id == id).delete()
        msg = self.db.query(SSORole).filter(SSORole.id == id).delete()
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
