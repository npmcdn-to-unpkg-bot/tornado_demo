# coding=utf-8
import os
from tornado.web import StaticFileHandler
from view.v_login import Login, Logout
from view.v_index import Index, Default, NotRight, ErrorHandler

from view.idc_host import HostList, HostAdd, HostUpdate, HostDel, IDCList, IDCList_test_01, IDCList_test_02, HostView
from view.idc_room import RoomList, RoomAdd, RoomUpdate, RoomDel
from view.idc_cabinet import CabinetList, CabinetAdd, CabinetUpdate, CabinetDel
from view.sso_role import SSORoleList, SSORoleAdd, SSORoleUpdate, SSORoleDel
from view.sso_user import SSOUserList, SSOUserAdd, SSOUserUpdate, SSOUserDel
from view.sso_func import SSOFuncList, SSOFuncAdd, SSOFuncUpdate, SSOFuncDel
from view.sso_role_right import SSORoleRightUpdate
from view.v_business import BusinessList, BusinessData, BusinessItem, BusinessDataItem
from view.v_system import SystemList, SystemDetail, SystemListData, SystemDetailData
from view.v_email import EmailList, EmailData
from view.v_sms import SMSList, SMSData
from view.d_images import ImagesList, ImagesData
from view.d_containers import ContainersList, ContainersData



urls = [
    # 静态文件
    (r'/css/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'static/css')}),
    (r'/js/(.*)', StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static/js")}),
    (r'/images/(.*)', StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static/images")}),
    (r'/img/(.*)', StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static/img")}),
    (r'/font-awesome/(.*)', StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static/font-awesome")}),
    (r'/Content/(.*)', StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "static/Content")}),

    (r'/', Default),
    (r'/index', Index),
    (r'/login', Login),
    (r'/logout', Logout),

    (r'/host/list', HostList),
    (r'/host/add', HostAdd),
    (r'/host/update/(\d+)', HostUpdate),
    (r'/host/delete/(\d+)', HostDel),
    (r'/idc', IDCList),
    (r'/idc_test_01', IDCList_test_01),
    (r'/idc_test_02', IDCList_test_02),
    (r'/host/view/(\d+)', HostView),

    (r'/room/list', RoomList),
    (r'/room/add', RoomAdd),
    (r'/room/update/(\d+)', RoomUpdate),
    (r'/room/delete/(\d+)', RoomDel),

    (r'/cabinet/list', CabinetList),
    (r'/cabinet/add', CabinetAdd),
    (r'/cabinet/update/(\d+)', CabinetUpdate),
    (r'/cabinet/delete/(\d+)', CabinetDel),

    (r'/sso_role/list', SSORoleList),
    (r'/sso_role/add', SSORoleAdd),
    (r'/sso_role/update/(\d+)', SSORoleUpdate),
    (r'/sso_role/delete/(\d+)', SSORoleDel),

    (r'/sso_user/list', SSOUserList),
    (r'/sso_user/add', SSOUserAdd),
    (r'/sso_user/update/(\d+)', SSOUserUpdate),
    (r'/sso_user/delete/(\d+)', SSOUserDel),

    (r'/sso_func/list', SSOFuncList),
    (r'/sso_func/add', SSOFuncAdd),
    (r'/sso_func/update/(\d+)', SSOFuncUpdate),
    (r'/sso_func/delete/(\d+)', SSOFuncDel),
    (r'/sso_role_right/update/(\d+)', SSORoleRightUpdate),

    (r"/business", BusinessList),
    (r"/business/(\w+)", BusinessItem),
    (r"/api/business_data", BusinessData),
    (r"/api/business_data/(\w+)", BusinessDataItem),

    (r"/image/list", ImagesList),
    (r"/api/image/list", ImagesData),

    (r"/containers/list", ContainersList),
    (r"/api/containers/list", ContainersData),

    (r"/system", SystemList),
    (r"/system/detail/(\w+)", SystemDetail),
    (r"/api/system_data", SystemListData),
    (r"/api/system_data/(\w+)", SystemDetailData),

    (r"/email", EmailList),
    (r"/api/email_data", EmailData),

    (r"/sms", SMSList),
    (r"/api/sms_data", SMSData),

    (r'/NotRight', NotRight),
    (r'.*', ErrorHandler),
]

