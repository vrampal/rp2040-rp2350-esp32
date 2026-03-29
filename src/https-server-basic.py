import board
import digitalio
import os
import socketpool
import wifi
from adafruit_httpserver import JSONResponse, Request, Response, Server

# Define fields CIRCUITPY_WIFI_SSID and CIRCUITPY_WIFI_PASSWORD in settings.toml
# See: https://docs.circuitpython.org/projects/httpserver/en/stable/starting_methods.html

# --- Initialization ---
print(f"IP address = {wifi.radio.ipv4_address}")
print(f"Router     = {wifi.radio.ipv4_gateway}")
print(f"DNS server = {wifi.radio.ipv4_dns}")
pool = socketpool.SocketPool(wifi.radio)
server = Server(
    pool,
    root_path="/static",
    https=True,
    certfile="demo-selfsigned-ecdsa.pem",
    keyfile="demo-selfsigned-ecdsa.key",
    debug=True
)

@server.route("/")
def index(request: Request):
    uname = os.uname()
    return Response(
        request,
        content_type="text/plain",
        body=f"Hello from CircuitPython.\nMachine: {uname.machine}\nVersion: {uname.version}"
    )
    
@server.route("/api")
def api(request: Request):
    uname = os.uname()
    return JSONResponse( request, {
        "title":"Hello from CircuitPython",
        "message":"This is a JSON API",
        "machine":uname.machine,
        "version":uname.version
    })

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

@server.route("/led_on")
def led_on(request: Request):
    led.value = True
    return Response(request, content_type="text/plain", body="Done")

@server.route("/led_off")
def led_off(request: Request):
    led.value = False
    return Response(request, content_type="text/plain", body="Done")

# --- Main ---
host = str(wifi.radio.ipv4_address)
server.start(host, port=443)
while True:
    # Do tasks between server poll
    try:
        server.poll()
    except OSError as error:
        print(f"Error {error.strerror} with code {error.errno}")