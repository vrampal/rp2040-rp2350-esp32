import socketpool
import wifi
from adafruit_httpserver import JSONResponse, Request, Response, Server

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)

@server.route("/")
def index(request: Request):
    return Response(request, "Hello, this is the index.")

@server.route("/api")
def index(request: Request):
    return JSONResponse(request, {"title":"Hello", "body":"this is the API"})


server.serve_forever(str(wifi.radio.ipv4_address))
