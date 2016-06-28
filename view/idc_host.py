# coding=utf-8
import tornado.web
from tornado import gen
from base import BaseRight
from models import IDCRoom, IDCCabinet, IDCHost
from common import base_state


class IDCList_test_02(BaseRight):
    @gen.engine
    def get(self):
        self.render("idc_host/idc_test_02.html", user=self.get_current_user())

    @gen.engine
    def post(self):
        room_id = self.get_arg('room_id', 1)
        cabinets = self.db.query(IDCCabinet).filter(IDCCabinet.room_id == room_id)
        html_data = ''
        for obj in cabinets:
            html_data += u'<div class="span2">'   ##  style="width: 147px;"
            html_data += u'<div class="widget-box">'
            html_data += u'<div class="widget-title"><span class ="icon"><i class="icon-th"></i></span><h5>%s 柜</h5></div>' % (obj.id)
            html_data += u'<div class="widget-content" style="background:url(/images/serverico/box.jpg); height: 630px;">'
            html_data += u'<table border="0" cellpadding="1" cellspacing="0" width="99%"><tr><td align="center" height="10" valign="bottom"></td></tr>'

            li_data = dict()
            for i in range(1, 25):
                li_data[i] = u'<tr><td class="jgtable" align="center" height="20" valign="bottom"></td></tr>'

            hosts = self.db.query(IDCHost).filter(IDCHost.cabinet_id == obj.id).order_by(IDCHost.u_start)
            for host in hosts:
                if host.u_start in li_data:
                    h_pic = '%su_%s.gif' % (host.u_number, host.status)
                    h_high = 23 * host.u_number - 3
                    print '----:', h_high, h_pic, host.ip, host.os_version, host.room_id, host.cabinet_id, host.u_start, host.u_number


                    li_data[host.u_start] = u'<tr><td class="jgtable" align="center" height="%s" valign="bottom"><img src="/images/serverico/%s" style="vertical-align: bottom;" height="12" width="127" id="example2" data-content="IP:%s<br>操作系统：%s<br>位置：%s-%s-%s<br>型号:%sU" data-placement="right" data-toggle="popover" data-original-title=""></td></tr>' % (h_high, h_pic, host.ip, host.os_version, host.room_id, host.cabinet_id, host.u_start, host.u_number)
                    for i in range(host.u_start+1, host.u_start + host.u_number):
                        if i in li_data:
                            del li_data[i]

            for k, v in li_data.items():
                print v
                html_data += v

            html_data += '</table></div></div></div>'
        self.write(html_data)


class IDCList_test_01(BaseRight):
    @gen.engine
    def get(self):
        self.render("idc_host/idc_test_01.html", user=self.get_current_user())

    @gen.engine
    def post(self):
        room_id = self.get_arg('room_id', 1)
        cabinets = self.db.query(IDCCabinet).filter(IDCCabinet.room_id == room_id)
        html_data = ''
        for obj in cabinets:
            html_data += u'<div class="span2" style="width: 147px;">'
            html_data += u'<div class="widget-box">'
            html_data += u'<div class="widget-title"><span class ="icon"><i class="icon-th"></i></span><h5>%s 柜</h5></div>' % (obj.id)
            html_data += u'<div class="widget-content" style="background:url(/images/serverico/jg.jpg); height: 570px;">'
            html_data += u'<table border="0" cellpadding="1" cellspacing="0" width="99%"><tr><td align="center" height="10" valign="bottom"></td></tr>'

            li_data = dict()
            for i in range(1, 25):
                li_data[i] = u'<tr><td class="jgtable" align="center" height="20" valign="bottom"></td></tr>'

            hosts = self.db.query(IDCHost).filter(IDCHost.cabinet_id == obj.id).order_by(IDCHost.u_start)
            for host in hosts:
                if host.u_start in li_data:
                    h_pic = '%su_%s.gif' % (host.u_number, host.status)
                    h_high = 23 * host.u_number - 3

                    li_data[host.u_start] = u'<tr><td class="jgtable" align="center" height="%s" valign="bottom"><img src="/images/serverico/%s" style="vertical-align: bottom;" height="12" width="127" id="example2" data-content="IP:%s<br>操作系统：%s<br>位置：%s-%s-%s<br>机型：%sU" data-placement="right" data-toggle="popover" data-original-title=""></td></tr>' % (
                        h_high, h_pic, host.ip, host.os_version, host.room_id, host.cabinet_id, host.u_start, host.u_number)
                    for i in range(host.u_start+1, host.u_start + host.u_number):
                        if i in li_data:
                            del li_data[i]

            for k, v in li_data.items():
                html_data += v

            html_data += u'</table></div></div></div>'
        self.write(html_data)


