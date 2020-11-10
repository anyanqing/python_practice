# coding=utf-8

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import os


class UploadHandler(RequestHandler):
    def get(self):
        self.render('templates/upload.html')

    def post(self):
        # 获取请求参数
        image = self.request.files['image']
        # print(image)
        # 遍历image
        for img in image:
            body = img.get("body", '')
            filename = img.get("filename", '')
            content_type = img.get("content_type", '')

        # 把图片存放到目录中
        dir = os.path.join(os.getcwd(), 'files', filename)
        with open(dir, 'wb') as fw:
            fw.write(body)

        # 将图片显示到浏览器页面
        # 设置响应头的信息
        self.set_header('Content-Type', content_type)
        self.write(body)


app = Application([
    (r'^/upload/$', UploadHandler)
])

app.listen(8888)

IOLoop.instance().start()
