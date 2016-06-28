# coding=utf-8
import json
from base import BaseRight
from models import BusinessStatus, BusinessStatus30, BusinessStatus60, BusinessStatusDay


class BusinessList(BaseRight):
    def get(self):
        self.render("business/list.html", user=self.get_current_user())


class BusinessItem(BaseRight):
    def get(self, item):
        if item in all_column.keys():
            self.render('business/detail.html', user=self.get_current_user(), item=item)
        else:
            self.render('business/item.html', user=self.get_current_user(), item=item)

all_column = {'login': u'登录', 'userinfo': u'查询用户基本信息', 'usercenter': u'进入用户中心', 'userid': u'查询用户',
              'gooddetail': u'查询商品详情',
              'colorstyle': u'查询商品规格', 'stock': u'查询库存', 'cartprice': u'查询购物车价格', 'addcart': u'添加购物车',
              'upcart': u'更新购物车',
              'getcart': u'查询购物车', 'goodsset': u'查询商品立减', 'userpoint': u'查询用户积分', 'userticket': u'查询购物车代金劵',
              'useraddr': u'查询默认地址', 'payconfig': u'查询支付配置',
              'order1': u'用户1库订单3库', 'order2': u'用户2库订单6库', 'order3': u'用户3库订单4库', 'order4': u'用户4库订单5库',
              'order5': u'用户5库订单2库', 'order6': u'用户6库订单1库'}

all_cateLinks = {'red': '/static/image/red.gif', 'green': '/static/image/green.gif'}
info_user = {'title': u'用户', 'title_link': '/business/info_user', 'column': ['login', 'userinfo', 'usercenter', 'userid', 'userpoint']}  # 登录-查询用户基本信息-进入用户中心-查询用户-查询用户积分
info_product = {'title': u'商品', 'title_link': '/business/info_product', 'column': ['gooddetail', 'colorstyle', 'stock', 'goodsset']}  # 查询商品详情-查询商品规格-查询库存-查询商品立减
info_cart = {'title': u'购物车', 'title_link': '/business/info_cart', 'column': ['cartprice', 'addcart', 'upcart', 'getcart', 'userticket']}  # 查询购物车价格-填加购物车-更新购物车-查询购物车-查询购物车代金劵
info_order = {'title': u'订单', 'title_link': '/business/info_order', 'column': ['order1', 'order2', 'order3', 'order4', 'order5', 'order6']}  # 查询订单列表-查询订单详情-取消订单-保存海外购订单-删除订单-保存订单
info_address = {'title': u'地址', 'title_link': '/business/info_address', 'column': ['useraddr']}  # 查询默认地址
info_payconfig = {'title': u'支付配置', 'title_link': '/business/info_payconfig', 'column': ['payconfig']}  # 支付配置

all_info = [info_user, info_product, info_cart, info_order]


class BusinessData(BaseRight):
    def get(self):
        obj_30 = self.db.query(BusinessStatus30).filter().order_by(BusinessStatus30.id.desc()).first()
        obj_30 = obj_30.__dict__ if obj_30 else {}

        obj_60 = self.db.query(BusinessStatus60).filter().order_by(BusinessStatus60.id.desc()).first()
        obj_60 = obj_60.__dict__ if obj_60 else {}

        obj_day = self.db.query(BusinessStatusDay).filter().order_by(BusinessStatusDay.id.desc()).first()
        obj_day = obj_day.__dict__ if obj_day else {}

        li_all = list()
        for k, v in enumerate(all_info):
            di = dict()
            li_gauge = list()
            li_bar = list()
            li_title = list()
            li_title_link = list()
            for col in v['column']:
                li_gauge.append(obj_30[col])
                li_bar.append([obj_60[col], obj_day[col]])
                li_title.append(all_column[col])
                li_title_link.append('/business/%s' % col)
            di['gauge'] = li_gauge
            di['bar'] = li_bar
            di['title'] = li_title
            di['title_link'] = li_title_link
            di['item_title'] = u'%s-可用图' % v['title']
            di['item_title_link'] = v['title_link']
            di['chance'] = float(sum(li_gauge)) / (len(li_gauge))
            li_all.append(di)
        li_all = sorted(li_all, key=lambda x: x['chance'])
        self.write(json.dumps(li_all))


