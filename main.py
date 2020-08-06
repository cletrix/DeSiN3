import tornado.ioloop
import tornado.web
import datetime

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        now = datetime.datetime.now()
        self.write("Server ok " + now.strftime("%Y-%m-%d %H:%M:%S"))

class Ping(tornado.web.RequestHandler):
    def get(self):
        self.write("pong")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ping", Ping),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()