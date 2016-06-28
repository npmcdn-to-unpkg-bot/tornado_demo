# coding=utf-8
import json
from base import BaseRight
from common import base_state
from common import base_docker


class ImagesList(BaseRight):
    _rightKey = base_state.ContainersManager
    _right = base_state.operation_view

    def get(self):
        self.render("d_images/list.html", user=self.get_current_user())


class ImagesData(BaseRight):
    _rightKey = base_state.ContainersManager
    _right = base_state.operation_view

    def post(self):
        images = base_docker.Docker('192.168.128.128').images()
        self.write(json.dumps(images))
