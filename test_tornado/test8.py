# coding=utf-8

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import MySQLdb


settings = {'debug': True}
db_config = {
    'host': 'db-d.dqprism.com',
    'db': 'datateam',
    'port': 3306,
    'user': 'daqi',
    'passwd': '7f1a45eac5985519829c929e7bbf0557'
}


class LoginHandler(RequestHandler):
    def initialize(self, conn):
        self.conn = conn

    def prepare(self):
        print('...................................')
        # 判断当前请求方式
        if self.request.method == 'POST':
            # 获取请求参数
            self.username = self.get_argument('username')
            self.password = self.get_argument('password')

    def get(self):
        self.render('templates/login.html')

    def post(self):
        cursor = self.conn.cursor()
        cursor.execute(f'select * from t_auser where username="{self.username}" and password="{self.password}"')
        user = cursor.fetchone()

        if user:
            self.write(u'登录成功！')
        else:
            self.write(u'登录失败！')

    def write_error(self, status_code, **kwargs):
        self.render('templates/error.html')

    def set_default_headers(self):
        self.set_header('Server', 'SHServer/1.0')


app = Application([
    (r'^/login/$', LoginHandler, {'conn': MySQLdb.connect(**db_config)})
], **settings)

app.listen(8888)

IOLoop.instance().start()

