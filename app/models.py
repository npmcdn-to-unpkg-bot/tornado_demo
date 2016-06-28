# coding=utf-8
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime, Boolean, Enum, Float, Text
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
BaseModel = declarative_base()


class SSORole(BaseModel):
    __tablename__ = 'sso_role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50), unique=True)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())


class SSOUser(BaseModel):
    __tablename__ = 'sso_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    password = Column(String(50), default='')
    email = Column(String(50), default='')
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())
    role_id = Column(Integer, default=0)


class SSOFunc(BaseModel):
    __tablename__ = 'sso_func'
    id = Column(Integer, primary_key=True, autoincrement=True)
    func_name = Column(String(50), unique=True)
    parent_id = Column(Integer, default=0)
    path = Column(String(50), default='')
    rights = Column(String(50), default='')
    custom_json = Column(String(50), default='')
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())


class SSORoleRight(BaseModel):
    __tablename__ = 'sso_role_right'
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, default=0)
    func_id = Column(Integer, default=0)
    func_right = Column(String(50), default='')
    custom_right = Column(String(50), default='')
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())


class IDCRoom(BaseModel):
    __tablename__ = 'idc_room'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_name = Column(String(50), unique=True)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())


class IDCCabinet(BaseModel):
    __tablename__ = 'idc_cabinet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, default=0)
    cabinet_number = Column(String(50), unique=True)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())


class IDCHost(BaseModel):
    __tablename__ = 'idc_host'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(50), unique=True)
    os_version = Column(String(50), default='')
    room_id = Column(Integer, default=0)
    cabinet_id = Column(Integer, default=0)
    position = Column(String(50), default=0)
    status = Column(Enum("normal", "down", "offline", "repair", "unknown"), default="unknown")
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())


class HostStatus(BaseModel):
    __tablename__ = 'host_status'
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, default='')
    cpu = Column(Float, default=0.00)
    memory = Column(Float, default=0.00)
    disk = Column(Float, default=0.00)
    create_at = Column(DateTime, default=func.now())


class Email(BaseModel):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True)
    theme = Column(String(200), default='')
    content = Column(Text, default='')
    sender = Column(String(200), default='')
    address = Column(String(200), default='')
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())
    create_UserId = Column(Integer, default='')


class SMS(BaseModel):
    __tablename__ = 'sms'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String(50), default='')
    send_content = Column(String(200), default='')
    send_status = Column(String(50), default='')
    delete_mark = Column(Integer, default=0)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())
    create_userid = Column(String(50), default='')


class BusinessStatus(BaseModel):
    __tablename__ = 'business_status'
    id = Column(Integer, primary_key=True, default='')
    time = Column(String(50), default='')
    date = Column(String(50), default='')
    login = Column(Integer, default=0)
    userinfo = Column(Integer, default=0)
    usercenter = Column(Integer, default=0)
    userid = Column(Integer, default=0)
    gooddetail = Column(Integer, default=0)
    colorstyle = Column(Integer, default=0)
    stock = Column(Integer, default=0)
    cartprice = Column(Integer, default=0)
    addcart = Column(Integer, default=0)
    upcart = Column(Integer, default=0)
    getcart = Column(Integer, default=0)
    goodsset = Column(Integer, default=0)
    userpoint = Column(Integer, default=0)
    userticket = Column(Integer, default=0)
    useraddr = Column(Integer, default=0)
    saveorder = Column(Integer, default=0)
    payconfig = Column(Integer, default=0)
    orderlist = Column(Integer, default=0)
    orderdetail = Column(Integer, default=0)
    cancelorder = Column(Integer, default=0)
    oversea_save = Column(Integer, default=0)
    delorder = Column(Integer, default=0)
    order1 = Column(Integer, default=0)
    order2 = Column(Integer, default=0)
    order3 = Column(Integer, default=0)
    order4 = Column(Integer, default=0)
    order5 = Column(Integer, default=0)
    order6 = Column(Integer, default=0)


