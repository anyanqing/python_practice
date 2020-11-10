# coding=utf-8


from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import MySQLdb


class RegisterHandler(RequestHandler):
    def initialize(self, conn) -> None:
        self.conn = conn
        print(conn)

    def get(self):
        self.render('templates/register.html')

    def post(self):
        # 获取请求参数
        username = self.get_argument('username')
        password = self.get_argument('password')

        # 将用户名密码存入数据库
        try:
            cursor = self.conn.cursor()
            cursor.execute(f'insert into t_auser (username, password, create_time) values ("{username}", "{password}", now())')
            self.conn.commit()
            self.write('注册成功！')
        except Exception as e:
            self.conn.rollback()
            self.redirect('/register/')


def _getConn():
    return MySQLdb.connect(
        host='db-d.dqprism.com',
        database='datateam',
        port=3306,
        user='daqi',
        password='7f1a45eac5985519829c929e7bbf0557'
    )  # 沙盒mysql


app = Application([
    (r'^/register/$', RegisterHandler, {'conn': _getConn()})
])

app.listen(8888)

IOLoop.instance().start()
