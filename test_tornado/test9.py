# coding=utf-8

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop


class CookieHandler(RequestHandler):
    def get(self):
        # self.set_cookie('username', 'admin', expires_days=3)
        self.set_secure_cookie('hello', 'zhangsan', expires_days=3)


class GetCookieHandler(RequestHandler):
    def get(self):
        # username = self.get_cookie('username')
        username = self.get_secure_cookie('hello')
        self.write(username)


# app = Application([
#     (r'^/$', CookieHandler),
#     (r'^/getCookie/$', GetCookieHandler),
# ])

settings = {'cookie_secret': 'abcde'}
app = Application([
    (r'^/$', CookieHandler),
    (r'^/getCookie/$', GetCookieHandler),
], **settings)

app.listen(8888)

IOLoop.instance().start()
