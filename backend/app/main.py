import json
import falcon

class Ping(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_202
        resp.body = json.dumps('pong!')

app = falcon.API()

app.add_route('/', Ping())
