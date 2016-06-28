# coding=utf-8
import tornado.web
from tornado import gen
from base import BaseRight
from models import IDCRoom, IDCCabinet
from common import base_state


class CabinetList(BaseRight):
    _rightKey = base_state.CabinetManager
    _right = base_state.operation_view

    def get(self):
        rooms = self.db.query(IDCRoom).order_by(IDCRoom.id.asc())
        self.render("idc_cabinet/list.html", user=self.get_current_user(), rooms=rooms)

    def post(self):
        parameters = self.get_args(['room_id', 'page_index'], None)
        query = self.db.query(IDCCabinet)
        if parameters['room_id'] and int(parameters['room_id']) > 0:
            query = query.filter_by(room_id=parameters['room_id'])
        query = query.order_by(IDCCabinet.id.asc())
        di_all_data = self.get_query(query)

        rooms = dict()
        for cur in self.db.query(IDCRoom):
            rooms[cur.id] = cur.room_name

        for k, v in enumerate(di_all_data['rows']):
            if v['room_id'] in rooms:
                v['room'] = rooms[v['room_id']]
            else:
                v['room'] = 'unknown'
        self.write(di_all_data)


class CabinetAdd(BaseRight):
    _rightKey = base_state.CabinetManager
    _right = base_state.operation_add

    def get(self):
        rooms = self.db.query(IDCRoom).order_by(IDCRoom.id.asc())
        self.render("idc_cabinet/add.html", user=self.get_current_user(), rooms=rooms)

    def post(self):
        obj = IDCCabinet()
        for k, v in self.request.arguments.items():
            obj.__dict__[k[5:]] = v[0]
        print obj.__dict__
        self.db.add(obj)
        self.db.commit()
        self.redirect('/cabinet/list')


class CabinetUpdate(BaseRight):
    _rightKey = base_state.CabinetManager
    _right = base_state.operation_edit

    def get(self, id):
        rooms = self.db.query(IDCRoom).order_by(IDCRoom.id.asc())
        cabinets = self.db.query(IDCCabinet).filter(IDCCabinet.id == id).first()

        self.render("idc_cabinet/update.html", user=self.get_current_user(), rooms=rooms, obj=cabinets)

    def post(self, id):
        up = grep_update(self.request)
        self.db.query(IDCCabinet).filter(IDCCabinet.id == id).update(up)
        self.redirect('/cabinet/list')


class CabinetDel(BaseRight):
    _rightKey = base_state.CabinetManager
    _right = base_state.operation_del

    def post(self, id):
        di = dict()
        id = self.get_argument('id', 0)
        msg = self.db.query(IDCCabinet).filter(IDCCabinet.id == id).delete()
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