class IDCList(BaseRight):
    _rightKey = base_state.HostManager
    _right = base_state.operation_view

    @gen.engine
    def get(self):
        self.render("idc_host/idc.html", user=self.get_current_user())

    @gen.engine
    def post(self):
        room_id = self.get_arg('room_id', 1)

        row_number = 1  # 第一排
        html_data = u''
        for cabinet in range(0, 14):
            if cabinet % 7 == 0:
                html_data += u'<div align="center">%02d排</div>' % row_number
                html_data += u'<table class="jjtable" bgcolor="#ffffff" border="0" cellpadding="1" cellspacing="3" width="1024">'
                html_data += u'<tbody>'
                html_data += u'<tr align="center" valign="top">'

            html_data += u'<td background="/images/serverico/jg.gif" bgcolor="#eeeeee" width="147">'
            html_data += u'<table border="0" cellpadding="1" cellspacing="0" height="440" width="99%">'
            html_data += u'<tbody><tr><td class="jgtable" align="center" height="30" valign="bottom"> <font class="jgtitle">%s</font></td></tr>' % (cabinet + 1)

            li_data = dict()
            for i in range(1, 14):
                li_data[i] = u'<tr><td class="jgtable" align="center" height="30" valign="bottom"> <font class="jgtitle">&nbsp;</font></td></tr>'

            hosts = self.db.query(IDCHost).filter(IDCHost.room_id == room_id, IDCHost.cabinet_id == (cabinet + 1)).order_by(IDCHost.position)
            for host in hosts:
                li_u = host.position.split('-')
                u_start = int(li_u[0])
                u_end = int(li_u[1])
                u_number = u_end - u_start + 1
                if u_start in li_data:
                    h_pic = '%su_%s.gif' % (u_number, host.status)
                    td_high = 30 * u_number
                    pic_hight = 12 * u_number

                    li_data[u_start] = u'<tr><td class="jgtable" align="center" height="%s" valign="bottom"><img src="/images/serverico/%s" style="vertical-align: bottom; cursor: pointer;" height="%s" width="127" id="example2" data-content="IP:%s<br>操作系统：%s<br>位置：%s-%s-%s<br>型号:%sU" data-placement="right" data-toggle="popover" data-original-title="" onclick="window.open(\'/host/view/%s\')"></td></tr>' % (td_high, h_pic, pic_hight, host.ip, host.os_version, host.room_id, host.cabinet_id, u_start, u_number, host.id)
                    for i in range(u_start + 1, u_end + 1):
                        if i in li_data:
                            del li_data[i]

            for k, v in li_data.items():
                html_data += v

            html_data += u'</tbody></table>'
            html_data += u'</td>'

            if (cabinet + 1) % 7 == 0:
                html_data += u'</tr>'
                html_data += u'</tbody>'
                html_data += u'</table><p>&nbsp;</p>'
                row_number += 1
        self.write(html_data)


class IDCList_back(BaseRight):
    @gen.engine
    def get(self):
        self.render("idc_host/idc.html", user=self.get_current_user())

    @gen.engine
    def post(self):
        room_id = self.get_arg('room_id', 1)
        cabinets = self.db.query(IDCCabinet).filter(IDCCabinet.room_id == room_id).order_by(IDCCabinet.id.asc())
        di_all = dict()
        for obj in cabinets:
            hosts = self.db.query(IDCHost).filter(IDCHost.room_id == obj.room_id, IDCHost.cabinet_id == obj.id)
            di_cabinet = {x: None for x in range(1, 11)}
            for host in hosts:
                d = dict()
                d['ip'] = host.ip
                d['os_version'] = host.os_version
                d['u_number'] = host.u_number
                d['u_position'] = '%02d-%02d-%02d' % (host.room_id, host.cabinet_id, host.u_start)
                di_cabinet[host.u_start] = d
                for y in range(host.u_start + 1, host.u_start + host.u_number):
                    if y in di_cabinet:
                        del di_cabinet[y]
            di_all[obj.id] = di_cabinet
        self.write(di_all)


