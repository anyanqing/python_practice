# coding=utf-8

from tornado.web import RequestHandler, Application, RedirectHandler
from tornado.ioloop import IOLoop
from tornado.routing import URLSpec


# 重定向的三种方式
class IndexHandler(RequestHandler):
    def get(self):
        pass
        # 方法1 默认302重定向
        # self.redirect('https://www.baidu.com')
        # 方法2
        self.set_status(302)
        self.set_header('Location', 'https://www.jd.com')


class LoginHandler(RequestHandler):
    def get(self):
        self.redirect(self.reverse_url('index'))



app = Application([
    (r'^/$', IndexHandler),
    # 方法3
    (r'^/redirect/$', RedirectHandler, {'url': 'https://www.taobao.com'}),
    (r'^/login/$', LoginHandler),
    URLSpec(R'^/index/$', IndexHandler, name='index')
])

app.listen(8888)

IOLoop.instance().start()

