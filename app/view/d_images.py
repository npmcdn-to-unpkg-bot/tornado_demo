# coding=utf-8
import sys
import json
import docker
import logging
from base import BaseRight
from common import base_state
from common import base_docker


class ImagesList(BaseRight):
    _rightKey = base_state.ContainersManager
    _right = base_state.operation_view

    def get(self):
        self.render("d_images/list.html", user=self.get_current_user())

    def post(self):
        name = self.get_argument('name', '')
        try:
            images = base_docker.Images('192.168.128.128').list(name)
        except Exception, ex:
            images = []
            logging.error(sys.exc_info())
        finally:
            self.write(json.dumps(images))


class ImagesDel(BaseRight):
    _rightKey = base_state.ContainersManager
    _right = base_state.operation_del

    def post(self, id):
        try:
            msg = base_docker.Images('192.168.128.128').remove(id)
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
