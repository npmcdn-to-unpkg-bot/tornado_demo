from admin_base import AdminRightBaseHandler
from common import base_state


class Index(AdminRightBaseHandler):
    _rightKey = 'SOCRight.HostManager'
    _right = base_state.operation_view

    def get(self):
        user = self.get_current_user()
        self.render("/admin/index.html", user=user)

