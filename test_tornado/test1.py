# coding=utf-8
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop


# 创建处理类
class IndexHandler(RequestHandler):
    def get(self):
        self.write("Hello Tornado!")


# 创建Application对象（即配置路由）
app = Application([
    (r'/', IndexHandler)
])


# 绑定监听端口
app.listen(8888)


# 启动监听
IOLoop.instance().start()
