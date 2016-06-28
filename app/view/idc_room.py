# coding=utf-8
import tornado.web
from tornado import gen
from base import BaseRight
from models import IDCRoom
from common import base_state


class RoomList(BaseRight):
    _rightKey = base_state.RoomManager
    _right = base_state.operation_view

    def get(self):
        self.render("idc_room/list.html", user=self.get_current_user())

    def post(self):
        parameters = self.get_args(['room_name', 'page_index'], None)
        query = self.db.query(IDCRoom)
        if parameters['room_name']:
            query = query.filter_by(name=parameters['room_name'])
        query = query.order_by(IDCRoom.id.desc())

        di_all_data = self.get_query(query)
        self.write(di_all_data)


class RoomAdd(BaseRight):
    _rightKey = base_state.RoomManager
    _right = base_state.operation_add

    def get(self):
        self.render("idc_room/add.html", user=self.get_current_user())

    def post(self):
        obj = IDCRoom()
        for k, v in self.request.arguments.items():
            obj.__dict__[k[5:]] = v[0]
        print obj.__dict__
        self.db.add(obj)
        self.db.commit()
        self.redirect('/room/list')


class RoomUpdate(BaseRight):
    _rightKey = base_state.RoomManager
    _right = base_state.operation_edit

    def get(self, id):
        rooms = self.db.query(IDCRoom).filter(IDCRoom.id == id).first()
        self.render("idc_room/update.html", user=self.get_current_user(), obj=rooms)

    def post(self, id):
        up = grep_update(self.request)
        print up
        self.db.query(IDCRoom).filter(IDCRoom.id == id).update(up)
        self.redirect('/room/list')


class RoomDel(BaseRight):
    _rightKey = base_state.RoomManager
    _right = base_state.operation_del

    def post(self, id):
        di = dict()
        id = self.get_argument('id', 0)
        msg = self.db.query(IDCRoom).filter(IDCRoom.id == id).delete()
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
