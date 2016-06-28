# coding=utf-8
import tornado
from base import BaseRight
from base import BaseUserRight


class Index(BaseRight):
    _rightKey = 'SOCRight.Index'
    _right = 1

    def get(self):
        self.render("index.html", user=self.get_current_user())


class Default(BaseRight):
    _rightKey = 'SOCRight.Index'
    _right = 1

    def get(self):
        self.redirect('/index')


class NotRight(BaseUserRight):
    def get(self):
        self.render("sys_error/no_right.html", user=self.get_current_user())


class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('sys_error/404.html')
        elif status_code == 500:
            self.render('sys_error/500.html')
        else:
            self.write('error:' + str(status_code))

