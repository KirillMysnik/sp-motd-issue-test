# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from http.server import BaseHTTPRequestHandler, HTTPServer, HTTPStatus
from threading import Thread

# Source.Python
from commands.typed import TypedSayCommand
from listeners.tick import Delay
from messages import SayText2, VGUIMenu


# =============================================================================
# >> CONSTANTS
# =============================================================================
HTTPD_PORT = 8080
URL_TEMPLATE = f"http://localhost:{HTTPD_PORT}" + "/TOTAL_URLS_SENT={counter}"


# =============================================================================
# >> CLASSES
# =============================================================================
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        msg = SayText2(f"Received request: {self.path}")
        Delay(0, msg.send)  # Execute in the nearest tick

        self.send_response(HTTPStatus.OK)
        self.end_headers()


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
urls_sent = 0
httpd = None


# =============================================================================
# >> COMMANDS
# =============================================================================
@TypedSayCommand('!test')
def typed_say_test(command_info):
    global urls_sent
    urls_sent += 1

    url = URL_TEMPLATE.format(counter=urls_sent)

    # Broadcast chat message
    SayText2(f"Sending URL: {url}").send()

    # Send MoTD to the player
    VGUIMenu(
        name='info',
        show=True,
        subkeys={
            'title': "motd (valve fix pls)",
            'type': '2',
            'msg': url,
        }
    ).send(command_info.index)


# =============================================================================
# >> LOAD / UNLOAD
# =============================================================================
def load():
    global httpd
    httpd = HTTPServer(('', HTTPD_PORT), MyHTTPRequestHandler)
    Thread(target=httpd.serve_forever).start()


def unload():
    global httpd
    if httpd is None:
        return

    httpd.shutdown()
    httpd.socket.close()
    httpd = None