class BusinessStatus30(BaseModel):
    __tablename__ = 'business_status_30'
    id = Column(Integer, primary_key=True)
    date = Column(default=func.now())
    login = Column(Integer, default=0)
    userinfo = Column(Integer, default=0)
    usercenter = Column(Integer, default=0)
    userid = Column(Integer, default=0)
    gooddetail = Column(Integer, default=0)
    colorstyle = Column(Integer, default=0)
    stock = Column(Integer, default=0)
    cartprice = Column(Integer, default=0)
    addcart = Column(Integer, default=0)
    upcart = Column(Integer, default=0)
    getcart = Column(Integer, default=0)
    goodsset = Column(Integer, default=0)
    userpoint = Column(Integer, default=0)
    userticket = Column(Integer, default=0)
    useraddr = Column(Integer, default=0)
    saveorder = Column(Integer, default=0)
    payconfig = Column(Integer, default=0)
    orderlist = Column(Integer, default=0)
    orderdetail = Column(Integer, default=0)
    cancelorder = Column(Integer, default=0)
    oversea_save = Column(Integer, default=0)
    delorder = Column(Integer, default=0)
    order1 = Column(Integer, default=0)
    order2 = Column(Integer, default=0)
    order3 = Column(Integer, default=0)
    order4 = Column(Integer, default=0)
    order5 = Column(Integer, default=0)
    order6 = Column(Integer, default=0)


class BusinessStatus60(BaseModel):
    __tablename__ = 'business_status_60'
    id = Column(Integer, primary_key=True)
    date = Column(default=func.now())
    login = Column(Integer, default=0)
    userinfo = Column(Integer, default=0)
    usercenter = Column(Integer, default=0)
    userid = Column(Integer, default=0)
    gooddetail = Column(Integer, default=0)
    colorstyle = Column(Integer, default=0)
    stock = Column(Integer, default=0)
    cartprice = Column(Integer, default=0)
    addcart = Column(Integer, default=0)
    upcart = Column(Integer, default=0)
    getcart = Column(Integer, default=0)
    goodsset = Column(Integer, default=0)
    userpoint = Column(Integer, default=0)
    userticket = Column(Integer, default=0)
    useraddr = Column(Integer, default=0)
    saveorder = Column(Integer, default=0)
    payconfig = Column(Integer, default=0)
    orderlist = Column(Integer, default=0)
    orderdetail = Column(Integer, default=0)
    cancelorder = Column(Integer, default=0)
    oversea_save = Column(Integer, default=0)
    delorder = Column(Integer, default=0)
    order1 = Column(Integer, default=0)
    order2 = Column(Integer, default=0)
    order3 = Column(Integer, default=0)
    order4 = Column(Integer, default=0)
    order5 = Column(Integer, default=0)
    order6 = Column(Integer, default=0)


class BusinessStatusDay(BaseModel):
    __tablename__ = 'business_status_day'
    id = Column(Integer, primary_key=True)
    status_datetime = Column(default=func.now())
    login = Column(Integer, default=0)
    userinfo = Column(Integer, default=0)
    usercenter = Column(Integer, default=0)
    userid = Column(Integer, default=0)
    gooddetail = Column(Integer, default=0)
    colorstyle = Column(Integer, default=0)
    stock = Column(Integer, default=0)
    cartprice = Column(Integer, default=0)
    addcart = Column(Integer, default=0)
    upcart = Column(Integer, default=0)
    getcart = Column(Integer, default=0)
    goodsset = Column(Integer, default=0)
    userpoint = Column(Integer, default=0)
    userticket = Column(Integer, default=0)
    useraddr = Column(Integer, default=0)
    saveorder = Column(Integer, default=0)
    payconfig = Column(Integer, default=0)
    orderlist = Column(Integer, default=0)
    orderdetail = Column(Integer, default=0)
    cancelorder = Column(Integer, default=0)
    oversea_save = Column(Integer, default=0)
    delorder = Column(Integer, default=0)
    order1 = Column(Integer, default=0)
    order2 = Column(Integer, default=0)
    order3 = Column(Integer, default=0)
    order4 = Column(Integer, default=0)
    order5 = Column(Integer, default=0)
    order6 = Column(Integer, default=0)


if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('mysql://root:root@localhost/assetss?charset=utf8', echo=True)
    BaseModel.metadata.create_all(engine)