class BusinessDataItem(BaseRight):
    def get(self, item):
        if item in all_column.keys():
            obj_60 = self.db.query(BusinessStatus60).filter().order_by(BusinessStatus60.id.desc()).first()
            obj_60 = obj_60.__dict__ if obj_60 else {}

            obj_day = self.db.query(BusinessStatusDay).filter().order_by(BusinessStatusDay.id.desc()).limit(30)
            # obj_day = obj_day.__dict__ if obj_day else {}

            obj_week = self.db.query(BusinessStatusDay).filter().order_by(BusinessStatusDay.id.desc()).limit(30)
            # obj_week = obj_week.__dict__ if obj_week else {}

            obj_month = self.db.query(BusinessStatusDay).filter().order_by(BusinessStatusDay.id.desc()).limit(30)
            # obj_month = obj_month.__dict__ if obj_month else {}

            all_data = dict()

            li_gauge = list()
            li_gauge.append(obj_60[item])
            li_gauge.append(obj_day[0].__dict__[item])
            li_gauge.append(obj_week[0].__dict__[item])
            li_gauge.append(obj_month[0].__dict__[item])
            all_data['gauge'] = li_gauge

            li_gauge_title = list()
            li_gauge.append(u'时')
            li_gauge.append(u'日')
            li_gauge.append(u'周')
            li_gauge.append(u'月')
            all_data['gauge_title'] = li_gauge_title

            li_bar_day = []
            li_bar_week = []
            li_bar_month = []

            li_bar_day_x = []
            li_bar_week_x = []
            li_bar_month_x = []

            for obj in obj_day:
                li_bar_day.append(obj.__dict__[item])
                li_bar_day_x.append(obj.__dict__['date'].strftime("%Y-%m-%d %H:%M:%S"))
            for obj in obj_week:
                li_bar_week.append(obj.__dict__[item])
                li_bar_week_x.append(obj.__dict__['date'].strftime("%Y-%m-%d %H:%M:%S"))
            for obj in obj_month:
                li_bar_month.append(obj.__dict__[item])
                li_bar_month_x.append(obj.__dict__['date'].strftime("%Y-%m-%d %H:%M:%S"))

            all_data['bar_day'] = li_bar_day
            all_data['bar_week'] = li_bar_week
            all_data['bar_month'] = li_bar_month

            all_data['bar_day_x'] = li_bar_day_x
            all_data['bar_week_x'] = li_bar_week_x
            all_data['bar_month_x'] = li_bar_month_x

            all_data['title'] = all_column[item]

            self.write(json.dumps(all_data))
        else:
            obj_30 = self.db.query(BusinessStatus30).filter().order_by(BusinessStatus30.id.desc()).first()
            obj_30 = obj_30.__dict__ if obj_30 else {}

            obj_60 = self.db.query(BusinessStatus60).filter().order_by(BusinessStatus60.id.desc()).first()
            obj_60 = obj_60.__dict__ if obj_60 else {}

            obj_day = self.db.query(BusinessStatusDay).filter().order_by(BusinessStatusDay.id.desc()).first()
            obj_day = obj_day.__dict__ if obj_day else {}

            all_data = dict()
            for k, v in enumerate(all_info):
                if item in v['title_link']:
                    li_gauge = list()
                    li_bar = list()
                    li_title = list()
                    li_title_link = list()
                    for col in v['column']:
                        li_gauge.append(obj_30[col])
                        li_bar.append([obj_60[col], obj_day[col]])
                        li_title.append(u'%s-可用图' % all_column[col])
                        li_title_link.append('/business/%s' % col)
                    all_data['gauge'] = li_gauge
                    all_data['bar'] = li_bar
                    all_data['title'] = li_title
                    all_data['title_link'] = li_title_link
                    # return make_response(json.dumps(all_data))
                    # all_data = json.dumps(all_data)
            obj_30 = self.db.query(BusinessStatus30).filter().order_by(BusinessStatus30.id.desc()).limit(5)
            for k, v in enumerate(all_info):
                if item in v['title_link']:
                    detail_column = v['column']

            li_detail = list()
            for obj in obj_30:
                li = list()
                for col in detail_column:
                    li.append(obj.__dict__[col])
                li_detail.append(li)
            all_data['detail_data'] = li_detail

            li_col = []
            for col in detail_column:
                li_col.append(all_column[col])
            all_data['detail_column'] = li_col

            self.write(json.dumps(all_data))
