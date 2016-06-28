# coding=utf-8
import datetime
import json

from base import BaseRight
from common.base_page import build_page_html
from models import IDCHost, HostStatus


class SystemList(BaseRight):
    def get(self):
        self.render('system/list.html', user=self.get_current_user())


class SystemDetail(BaseRight):
    def get(self, item):
        self.render('system/detail.html', user=self.get_current_user(), item=item)


class SystemListData(BaseRight):
    def get(self):
        page_index = int(self.get_arg('page_index', '1'))
        page_size = 4

        hosts = self.db.query(IDCHost).order_by(IDCHost.id.desc())
        query_total = hosts.count()
        page_total = query_total / page_size + 1
        hosts = hosts.limit(page_size).offset((page_index - 1) * page_size).all()
        di = dict()
        li_all = list()
        for host in hosts:
            host_status = self.db.query(HostStatus).filter(HostStatus.host_id == host.id).order_by(HostStatus.id.desc()).first()

            d = dict()
            d['ip'] = host.ip
            d['id'] = host.id
            d['value'] = list()
            if host_status:
                d['value'].append(host_status.cpu)
                d['value'].append(host_status.memory)
                d['value'].append(host_status.disk)
            else:
                d['value'].append(100.00)
                d['value'].append(100.00)
                d['value'].append(100.00)
            li_all.append(d)
        di['rows'] = li_all
        di['page_info'] = build_page_html(page_index, page_total)
        self.write(json.dumps(di))


class SystemDetailData(BaseRight):
    def post(self, item):
        di = dict()
        li_cpu = list()
        li_memory = list()
        li_disk = list()

        li_cpu_x = list()
        li_memory_x = list()
        li_disk_x = list()
        objs = self.db.query(HostStatus).filter(HostStatus.host_id == item).order_by(HostStatus.id.desc())
        if objs.count() > 0:
            objs = objs.limit(30)
            for obj in objs:
                li_cpu.append(obj.cpu)
                li_cpu_x.append(obj.create_at.strftime("%Y-%m-%d %H:%M:%S"))

                li_memory.append(obj.memory)
                li_memory_x.append(obj.create_at.strftime("%Y-%m-%d %H:%M:%S"))

                li_disk.append(obj.disk)
                li_disk_x.append(obj.create_at.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            li_cpu.append(0)
            li_cpu_x.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            li_memory.append(0)
            li_memory_x.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            li_disk.append(0)
            li_disk_x.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        di['cpu'] = [li_cpu_x, li_cpu]
        di['memory'] = [li_memory_x, li_memory]
        di['disk'] = [li_disk_x, li_disk]
        self.write(json.dumps(di))
