# coding=utf-8

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36']


class AccessHandler(RequestHandler):
    def get(self):
        user_agent = self.request.headers['User-Agent']
        # 判断是否有权访问
        if user_agent not in user_agents:
            self.send_error(403)
        else:
            self.write('hello world!')


ip_cnt = {}
class LoginHandler(RequestHandler):
    def get(self):
        ip = self.request.remote_ip
        num = ip_cnt.get(ip, 0) + 1
        ip_cnt[ip] = num
        # 判断访问次数是否大于10
        if ip_cnt[ip] > 10:
            self.send_error(403)
        else:
            self.write('正常访问')


app = Application([
    (r'^/$', AccessHandler),
    (r'^/login/$', LoginHandler)
])

# app.listen(8888, '10.10.20.163')
app.listen(8888)

IOLoop.instance().start()
