# coding=utf-8
import tornado.web
from tornado import gen
from base import BaseRight
from models import SSOUser, SSORole
from common import base_state


class SSOUserList(BaseRight):
    _rightKey = base_state.UserManager
    _right = base_state.operation_view

    def get(self):
        roles = self.db.query(SSORole).order_by(SSORole.id.asc())
        self.render("sso_user/list.html", user=self.get_current_user(), roles=roles)

    def post(self):
        parameters = self.get_args(['username', 'email', 'role_id', 'page_index'], None)
        query = self.db.query(SSOUser)
        if parameters['username']:
            query = query.filter_by(username=parameters['username'])
        if parameters['email']:
            query = query.filter_by(email=parameters['email'])
        if parameters['role_id'] and int(parameters['role_id']) > 0:
            query = query.filter_by(role_id=parameters['role_id'])

        query = query.order_by(SSOUser.id.desc())
        di_all_data = self.get_query(query)

        di_roles = dict()
        roles = self.db.query(SSORole)
        for role in roles:
            di_roles[role.id] = role.role_name

        for k, v in enumerate(di_all_data['rows']):
            di_all_data['rows'][k]['role_name'] = di_roles[di_all_data['rows'][k]['role_id']]
        self.write(di_all_data)


class SSOUserAdd(BaseRight):
    _rightKey = base_state.UserManager
    _right = base_state.operation_add

    def get(self):
        roles = self.db.query(SSORole).order_by(SSORole.id.asc())
        self.render("sso_user/add.html", user=self.get_current_user(), roles=roles)

    def post(self):
        obj = SSOUser()
        for k, v in self.request.arguments.items():
            obj.__dict__[k[5:]] = v[0]
        print obj.__dict__
        self.db.add(obj)
        self.db.commit()
        self.redirect('/sso_user/list')


class SSOUserUpdate(BaseRight):
    _rightKey = base_state.UserManager
    _right = base_state.operation_edit

    def get(self, id):
        roles = self.db.query(SSORole).order_by(SSORole.id.asc())
        obj = self.db.query(SSOUser).filter(SSOUser.id == id).first()
        self.render("sso_user/update.html", user=self.get_current_user(), roles=roles, obj=obj)

    def post(self, id):
        up = grep_update(self.request)
        print up
        self.db.query(SSOUser).filter(SSOUser.id == id).update(up)
        self.redirect('/sso_user/list')


class SSOUserDel(BaseRight):
    _rightKey = base_state.UserManager
    _right = base_state.operation_del

    def post(self, id):
        di = dict()
        id = self.get_argument('id', 0)
        msg = self.db.query(SSOUser).filter(SSOUser.id == id).delete()
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