class HostList(BaseRight):
    _rightKey = base_state.HostManager
    _right = base_state.operation_view

    def get(self):
        cabinets = self.db.query(IDCCabinet).order_by(IDCCabinet.id.asc())
        self.render("idc_host/list.html", user=self.get_current_user(), cabinets=cabinets)

    def post(self):
        parameters = self.get_args(['ip', 'cabinet_id', 'page_index'], None)
        query = self.db.query(IDCHost)
        if parameters['ip']:
            query = query.filter_by(ip=parameters['ip'])
        if parameters['cabinet_id'] and int(parameters['cabinet_id']) > 0:
            query = query.filter_by(cabinet_id=parameters['cabinet_id'])
            query = query.order_by(IDCHost.u_start.asc())
        else:
            query = query.order_by(IDCHost.id.desc())

        di_all_data = self.get_query(query)

        for k, v in enumerate(di_all_data['rows']):
            di_all_data['rows'][k]['status'] = base_state.host_state[di_all_data['rows'][k]['status']]

        self.write(di_all_data)


class HostAdd(BaseRight):
    _rightKey = base_state.HostManager
    _right = base_state.operation_add

    def get(self):
        rooms = self.db.query(IDCRoom).order_by(IDCRoom.id.asc())
        cabinets = self.db.query(IDCCabinet).order_by(IDCCabinet.id.asc())
        self.render("idc_host/add.html", user=self.get_current_user(), rooms=rooms, cabinets=cabinets)

    def post(self):
        obj = IDCHost()
        for k, v in self.request.arguments.items():
            obj.__dict__[k[5:]] = v[0]
        print obj.__dict__
        self.db.add(obj)
        self.db.commit()
        self.redirect('/host/list')


class HostUpdate(BaseRight):
    _rightKey = base_state.HostManager
    _right = base_state.operation_edit

    def get(self, id):
        rooms = self.db.query(IDCRoom).order_by(IDCRoom.id.asc())
        cabinets = self.db.query(IDCCabinet).order_by(IDCCabinet.id.asc())
        hosts = self.db.query(IDCHost).filter(IDCHost.id == id).first()
        self.render("idc_host/update.html", user=self.get_current_user(), rooms=rooms, cabinets=cabinets, obj=hosts)

    def post(self, id):
        up = grep_update(self.request)
        print up
        self.db.query(IDCHost).filter(IDCHost.id == id).update(up)
        self.db.commit()
        self.redirect('/host/list')


class HostDel(BaseRight):
    _rightKey = base_state.HostManager
    _right = base_state.operation_del

    def post(self, id):
        di = dict()
        id = self.get_argument('id', 0)
        msg = self.db.query(IDCHost).filter(IDCHost.id == id).delete()
        self.db.commit()
        if msg == 1:
            di['msg'] = 'ok'
        else:
            di['msg'] = 'error'
        self.write(di)


class HostView(BaseRight):
    _rightKey = base_state.HostManager
    _right = base_state.operation_view

    def get(self, id):
        hosts = self.db.query(IDCHost).filter(IDCHost.id == id).first()
        rooms = self.db.query(IDCRoom).filter(IDCRoom.id == hosts.room_id).first()
        cabinets = self.db.query(IDCCabinet).filter(IDCCabinet.id == hosts.cabinet_id).first()
        hosts.__dict__['host_status'] = base_state.host_state[hosts.status]
        hosts.__dict__['host_room'] = u'未知'
        hosts.__dict__['host_cabinet'] = u'未知'
        if rooms:
            hosts.__dict__['host_room'] = rooms.name
        if cabinets:
            hosts.__dict__['host_cabinet'] = cabinets.number

        self.render("idc_host/view.html", user=self.get_current_user(), obj=hosts)


def grep_update(req):
    update = {}
    for k, v in req.arguments.items():
        if k.startswith("obj__"):
            update[k[5:]] = v
    return update
