# coding=utf-8
import json
from base import BaseRight
from common import base_state
from common import base_docker


class ContainersList(BaseRight):
    _rightKey = base_state.ContainersManager
    _right = base_state.operation_view

    def get(self):
        self.render("d_containers/list.html", user=self.get_current_user())


class ContainersData(BaseRight):
    _rightKey = base_state.ContainersManager
    _right = base_state.operation_view

    def post(self):
        room_id = self.get_arg('room_id', 1)
        containers = base_docker.Docker('192.168.128.128').containers()
        self.write(json.dumps(containers))
