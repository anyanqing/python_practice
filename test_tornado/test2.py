# coding=utf-8

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self):
        self.render('templates/login.html')


class LoginHandler(RequestHandler):
    def get(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        self.write(username + ',' + password)

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        self.write(username + ',' + password)


app = Application([
    (r'^/$', IndexHandler),
    (r'^/login/$', LoginHandler)
])


app.listen(8888)


IOLoop.instance().start()
