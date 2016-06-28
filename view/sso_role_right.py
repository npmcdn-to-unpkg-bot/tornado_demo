# coding=utf-8
import json
import tornado.web
from tornado import gen
from base import BaseRight
from models import SSOFunc, SSORoleRight
from common import base_state


class SSORoleRightUpdate(BaseRight):
    _rightKey = base_state.RoleBindRightManager
    _right = base_state.operation_edit

    def get(self, id):
        objs = self.db.query(SSORoleRight).filter(SSORoleRight.role_id == id).order_by(SSORoleRight.id.asc())
        rights = dict()
        for obj in objs:
            rights[obj.func_id] = json.loads(obj.func_right)

        html_data = ''
        funcs = self.db.query(SSOFunc).order_by(SSOFunc.id.asc())
        for func in funcs:
            html_data += '<div class="control-group">'
            html_data += '<label class="control-label">%s</label>' % func.func_name
            html_data += '<div class="controls">'
            for right in func.rights.split(';'):
                right_key = right.split(':')[0]
                right_value = right.split(':')[1]
                if func.id in rights and right_key in rights[func.id]:
                    html_data += '<label><input type="checkbox" name="obj__%s" value="%s" checked />%s</label>' % (func.id, right_key, right_value)
                else:
                    html_data += '<label><input type="checkbox" name="obj__%s" value="%s" />%s</label>' % (func.id, right_key, right_value)
            html_data += '</div>'
        self.render("sso_role_right/update.html", user=self.get_current_user(), html_data=html_data)

    def post(self, id):
        up = grep_update(self.request)
        for k, v in up.items():
            obj = self.db.query(SSORoleRight).filter(SSORoleRight.role_id == id, SSORoleRight.func_id == k).first()
            if obj:
                obj.func_right = json.dumps(v)
                self.db.commit()
            else:
                obj = SSORoleRight()
                obj.role_id = int(id)
                obj.func_id = int(k)
                obj.func_right = json.dumps(v)
                obj.custom_right = None
                self.db.add(obj)
                self.db.commit()
        self.redirect('/sso_role/list')


def grep_update(req):
    update = {}
    for k, v in req.arguments.items():
        if k.startswith("obj__"):
            update[k[5:]] = v
    return update


