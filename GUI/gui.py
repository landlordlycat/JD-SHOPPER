import os
import signal
from Config import config

PROJECT = config.Information.project
SERVER_HOST = config.Server.server_host
PORT = config.Server.port

def gui():
    url = "http://{}:{}/".format(SERVER_HOST, PORT)

    # def on_closed():
    #     os.kill(os.getpid(), signal.SIGTERM)

    # import webview
    # window = webview.create_window(PROJECT,
    #                       url=url,
    #                       js_api=None,
    #                       width=900,
    #                       height=800,
    #                       resizable=True,
    #                       fullscreen=False,
    #                       min_size=(200, 200),
    #                       background_color='#FFF',
    #                       text_select=False)
    # window.events.closed += on_closed
    # webview.start()
