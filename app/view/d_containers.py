# coding=utf-8
import sys
import json
import logging
from base import BaseRight
from common import base_state
from common import base_docker


class ContainersList(BaseRight):
    _rightKey = base_state.ContainersManager
    _right = base_state.operation_view

    def get(self):
        self.render("d_containers/list.html", user=self.get_current_user())

    def post(self):
        containers = base_docker.Containers('192.168.128.128').list()
        self.write(json.dumps(containers))


class ContainersStart(BaseRight):
    _rightKey = base_state.ContainersManager
    _right = base_state.operation_view

    def post(self):
        id = self.get_argument('id', None)
        try:
            msg = base_docker.Containers('192.168.128.128').start(id)
        except Exception, ex:
            msg = 'error'
            logging.error(sys.exc_info())
        finally:
            pass

        di = dict()
        if msg is None:
            di['msg'] = 'ok'
        else:
            di['msg'] = 'error'
        self.write(di)


class ContainersStop(BaseRight):
    _rightKey = base_state.ContainersManager
    _right = base_state.operation_view

    def post(self):
        id = self.get_argument('id', None)
        print id
        msg = base_docker.Containers('192.168.128.128').stop(id)
        try:
            # msg = base_docker.Containers('192.168.128.128').stop(id)
            pass
        except Exception, ex:
            msg = 'error'
            logging.error(sys.exc_info())
        finally:
            pass

        di = dict()
        if msg is None:
            di['msg'] = 'ok'
        else:
            di['msg'] = 'error'
        self.write(di)


class ContainersDelete(BaseRight):
    _rightKey = base_state.ContainersManager
    _right = base_state.operation_view

    def post(self):
        id = self.get_argument('id', None)
        try:
            msg = base_docker.Containers('192.168.128.128').delete(id)
        except Exception, ex:
            msg = 'error'
            logging.error(sys.exc_info())
        finally:
            pass

        di = dict()
        if msg is None:
            di['msg'] = 'ok'
        else:
            di['msg'] = 'error'
        self.write(di)