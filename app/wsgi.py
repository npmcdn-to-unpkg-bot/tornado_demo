# coding=utf-8
import os
import logging.config
import yaml
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from url import urls
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Options
define("port", default=80, help="run on the given port", type=int)
define("debug", default=True, type=bool)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            static_url_prefix='/static/',
            cookie_secret='CIF4q7mZS/ankeZBnYubeHwQ8M19REjBoQaHiapQf30=',
            xsrf_cookies=True,  # 跨站请求伪造
            debug=True
        )
        engine = create_engine('mysql://root:root@localhost/assetss?charset=utf8')
        # engine = create_engine('mysql://test:123456@10.0.2.92:3307/test?charset=utf8')
        db_session = sessionmaker(bind=engine)
        self.db = db_session()
        tornado.web.Application.__init__(self, handlers, **settings)

        logging.config.dictConfig(yaml.load(open('common/logging.yaml', 'r')))


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()

